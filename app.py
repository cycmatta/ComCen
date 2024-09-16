import streamlit as st
import pandas as pd

# タイトルとサブタイトル
st.title("きくがわスポーツ大会 2024")
st.subheader("みんなの声に力がわいてくる！")

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
#Q_大会記録のクロス集計
url1='https://drive.google.com/uc?id=1Y7mPE4ikULQVi6T6TGDYlhz1nT2r-hXM'
#Q_町会マスタ_総合順位_繰上
url2='https://drive.google.com/uc?id=1Sh8YcsmhfBTrWYgx-fz9E7Nb52e83LAg'
try:
    #encodingやon_bad_lines='skip'を使用して不正な行をスキップ
    df1 = pd.read_csv(url1, on_bad_lines='skip', encoding='utf-8')
    df2 = pd.read_csv(url2, on_bad_lines='skip', encoding='utf-8')
 
    # df2の最新の更新日時を取得(更新日時を日付型に変換、最大値を取得、最大値を表示)
    df2['更新日時']=pd.to_datetime(df2['更新日時'])
    max_date=df2['更新日時'].max()
    #25pxで、st.write(f"最新更新日時: {max_date}")
    st.markdown(f"<p style='font-size:25px;'>最新更新日時: {max_date}</p>", unsafe_allow_html=True)
    
    # 表示する列の順番を指定
    columns_order = ['総合順位', '町会NO', '町会', '繰越点','得点合計','総合計']  # 順番を指定

    # 表形式で表示
    st.write(df1)
    st.write(df2)

    # インデックスをリセットし、None/NaNを空文字に置き換え
    #df1_clean = df1.fillna("").reset_index(drop=True)
    #df2_clean = df2.fillna("").reset_index(drop=True)

    # インデックスを非表示にして表形式で表示(クロス集計は整数で表示)
    #st.table(df1_clean.style.hide(axis='index').format(precision=0))
    #st.table(df2_clean.style.hide(axis='index'))

except pd.errors.ParserError as e:
    st.error(f"CSVファイルの読み込みに失敗しました: {e}")
