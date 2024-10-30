import streamlit as st
import pandas as pd

tab1, tab2, tab3 = st.tabs(["입력위젯 및 출력컴포넌트", "semina2", "semian3"])

with tab1:
    with st.form("입력 위젯"):
        name = st.text_input("이름을 입력하세요")
        age = st.number_input("나이를 입력하세요", min_value=0, max_value=200)
        gender = st.selectbox("성별을 입력하세요", ["남성","여성"])
        score = st.slider("점수를 선택하세요",0,100)
        date = st.date_input("날짜를 선택하세요:")
    with st.form("출력 컴포넌트"):
        st.write("입력한 정보:")
        st.write(f"이름: {name}")
        st.write(f"나이: {age}")
        st.write(f"성별: {gender}")
        st.write(f"점수: {score}")
        st.write(f"날짜: {date}")
with tab2:
    # 세션 상태에 semina_df가 없는 경우에만 데이터 로드 및 저장
    x = st.slider("X 값을 선택", 0, 100, 50)
    st.write(f"선택한 값: {x}")

    semina_df = pd.read_csv("joojong.csv")
    semina_df.set_index("연도", inplace=True)
    st.line_chart(semina_df)

with tab3:
# 저장된 데이터 사용하기
    if 'count' not in st.session_state:
        st.session_state.count = 0  # 초기화

    if st.button("카운트 증가", key="button1"):
        st.session_state.count += 1

    st.write(f"현재 카운트: {st.session_state.count}")

with tab4:
    count = 0
    if st.button("카운트 증가", key="button2"):
            count += 1

    st.write(f"현재 카운트: {count}")

