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
    endpoint="/addmessage"
    summary="メッセージの追加"
    description="""メッセージの追加"""

class DelMessage:
    endpoint="/delmessage"
    summary="メッセージの削除"
    description="""メッセージの削除"""
