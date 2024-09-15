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
#Q_町会マスタ_総合順位_繰上
url1='https://drive.google.com/uc?id=1Y7mPE4ikULQVi6T6TGDYlhz1nT2r-hXM'
#Q_町会マスタ_総合順位_繰上
url2='https://drive.google.com/uc?id=1Sh8YcsmhfBTrWYgx-fz9E7Nb52e83LAg'
try:
    #encodingやon_bad_lines='skip'を使用して不正な行をスキップ
    df1 = pd.read_csv(url1, on_bad_lines='skip', encoding='utf-8')
    df2 = pd.read_csv(url2, on_bad_lines='skip', encoding='utf-8')
 
    # 表形式で表示
    st.write(df1)
    st.write(df2)
except pd.errors.ParserError as e:
    st.error(f"CSVファイルの読み込みに失敗しました: {e}")
