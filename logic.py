import requests

def search_anime(query, limit=5):
    """
    指定されたアニメタイトルでJikan APIを使って検索
    :param query: 検索キーワード
    :param limit: 取得件数
    :return: 検索結果のリスト（タイトル、年、画像、あらすじ）
    """
    if not query:
        return {"error": "検索ワードを入力してください"}

    url = f"https://api.jikan.moe/v4/anime?q={query}&limit={limit}"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return {"error": f"APIリクエストに失敗しました: {e}"}
    
    data = response.json().get("data", [])
    if not data:
        return {"error": "該当するアニメが見つかりませんでした"}
    
    results = []
    for anime in data:
        results.append({
            "title": anime.get("title", "タイトル不明"),
            "year": anime.get("year", "不明"),
            "image": anime.get("images", {}).get("jpg", {}).get("image_url"),
            "synopsis": anime.get("synopsis", "あらすじ情報はありません。")
        })
    return results
