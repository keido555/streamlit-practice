# from turtle import left, right
# from click import option
import streamlit as st
import time

# from matplotlib.pyplot import axis
# from PIL import Image

st.title('Streamlit 超入門')

st.write('ブログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.05)
'Done'


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに表示')
if button:
    right_column.write('ボタンが押されました')

expander1 = st.expander('Q1')
expander1.write('A1')
expander1 = st.expander('Q2')
expander1.write('A2')

# text = st.text_input('あなたの趣味を教えてください')
# 'あなたの好きな趣味は、', text, 'ですね。'

# condition = st.slider('あなたの調子は？', 0, 100, 50)
# 'コンディション：', condition

# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1, 11))
# )

# 'あなたの好きな数字は、', option, 'ですね。'

# if st.checkbox('show Image'):
#     img = Image.open('img.jpeg')
#     st.image(img, caption='Miku Hatsune', use_column_width=True)

# st.write('DataFrame')

# df = pd.DataFrame(
#     np.random.rand(30, 3),
#     columns=['a', 'b', 'c']
# )
# df
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )
# st.map(df)