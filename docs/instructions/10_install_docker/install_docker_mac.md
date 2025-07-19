# Docker Desktop セットアップ - Mac 編

この手順では macOS 環境下における`Docker Desktop`のインストール手順を説明しています。

## Docker Desktop インストール
1. 自身の Mac に搭載されている CPU を確認し、[Install Docker Desktop on Mac](https://docs.docker.com/desktop/install/mac-install/) から Docker Desktop をダウンロードし、インストールします。
    ![Docker Desktopをインストール](../../images/install-docker-desktop.gif)
2. Docker Desktop をインストールした後、一度 PC を再起動してから Docker Desktop を起動してください。
3. これにより、Docker が正しく動作するか確認できます。

## Docker　実行環境の準備
Docker をインストールしたら、続いて今回の Railway で利用する Docker 環境のセットアップを行います。

Docker では実行環境としてコンテナというものを用意します。

以下の手順にて、今回の Railway で使用する Docker コンテナを作成 ( コンテナをビルド ) します。

1. VSCode にて、今回の Railway で使用する Clone 済みのテンプレートリポジトリのフォルダを開く。
2. VSCode の拡張機能で Docker をインストールする。
3. VSCode からターミナルを起動しアプリケーション実行環境を構築する。
    1. 左上のターミナル -> 新しいターミナルを選択して、ターミナルを起動します。
    2. 以下のコマンドを実行し、アプリケーションの環境固有 ( データベースへの接続情報等 ) の設定や機密情報を格納する`.env`ファイルを作成します。
    ```bash
    cp .env.sample .env
    ```
    この `.env` ファイルは、今回のプロジェクトではDockerでコンテナを立ち上げる際に自動的に参照されます。
    今回はデータベース環境向けの環境変数を `.env` に設定していますので、正常に作成されていない場合、開発を進める中でデータベースに正常に接続できない等の問題が発生しますのでご注意ください。
    3. 以下のコマンドを実行し、Docker コンテナのビルドを行います。
    ```bash
    docker compose build --no-cache
    ```
   ※ Docker コンテナのビルドおよび起動には時間がかかる場合があります。コマンドが正常に完了するまで待ってください。
