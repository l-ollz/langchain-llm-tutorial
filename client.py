from langserve import RemoteRunnable

# サーバーのエンドポイントを指定してRemoteRunnableを作成
remote_chain = RemoteRunnable("http://localhost:8000/chain/")

# サーバーにリクエストを送信し、応答を取得
response = remote_chain.invoke({"language": "french", "text": "hi"})

# 応答を表示
print(response)
