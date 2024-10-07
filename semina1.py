import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# x = st.slider("X의 값 입력", 0,100,30) # 0~ 100의 범의의 slider , 초기값 50
# y = np.sin(x)
#
fig, ax = plt.subplots()
ax.plot([x],[y],marker="o")
st.pyplot(fig)

x = st.slider("X 값을 선택", 0, 100, 50)
st.write(f"선택한 값: {x}")
y = np.sin(x)

semina_df = pd.read_csv("joojong.csv")
semina_df.set_index("연도",inplace=True)
st.line_chart(semina_df)
