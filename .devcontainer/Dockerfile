# ベースイメージとしてPythonを使用
FROM mcr.microsoft.com/vscode/devcontainers/python:0-3.9

# Playwrightと必要な依存関係をインストール
RUN pip install playwright \
    && playwright install

# 環境変数の設定
ENV PYTHONUNBUFFERED=1

# ワークディレクトリの設定
WORKDIR /workspace
