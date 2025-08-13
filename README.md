# Anime Finder 🎥

## アプリ概要
ユーザーがアニメタイトルを入力すると、Jikan APIを利用して関連アニメ情報（タイトル・放送年・あらすじ・画像）を取得し、Streamlitで表示するアプリです。

## 使用API
- [Jikan API](https://docs.api.jikan.moe/)

## システム設計図
![システム設計図](system_design.png)

## コード説明図
![コード説明図](code_diagram.png)

## 利用方法
```bash
pip install -r requirements.txt
streamlit run app.py
