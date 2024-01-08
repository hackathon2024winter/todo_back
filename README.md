## alembic

- alembic は declarative_base を継承するクラスをマイグレーションして env.py で指定したデータベースにテーブルを自動生成する。データベースをゼロから作るのであれば、build.sh に一連の手続きを記載しているので、コンテナ消去・再生成で自動的にマイグレーションされる。
- 手動でテーブルを再構成する場合、以下の手順で進める。
  1.FastAPI のある devcontainer に入り、alembic.ini を右クリック →Open in Integrated Terminal

  2.server/models/\_\_init\_\_.py に MySQL のテーブルを作りたい class を import で記載することを忘れにない。ファイルを server/models フォルダに置くだけでは無意味。

  3.以下コマンドを実行しマイグレーションファイルを生成。messege に何をするのかを記入。"Add column hoge"など。
  ~/devcon$ alembic revision --autogenerate -m "message"

  4./alembic/versions にあるマイグレーションファイルは upgrade と downgrade のペアになっており、upgrade は message に見合う内容を自作する。データを残しながらテーブル構造を変更するには、カラムの nullable=True を設定して値を追加更新するなど、Python でのテーブル操作を熟知しておく必要がある。downgrade は upgrade をキャンセルする内容にする。

  5.以下コマンドを実行しマイグレーションファイルを適用する。
  ~/devcon$ alembic upgrade head

  6.面倒なら devcontainer から抜け、./docker_softclear.sh を実行してコンテナを完全削除し、server/models フォルダを更新して改めて docker-compose.yml を右クリック compose up で再構築すると良い。

- dumpDB.sh で MySQL をバックアップし、それを戻すと途中の migration が消え、dumpDB の状態に戻ってしまう。
