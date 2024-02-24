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


class AddChannel:
    endpoint = "/addchannel"
    summary = "掲示板の追加"
    description = """掲示板の追加"""


class AddMessage:
    endpoint = "/addmessage"
    summary = "メッセージの追加"
    description = """メッセージの追加"""


class DelMessage:
    endpoint = "/delmessage"
    summary = "メッセージの削除"
    description = """メッセージの削除"""


class DelChannel:
    endpoint = "/delchannel"
    summary = "掲示板の削除"
    description = """掲示板の削除"""


class GetChannels:
    endpoint = "/getchannels"
    summary = "掲示板の取得"
    description = """掲示板の取得"""


class GetMessages:
    endpoint = "/getmessages"
    summary = "メッセージの取得"
    description = """メッセージの取得"""


class GetCards:
    endpoint = "/getcards"
    summary = "カードの取得"
    description = """DB上のカード情報をすべて取得します。is_user_createdでログイン中のユーザーが作成したものかをbool値で示します"""


class GetCategories:
    endpoint = "/getcategories"
    summary = "カテゴリの取得"
    description = """DB上のカテゴリ情報をすべて取得します。is_user_createdでログイン中のユーザーが作成したものかをbool値で示します"""


class AddCard:
    endpoint = "/addcard"
    summary = "カードの追加"
    description = """カードの追加"""

class AddCategory:
    endpoint = "/addcategory"
    summary = "カテゴリの追加"
    description = """カテゴリの追加"""

class GetBoardView:
    endpoint = "/getboardview"
    summary = "ボード画面に表示するカードの情報取得"
    description = """ログイン中のユーザーが作成したカテゴリとカードの情報を取得します(詳細含む)"""

class UpdateCard:
    endpoint = "/updatecard"
    summary = "カード情報の編集"
    description = """カード編集画面からの編集内容を反映します"""

class GetBoardDetail:
    endpoint = "/getboarddetail"
    summary = "ボード画面に表示するカード情報の取得(詳細含む)"
    description = """ログイン中のユーザーが作成したカテゴリとカードの情報を取得します(詳細含む)"""

class DelCard:
    endpoint = "/delcard"
    summary = "カードの削除"
    description = """カードの削除"""

class UpdateCardsPosition:
    endpoint = "/updatecardsposition"
    summary = "カードの位置情報(card_pos,col_id)の更新"
    description = """ドラッグアンドドロップ等の後の、各カードのcard_posとcol_idを受け取り更新します"""

class DelCategory:
    endpoint = "/delcategory"
    summary = "カテゴリの削除"
    description = """カテゴリを削除します。カテゴリに属するカードがある場合は同時に削除されます。"""