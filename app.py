import streamlit as st
import pandas as pd

# 背景色を若葉色に設定するためのカスタムCSS
st.markdown(
    """
    <style>
    /* 文字の色: 白,ページ全体の背景色を緑色に設定 */
    body {
        color: #FFFFFF;
        background-color: #008000;
    }

    /* メインコンテンツの背景も変更 */
    .stApp {
        color: #FFFFFF;
        background-color: #008000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# タイトルとサブタイトル
st.title("きくがわスポーツ大会 2024")
st.subheader("みんなの声に力がわいてくる！")

# Google Driveの共有リンクからファイルを読み込む
#url = 'https://drive.google.com/uc?id=ファイルID'
#Q_大会記録のクロス集計
url1='https://drive.google.com/uc?id=1kYeIXoe0DC__s9oYqmM16M-YbWU_3W-s'
#Q_町会マスタ_総合順位_繰上
url2='https://drive.google.com/uc?id=1Sh8YcsmhfBTrWYgx-fz9E7Nb52e83LAg'
#Q_大会記録
url3='https://drive.google.com/uc?id=1GsecoyElkljs0pBIqexVJgUVYOKPeBMc'

try:
    #encodingやon_bad_lines='skip'を使用して不正な行をスキップ
    df1 = pd.read_csv(url1, on_bad_lines='skip', encoding='utf-8')
    df2 = pd.read_csv(url2, on_bad_lines='skip', encoding='utf-8')
    df3 = pd.read_csv(url3, on_bad_lines='skip', encoding='utf-8')

    # df2の最新の更新日時を取得(更新日時を日付型に変換、最大値を取得、最大値を表示)
    df2['更新日時']=pd.to_datetime(df2['更新日時'])
    max_date=df2['更新日時'].max()
    #25pxで表示。st.write(f"最新更新日時: {max_date}")
    st.markdown(f"<p style='font-size:25px;'>最新更新日時: {max_date}</p>", unsafe_allow_html=True)
    
    # df2,df3は表示する列の特定と順番を指定
    df_selected2 = df2[['総合順位', '町会NO', '町会', '繰越点', '得点合計', '総合計']]
    df_selected3 = df3[['種目NO', '種目', 'RaceNO', '順位', '町会NO', '町会', '得点']]

    #df_selected3の「種目」の文字列を7文字にカット
    #df_selected3['種目'] = df_selected3['種目'].str[:7]

    # df3はソート指定,全て昇順
    df_sorted3 = df_selected3.sort_values(by=['種目NO', 'RaceNO', '順位'], ascending=[True, True, True])

    # df3を'種目NO', '種目'でグループ化
    df_grouped3 = df_sorted3.groupby(['種目NO', '種目']) 

    #確認用
    #print(df3.columns)

    # タブを作成
    tab1, tab2, tab3 = st.tabs(["総合順位", "クロス集計", "大会記録"])

    # タブごとに表形式で表示
    with tab1:
        st.write("総合順位", use_container_width=True)
        st.dataframe(df_selected2) #列を特定したdf

    with tab2:
        st.write("大会記録のクロス集計", use_container_width=True)
        st.dataframe(df1) #ここはそのまま

    with tab3:
        st.write("大会記録")
        #st.dataframe(df_sorted3, use_container_width=True) #ソート指定したdf
        
        # 各グループごとにデータフレームを表示(インデックス削除)
        for (種目NO, 種目), group in df_grouped3:
            st.write(f"種目NO: {種目NO}  種目名: {種目}")
            st.dataframe(group[['RaceNO', '順位', '町会NO', '町会', '得点']].reset_index(drop=True))

    # インデックスをリセットし、None/NaNを空文字に置き換え(うまく動作しないのでボツ)
    #df1_clean = df1.fillna("").reset_index(drop=True)
    #df2_clean = df2.fillna("").reset_index(drop=True)

    # インデックスを非表示にして表形式で表示(クロス集計は整数で表示)(うまく動作しないのでボツ)
    #st.table(df1_clean.style.hide(axis='index').format(precision=0))
    #st.table(df2_clean.style.hide(axis='index'))

except pd.errors.ParserError as e:
    st.error(f"CSVファイルの読み込みに失敗しました: {e}")
