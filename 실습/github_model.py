# 필수 라이브러리와 모듈을 임포트
# torch, torchvision, tensorboardX, numpy, matplotlib 등을 포함
import os

import shutil
import numpy as np
import torch
from torchvision import models

from tensorboardX import SummaryWriter

import copy
from torch.utils.data import random_split
from matplotlib import pyplot as plt
from logger import setup_logger
from data_loader import CustomDataset
from model import resume_checkpoint, mkdir, Model
from torchvision.models import ResNet50_Weights
import torch.nn as nn

import argparse
from torch.utils import data

# 명령줄 인자 파싱
## 이는 딥러닝 모델 학습과 평가에 필요한 다양한 설정
def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--name", default="100%/1,2,3", type=str)
    parser.add_argument("--img_path", default="dataset/img", type=str)
    parser.add_argument("--loss_dir", default="tensorboard", type=str)
    parser.add_argument("--stop_early", type=int, default=30)
    parser.add_argument("--mode", default="class", choices=["regression", "class"], type=str)
    parser.add_argument("--json_path", default="dataset/label", type=str)
    parser.add_argument("--output_dir", default="checkpoint", type=str)
    parser.add_argument("--epoch", default=300, type=int)
    parser.add_argument("--res", default=128, type=int)
    parser.add_argument("--load_epoch", default=0, type=int)
    parser.add_argument("--lr", default=1e-3, type=float)
    parser.add_argument("--batch_size", default=1, type=int)
    parser.add_argument("--num_workers", default=4, type=int)
    parser.add_argument("--reset", action="store_true")

    args = parser.parse_args()
    return args


# 메인 함수
## 이는 모델 학습과 평가 파이프라인을 설정하고 실행
def main(args):
    ## 로그 및 체크포인트 디렉토리 설정
    log_path = os.path.join(args.loss_dir, args.mode, args.name)
    check_path = os.path.join(args.output_dir, args.mode, args.name)
    ## TensorBoard 로그를 기록하기 위해 사용
    writer = SummaryWriter(log_path)
    ## mkdir 함수는 해당 경로가 존재하지 않으면 디렉토리를 생성
    mkdir(log_path)
    mkdir(check_path)
    ## Make the directories for save
    
    # 모델 설정
    ## 모델 resnet50을 불러옴
    model = models.resnet50(weights=ResNet50_Weights.DEFAULT)

    ## 각 이미지 영역의 클래스 수를 정의
    model_num_class = (
        ## args.mode가 'class'이면 분류를 위해 클래스 수를 설정하고
        [np.nan, 15, 7, 7, 0, 12, 0, 5, 7]
        if args.mode == "class"
        ## 'regression'이면 회귀를 위해 설정
        else [1, 2, np.nan, 1, 0, 3, 0, np.nan, 2]
    )

    ## args.best_loss는 각 모델의 최적 손실값을 무한대로 초기화
    args.best_loss = [np.inf for _ in range(len(model_num_class))]
    
    ## model_list는 각 이미지 영역에 대해 복사된 모델 리스트
    ## 총 9개의 모델이 생성 # 각 영역에 9개의 resnet 모델을 정의
    model_list = [copy.deepcopy(model) for _ in range(len(model_num_class))]
    
    ## 모델을 로드할 때 사용할 인덱스를 저장
    ## 각 모델의 출력층을 해당 이미지 영역의 클래스 수에 맞게 조정
    resume_list = list()    
    for idx, item in enumerate(model_num_class):
        if not np.isnan(item):
            model_list[idx].fc = nn.Linear(
                model_list[idx].fc.in_features, model_num_class[idx]
            )
            resume_list.append(idx)
    ## 각 모델의 출력층(fc)을 해당하는 영역 클래스 수(model_num_class[idx])에 맞게 조정
    ## 출력층을 조정한 모델의 인덱스를 resume_list에 추가
    ## Adjust the number of output in model for each region image
    ## 각 모델의 출력층을 해당 이미지 영역의 클래스 수에 맞게 조정


    # 체크포인트 로드 및 초기화 
    ## model_dict_path는 체크포인트 파일의 경로를 설정
    model_dict_path = os.path.join(check_path, "1", "state_dict.bin")

    ## args.reset이 참이면 체크포인트 디렉토리를 초기화
    if args.reset:
        print(f"\033[90mReseting......{model_dict_path}\033[0m")
        if os.path.isdir(check_path):
            shutil.rmtree(check_path)
            mkdir(check_path)
    ## If there is check-point, load that

    if os.path.isfile(model_dict_path):
        print(f"\033[92mResuming......{model_dict_path}\033[0m")

        for idx in resume_list:
            if idx in [4, 6]:
                continue
            model_list[idx] = resume_checkpoint(
                args,
                model_list[idx],
                os.path.join(check_path, f"{idx}", "state_dict.bin"),
            )

    # 로깅 설정 및 데이터셋 로드
    ## setup_logger를 통해 로거를 설정하고, 인자를 기록
    logger = setup_logger(args.name, args.mode)
    logger.info(args)

    ## customDataset 클래스를 사용하여 데이터셋을 로드
    dataset = CustomDataset(args)

    ##load_dataset 메소드를 호출하여 학습데이터셋을 로드
    dataset.load_dataset(args, "train")
    trainset_loader = data.DataLoader(  # DataLoader를 사용하여 데이터 로더 설정
        dataset=dataset,
        batch_size=args.batch_size,
        num_workers=args.num_workers,
        shuffle=True,
    ) 
    
    ## load_dataset 메소드를 호출하여 검증데이터셋을 로드
    dataset.load_dataset(args, "val")
    valset_loader = data.DataLoader(   # DataLoader를 사용하여 데이터 로더 설정
        dataset=dataset,
        batch_size=args.batch_size,
        num_workers=args.num_workers,
        shuffle=False,
    ) 
    
    # 모델 학습 및 평가
    
    ## Mode 클래스를 초기화
    resnet_model = Model(
        args, model_list, trainset_loader, valset_loader, logger, writer
    )

    for epoch in range(args.load_epoch, args.epoch):
        resnet_model.update_e(epoch + 1) if args.load_epoch else None

        for model_idx in range(len(model_num_class)):
            if np.isnan(model_num_class[model_idx]):
                continue
            # In regression task, there are no images for 미간, 입술, 턱
            resnet_model.choice(model_idx)
            # Change the model for each region
            resnet_model.run(phase="train")
            resnet_model.run(phase="valid")
            
        resnet_model.update_m(model_num_class)

        # Show the result for each value, such as pigmentation and pore, by averaging all of them
        resnet_model.update_e(epoch + 1)
        resnet_model.reset_log(mode=args.mode)

        if resnet_model.stop_early():
            break
        
    writer.close()
# Model 클래스를 초기화합니다.
# 각 에포크에 대해 학습 및 검증을 수행합니다.
# update_e를 통해 현재 에포크를 업데이트합니다.
# 각 모델 인덱스에 대해 모델을 선택하고(choice), 학습(run(phase="train"))과 검증(run(phase="valid"))을 수행합니다.
# update_m을 통해 모델 성능을 업데이트합니다.
# reset_log를 통해 로그를 초기화합니다.
# 조기 종료 조건(stop_early())이 만족되면 학습을 중단합니다.
# TensorBoard 로그 기록을 종료합니다.
    


if __name__ == "__main__":
    args = parse_args()
    main(args)