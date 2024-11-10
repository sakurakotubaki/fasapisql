DockerfileだけでMySQLを使用する場合の最小構成と、必要なコマンドを説明します。

```docker
# Dockerfile
FROM mysql:8.0

# 文字コードの設定
ENV LANG="ja_JP.UTF-8"
ENV LC_ALL="ja_JP.UTF-8"
ENV LANGUAGE="ja_JP.UTF-8"

# タイムゾーンの設定
ENV TZ="Asia/Tokyo"

# MySQLの環境変数設定
ENV MYSQL_USER=jboy
ENV MYSQL_PASSWORD=1234qw
ENV MYSQL_ROOT_PASSWORD=root1234
ENV MYSQL_DATABASE=myapp

```

### 基本コマンド

1. **ビルドコマンド**
```bash
# イメージのビルド
docker build -t mysql-custom .
```

2. **起動コマンド**
```bash
# コンテナの起動
docker run -d -p 3306:3306 --name mysql-container mysql-custom
```

3. **停止コマンド**
```bash
# コンテナの停止
docker stop mysql-container
```

### その他の便利なコマンド
```bash
# コンテナの削除（停止後に実行）
docker rm mysql-container

# コンテナの状態確認
docker ps

# コンテナのログ確認
docker logs mysql-container
```

これだけで基本的なMySQL環境が構築できます。シンプルで必要最小限の設定となっています。

# 既存のコンテナを停止・削除（必要な場合）
docker stop mysql-container
docker rm mysql-container

# イメージの再ビルド
docker build -t mysql-custom .

# 新しい設定でコンテナを起動
docker run -d -p 3306:3306 --name mysql-container mysql-custom

ホスト: localhost
ポート: 3306
データベース: myapp
ユーザー名: jboy
パスワード: 1234qw