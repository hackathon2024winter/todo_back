## alembic

- alembic は declarative_base を継承するクラスをマイグレーションして env.py で指定したデータベースにテーブルを自動生成する。マイグレーションとは Python ファイルを設計図とし、データベースのテーブルを作成することを言う。データベースをゼロから作るのであれば、build.sh に一連の手続きを記載しているので、コンテナ消去・再生成で自動的にマイグレーションされる。
- 手動でテーブルを再構成する場合、以下の手順で進める。
  1.FastAPI のある devcontainer に入り、alembic.ini を右クリック →Open in Integrated Terminal

  2.server/models/\_\_init\_\_.py に MySQL のテーブルを作りたい class を import で記載することを忘れにない。ファイルを server/models フォルダに置くだけでは無意味。

  3.以下コマンドを実行しマイグレーションファイルを生成。messege に何をするのかを記入。"Add column hoge"など。
  ~/devcon$ alembic revision --autogenerate -m "message"

  4./alembic/versions にあるマイグレーションファイルは upgrade と downgrade のペアになっており、upgrade は message に見合う内容を自作する。データを残しながらテーブル構造を変更するには、カラムの nullable=True を設定して値を追加更新するなど、Python でのテーブル操作を熟知しておく必要がある。downgrade は upgrade をキャンセルする内容にする。

  5.以下コマンドを実行しマイグレーションファイルを適用する。
  ~/devcon$ alembic upgrade head

  6.面倒なら devcontainer から抜け、./docker_softclear.sh を実行してコンテナを完全削除し、server/models フォルダを更新して改めて docker-compose.yml を右クリック compose up で再構築すると良い。

- dumpDB.sh で MySQL をバックアップし、restoreDB.sh で元に戻す。ただしテーブル構成が変わっていない事が条件。backup.sql を手動で修正すれば、不可能ではない。

## docker コンテナ

- docker-compose.yml の上にマウスカーソルを持っていき、右クリック → Compose Up で全てのコンテナが起動する。
  - fastapi コンテナ：api を提供する本体
  - mysql_fast コンテナ：データベース
  - pma_fast コンテナ:データベースを閲覧するツール
- http://localhost:8080/docs にブラウザでアクセスすると FastAPI を動作させる GUI (Swagger UI)が起動する。
- http://localhost:4081 にブラウザでアクセスするとデータベースの中を閲覧できる。

## dev container

- クジラのアイコンから 動作中の docker コンテナ(緑の三角マーク)を右クリック →Attach Shell を実行すると、CLI でコンテナ内に入ることができる。dev container は CLI ではなく VSCode の GUI でコンテナ内に入るツール。
- python コンテナであれば requirements.txt、nodejs コンテナ(React、NextJS など)であれば package.json に導入するライブラリとバージョンが明記されるので、均質な開発環境を共有できる。
- 入れるコンテナは.devcontainer フォルダの devcontainer.json の service で決定され、この service は docker-compose.yml の service が選択される。このプロジェクトの場合、fastapi コンテナに入れる。
- 左下の><を左クリック →Reopen in Container で dev container に入れる。
- 左下>< Dev Containerを左クリック→ Reopen Folder Locallyでdev container から出られる。