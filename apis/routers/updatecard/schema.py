from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class TokenData(BaseModel):
    uid: str = Field(
        ..., title="デコードされたtoken", description="cookieから取得したtoken一式"
    )


# カードテーブルの要素のうち以下をフロントから受け取る（addの場合と同じもの）
class Request(BaseModel):
    card_id: str = Field(..., title="カードid", description="カードのID(ハッシュ値)")
    card_pos: int = Field(
        ..., title="カードの位置", description="カテゴリ内でのカードの位置を示す番号"
    )
    col_id: str = Field(
        ..., title="カテゴリid", description="カテゴリのID(ハッシュ値)"
    )  # 不要？？
    card_name: str = Field(..., title="カード名", description="カードの名前(タスク名)")
    input_date: date = Field(..., title="作成日", description="カードの作成日")
    due_date: date = Field(..., title="期限", description="タスクの期限")
    color: str = Field(..., title="色id", description="色のid")
    description: str = Field(None, title="カードの説明", description="カードの説明")


RequestExample = {
    "card_id": "card-b2c04f39-66d7-4eaf-af36-d52a234",  # card_idの更新は想定しない
    "card_pos": 1,
    "col_id": "category-734c5844-7cba-4c51-8d0c-983",  # col_idの更新は想定しない
    "card_name": "中間発表資料を作成する",
    "input_date": "2024-02-01",
    "due_date": "2024-02-25",
    "color": "#e9c77b",
    "description": "Canvaで編集する",
}


# 更新後のカード情報をそのまま返す
class Data(BaseModel):
    card_id: str = Field(..., title="カードid", description="カードのID(ハッシュ値)")
    card_pos: int = Field(
        ..., title="カードの位置", description="カテゴリ内でのカードの位置を示す番号"
    )
    col_id: str = Field(..., title="カテゴリid", description="カテゴリのID(ハッシュ値)")
    # uid: str = Field(..., title="ユーザーid", description="カードの作成者のID")
    card_name: str = Field(..., title="カード名", description="カードの名前(タスク名)")
    input_date: date = Field(..., title="作成日", description="カードの作成日")
    due_date: date = Field(..., title="期限", description="タスクの期限")
    color: str = Field(..., title="色id", description="色のid")
    description: str = Field(None, title="カードの説明", description="カードの説明")


class Response(BaseModel):
    status: int = Field(
        ...,
        title="ステータス",
        description="正しい場合1、不正の場合0",
    )
    data: Optional[Data] = Field(None, title="更新したカードの情報")


# 必要に応じて後で作成
ResponseExamples = {}
