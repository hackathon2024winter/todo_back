from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date


class TokenData(BaseModel):
    uid: str = Field(
        ..., title="デコードされたtoken", description="cookieから取得したtoken一式"
    )


# カードテーブルの要素のうち以下をフロントから受け取る
class CardData(BaseModel):
    card_id: str = Field(..., title="カードid", description="カードのID(ハッシュ値)")
    card_pos: int = Field(
        ..., title="カードの位置", description="カテゴリ内でのカードの位置を示す番号"
    )
    col_id: str = Field(..., title="カテゴリid", description="カテゴリのID(ハッシュ値)")


class Request(BaseModel):
    cards: List[CardData] = Field(..., title="カード情報リスト")


# fugaさんの各カードの情報を受け取り更新。「中間発表資料の作成」カードを「未着手」→「完了」にD&Dした想定。
RequestExample = {
    "cards": [
        {
            "card_id": "card-29207055-e668-40ef-9668-a0a9d35",
            "card_pos": 2,
            "col_id": "category-734c5844-7cba-4c51-8d0c-983",
        },
        {
            "card_id": "card-9c16f9d6-b968-4873-be2e-b307792",
            "card_pos": 1,
            "col_id": "category-734c5844-7cba-4c51-8d0c-983",
        },
        {
            "card_id": "card-017f8b11-4e1e-470d-b8f8-38f35d3",
            "card_pos": 1,
            "col_id": "category-734c5844-7cba-4c51-8d0c-983",
        },
    ]
}


class Response(BaseModel):
    status: int = Field(
        ...,
        title="ステータス",
        description="正しい場合1、不正の場合0",
    )
    message: str = Field(..., title="更新した旨のメッセージ")


# 必要に応じて後で作成
ResponseExamples = {}
