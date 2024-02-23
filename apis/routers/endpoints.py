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
    description = """カードの取得"""


class GetCategories:
    endpoint = "/getcategories"
    summary = "カテゴリの取得"
    description = """カテゴリの取得"""


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
    description = """ボード画面に表示するカードの情報取得"""
    
class UpdateCard:
    endpoint = "/updatecard"
    summary = "カード情報の更新"
    description = """カード情報の更新"""
    
class GetBoardDetail:
    endpoint = "/getboarddetail"
    summary = "ボード画面に表示するカード情報(詳細含む)の取得"
    description = """ボード画面に表示するカード情報(詳細含む)の取得"""
    
class DelCard:
    endpoint = "/delcard"
    summary = "カードの削除"
    description = """カードの削除"""