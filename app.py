import streamlit as st
import pandas as pd

# タイトルとサブタイトル
st.title("菊川町スポーツ大会 2024")
st.subheader("Run for everyone!")

# 背景色を若葉色に設定するためのカスタムCSS
st.markdown(
    """
    <style>
    /* ページ全体の背景色を若葉色に設定 */
    body {
        background-color: #7FFF00;
    }

    /* メインコンテンツの背景も変更 */
    .stApp {
        background-color: #7FFF00;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Google Driveの共有リンクからファイルを読み込む
#url = 'https://drive.google.com/uc?id=ファイルID'
#url="https://drive.google.com/file/d/1Y7mPE4ikULQVi6T6TGDYlhz1nT2r-hXM/view?usp=sharing"
url='https://drive.google.com/uc?id=1Y7mPE4ikULQVi6T6TGDYlhz1nT2r-hXM'

try:
    #encodingやon_bad_lines='skip'を使用して不正な行をスキップ
    df = pd.read_csv(url, on_bad_lines='skip', encoding='utf-8')
    # 表形式で表示
    st.write(df)
except pd.errors.ParserError as e:
    st.error(f"CSVファイルの読み込みに失敗しました: {e}")
