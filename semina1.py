import streamlit as st
import pandas as pd

tab1, tab2, tab3 = st.tabs(["semina1", "semina2", "semian3"])

with tab1:
    # 세션 상태에 semina_df가 없는 경우에만 데이터 로드 및 저장
    x = st.slider("X 값을 선택", 0, 100, 50)
    st.write(f"선택한 값: {x}")

    semina_df = pd.read_csv("joojong.csv")
    semina_df.set_index("연도", inplace=True)
    st.line_chart(semina_df)

with tab2:
# 저장된 데이터 사용하기
    if 'count' not in st.session_state:
        st.session_state.count = 0  # 초기화

    if st.button("카운트 증가", key="button1"):
        st.session_state.count += 1

    st.write(f"현재 카운트: {st.session_state.count}")

with tab3:
    count = 0
    if st.button("카운트 증가", key="button2"):
        count += 1

    st.write(f"현재 카운트: {count}")

