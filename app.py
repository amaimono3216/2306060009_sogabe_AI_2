import streamlit as st
from logic import search_anime

# ページ設定
st.set_page_config(page_title="Anime Finder", page_icon="🎥", layout="wide")

# タイトル
st.title("🎥 Anime Finder")
st.write("アニメタイトルを入力して情報を検索できます（Jikan API 使用）")

# 入力フォーム
query = st.text_input("アニメタイトルを入力", "")

# 検索実行
if query:
    results = search_anime(query)
    if "error" in results:
        st.error(results["error"])
    else:
        for anime in results:
            with st.expander(f"{anime['title']} ({anime['year']})"):
                if anime["image"]:
                    st.image(anime["image"], width=200)
                st.write(anime["synopsis"])
