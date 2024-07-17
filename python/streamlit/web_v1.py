import streamlit as st
import pandas as pd

# 전체 데이터
all_data = pd.read_csv('./final_data_set_v2.csv', index_col=0)

# 초기 상태 설정
if 'page' not in st.session_state:
    st.session_state.page = 0

def making_pivot(category, types, hashtags):
    tour_hashtag_mapping = {'#분위기': '매력도', '#시설': '편의', '#활동': '매력도', '#접근성': '편의', '#서비스': '만족', '#가격': '만족'}
    food_hashtag_mapping = {'#음식의 맛과 질': '음식의 속성', '#음식의 다양성': '음식의 속성', '#시설 및 환경': '시설 및 분위기',
                            '#분위기': '시설 및 분위기', '#청결도와 위생': '시설 및 분위기', '#접근성': '시설 및 분위기',
                            '#특별한 목적': '시설 및 분위기', '#가격과 가치': '가격 및 가치', '#서비스': '서비스'}
    
    # 해시태그 매핑
    if category == '관광':
        hashtag_mapping = tour_hashtag_mapping
    elif category == '음식':
        hashtag_mapping = food_hashtag_mapping
    
    hashtag_categories = [hashtag_mapping.get(tag, '기타') for tag in hashtags]
    
    # 데이터 필터링
    filtered_data = all_data[(all_data["Category"] == category) & (all_data["type"].isin(types)) & (all_data["Category_Map"].isin(hashtag_categories))]

    if not filtered_data.empty:
        pivot_table = filtered_data.pivot_table(index='Attraction', columns='Category_Map', values='Selected_People', aggfunc='sum', fill_value=0)
        return pivot_table
    else:
        return pd.DataFrame()  # 빈 데이터프레임 반환

def page1():
    st.title("카테고리 선택")
    if st.button("관광"):
        st.session_state.category = '관광'
        st.session_state.page = 1
        st.experimental_rerun()
    if st.button("음식"):
        st.session_state.category = '음식'
        st.session_state.page = 1
        st.experimental_rerun()

def page2():
    st.title("유형 선택")
    category = st.session_state.category
    if category == '관광':
        types = st.multiselect(
            "관광 카테고리에서 선택할 수 있는 유형:",
            ['experience', 'nature', 'theme', 'history', 'shop_etc', 'culture']
        )
    else:
        types = st.multiselect(
            "음식 카테고리에서 선택할 수 있는 유형:",
            ['cafe', 'korean', 'chinese', 'west', 'japanese', 'etc']
        )

    if st.button("다음"):
        if not types:
            st.warning("유형을 하나 이상 선택하세요.")
        else:
            st.session_state.types = types
            st.session_state.page = 2
            st.experimental_rerun()

def page3():
    st.title("해시태그 선택")
    category = st.session_state.category
    if category == '관광':
        hashtags = st.multiselect(
            "관광 카테고리에서 선택할 수 있는 해시태그:",
            ['#분위기', '#시설', '#활동', '#접근성', '#서비스', '#가격']
        )
    else:
        hashtags = st.multiselect(
            "음식 카테고리에서 선택할 수 있는 해시태그:",
            ['#음식의 맛과 질', '#음식의 다양성', '#시설 및 환경', '#분위기', '#청결도와 위생', '#접근성', '#특별한 목적', '#가격과 가치', '#서비스']
        )

    if st.button("다음"):
        if not hashtags:
            st.warning("해시태그를 하나 이상 선택하세요.")
        else:
            st.session_state.hashtags = hashtags
            st.session_state.page = 3
            st.experimental_rerun()

def page4():
    st.title("피벗 테이블")
    category = st.session_state.category
    types = st.session_state.types
    hashtags = st.session_state.hashtags

    pivot_table = making_pivot(category, types, hashtags)
    if not pivot_table.empty:
        st.write("생성된 피벗 테이블:")
        st.dataframe(pivot_table)
    else:
        st.write("선택한 조건에 해당하는 데이터가 없습니다.")

    if st.button("처음으로"):
        st.session_state.page = 0
        st.experimental_rerun()

if __name__ == "__main__":
    if st.session_state.page == 0:
        page1()
    elif st.session_state.page == 1:
        page2()
    elif st.session_state.page == 2:
        page3()
    elif st.session_state.page == 3:
        page4()
