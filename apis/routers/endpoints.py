class Signup:
    endpoint = "/signup"
    summary = "ユーザー登録"
    description = """ユーザーを登録します。"""


class Login:
    endpoint = "/login"
    summary = "ログイン"
    description = """ログイン"""


class Signout:
    endpoint = "/signout"
    summary = "サインアウト"
    description = """サインアウト"""


class GetCards:
    endpoint = "/getcards"
    summary = "カード情報の取得"
    description = """ログイン中のユーザーが作成したカード情報を取得します"""


class AddCard:
    endpoint = "/addcard"
    summary = "カードの追加"
    description = """カードを追加します"""


class UpdateCard:
    endpoint = "/updatecard"
    summary = "カード情報の編集"
    description = """カード情報の編集内容を反映します"""


class DelCard:
    endpoint = "/delcard"
    summary = "カードの削除"
    description = """カードを削除します"""


class GetCategories:
    endpoint = "/getcategories"
    summary = "カテゴリ情報の取得"
    description = """ログイン中のユーザーが作成したカード情報を取得します"""


class AddCategory:
    endpoint = "/addcategory"
    summary = "カテゴリの追加"
    description = """カテゴリを追加します"""


class UpdateCategory:
    endpoint = "/updatecategory"
    summary = "カテゴリ情報の編集"
    description = """カード情報の編集内容を反映します"""


class DelCategory:
    endpoint = "/delcategory"
    summary = "カテゴリの削除"
    description = """カテゴリを削除します。カテゴリに属するカードがある場合は同時に削除されます。"""


class UpdateCardsPosition:
    endpoint = "/updatecardsposition"
    summary = "カードの位置情報(card_pos,col_id)の更新"
    description = """ドラッグアンドドロップ等の後の、各カードのcard_posとcol_idを受け取り更新します"""


# class GetBoardView:
#     endpoint = "/getboardview"
#     summary = "ボード画面に表示するカードの情報取得"
#     description = """ログイン中のユーザーが作成したカテゴリとカードの情報を取得します(詳細含む)"""


# class GetBoardDetail:
#     endpoint = "/getboarddetail"
#     summary = "ボード画面に表示するカード情報の取得(詳細含む)"
#     description = """ログイン中のユーザーが作成したカテゴリとカードの情報を取得します(詳細含む)"""



