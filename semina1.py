import streamlit as st
import pandas as pd

# 사이드바에 "자료1"과 "자료2" 버튼 추가 및 클릭 상태를 session_state에 저장
st.sidebar.title("자료 선택")
if "show_tabs" not in st.session_state:
    st.session_state.show_tabs = False  # 초기화

# "자료1" 버튼 클릭 시 상태를 True로 변경
if st.sidebar.button("자료1"):
    st.session_state.show_tabs = True

# "자료2" 버튼 클릭 시 상태를 False로 변경하고, 자료2 내용 표시
if st.sidebar.button("자료2"):
    st.session_state.show_tabs = False

# "자료1"이 선택되었을 때만 모든 탭을 표시
if st.session_state.show_tabs:
    # 자료1의 내용 (기존 탭 코드)
    tab1, tab2, tab3, tab4 = st.tabs(["입력 위젯 및 출력 컴포넌트", "Data Frame 시각화", "session_state 활성", "session_state 비활성화"])

    with tab1:
        st.header("입력 위젯 및 출력 컴포넌트")
        with st.form("입력 위젯"):
            name = st.text_input("이름을 입력하세요")
            age = st.number_input("나이를 입력하세요", min_value=0, max_value=200)
            gender = st.selectbox("성별을 입력하세요", ["남성", "여성"])
            score = st.slider("점수를 선택하세요", 0, 100)
            date = st.date_input("날짜를 선택하세요:")
            submitted = st.form_submit_button("제출")

            if submitted:
                st.write("신상 정보:")
                st.write(f"이름: {name}")
                st.write(f"나이: {age}")
                st.write(f"성별: {gender}")
                st.write(f"점수: {score}")
                st.write(f"날짜: {date}")

    with tab2:
        st.header("Data Frame 시각화")
        semina_df = pd.read_csv("joojong.csv")
        semina_df.set_index("연도", inplace=True)
        st.write("한국건강증진개발원_절주(알코올 생산과 소비)_주요 주류 출고현황(국내분)")
        st.dataframe(semina_df)
        st.line_chart(semina_df)

    with tab3:
        st.header("session_state 활성")
        if 'count' not in st.session_state:
            st.session_state.count = 0

        if st.button("카운트 증가", key="button1"):
            st.session_state.count += 1

        st.write(f"현재 카운트: {st.session_state.count}")

    with tab4:
        st.header("session_state 비활성화")
        count = 0
        if st.button("카운트 증가", key="button2"):
            count += 1

        st.write(f"현재 카운트: {count}")

# "자료2"가 선택되었을 때만 3개의 컬럼 레이아웃 표시
else:
    col1, col2, col3 = st.columns(3)
    semina_df = pd.read_csv("joojong.csv")
    with col1:
        st.header("컬럼 1")
        st.write("여기는 첫 번째 분활 화면 입니다.")
        st.write("한국건강증진개발원_절주(알코올 생산과 소비)_주요 주류 출고현황(국내분)")

    with col2:
        st.header("컬럼 2")
        st.write("여기는 두 번째 분활 화면 입니다")
        st.dataframe(semina_df)

    with col3:
        st.header("컬럼 3")
        st.write("여기는 세 번째 분활 화면 입니다")
        st.line_chart(semina_df)
        st.write("삭제")
    st.write("삭제")