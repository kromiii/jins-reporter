import urllib.request
from oauthlib.oauth2 import WebApplicationClient
import webbrowser
import os

#JINS MEME API 固有値
token_url = 'https://apis.jins.com/meme/v1/oauth/token'
auth_url = 'https://accounts.jins.com/jp/ja/oauth/authorize'
scope = ['official']
state = 'somestate'
service_id = 'meme'

#JINS MEME Developers サイトから取得して以下をセットしてください
client_id = os.environ['JINS_CLIENT_ID']
client_secret = os.environ['JINS_CLIENT_SECRET']
redirect_uri = 'https://localhost:5001/' #ここで使用しているライブラリではhttpsが必須です

#クライアントの作成
oauth = WebApplicationClient(client_id)

#認証リクエストの作成
url, headers, body = oauth.prepare_authorization_request(
    auth_url,
    redirect_url=redirect_uri,
    scope=scope,
    state=state,
    service_id=service_id
)

#認可URLをブラウザで開き、リダイレクトされる
webbrowser.open(url, new=0, autoraise=True)

#リダイレクト先のURL(パラメター全て含め)をPythonのREPLにコピペする
authorization_response = input('Press Enter Browser URL: ')

#tokenのリクエストを作成
url, headers, body = oauth.prepare_token_request(token_url, authorization_response, redirect_uri, client_secret=client_secret)

#tokenリクエストを実行し、成功するとoauthに格納される
req = urllib.request.Request(url, body.encode(), headers=headers)
with urllib.request.urlopen(req) as res:
    oauth.parse_request_body_response(res.read())

# トークンをファイルに保存（３０日間有効）
with open('token.txt', 'w') as f:
    f.write(oauth.access_token)

