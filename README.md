# LangChain と FastAPI を使用した翻訳サービス

このプロジェクトは、LangChain と FastAPI を使用して翻訳サービスを提供するためのものです。以下の手順に従って環境をセットアップし、サービスを動かすことができます。

## 必要なもの

- Docker
- Docker Compose
- LangChain API キー
- GROQ API キー

## セットアップ手順

### 1. .env ファイルの作成

プロジェクトディレクトリに`.env`ファイルを作成し、以下の内容を記述します。

```txt
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=YOUR_API_KEY_HERE
GROQ_API_KEY=YOUR_API_KEY_HERE
```
YOUR_API_KEY_HEREを実際のLangChain APIキーに置き換えてください。

### コンテナのビルドと起動
以下のコマンドでDockerコンテナをビルドし、起動します。

```sh
$ docker-compose up --build
```

サーバーが正常に起動し、http://localhost:8000/chain/playground/ にアクセスできることを確認します。
