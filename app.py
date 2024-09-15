import streamlit as st
import pandas as pd

# タイトルとサブタイトル
st.title("菊川町スポーツ大会 2024")
st.subheader("Run for everyone!")

# 背景色を若葉色に設定するためのカスタムCSS
st.markdown(
    
    <style>
    body {
        background-color: #7FFF00;  /* 若葉色のコード (若干明るい黄緑) */
    }
    </style>
    ,
    unsafe_allow_html=True
)


# Google Driveの共有リンクからファイルを読み込む
#url = 'https://drive.google.com/uc?id=ファイルID'
#url="https://drive.google.com/file/d/1Y7mPE4ikULQVi6T6TGDYlhz1nT2r-hXM/view?usp=sharing"
url='https://drive.google.com/uc?id=1Y7mPE4ikULQVi6T6TGDYlhz1nT2r-hXM'

try:
    #encodingやエラーハンドリングを追加
    df = pd.read_csv(url, error_bad_lines=False, warn_bad_lines=True)
    # 表形式で表示
    st.write(df)
except pd.errors.ParserError as e:
    st.error(f"CSVファイルの読み込みに失敗しました: {e}")
    