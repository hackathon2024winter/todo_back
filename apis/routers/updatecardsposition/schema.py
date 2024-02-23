from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date


class TokenData(BaseModel):
    uid: str = Field(..., title="デコードされたtoken", description="cookieから取得したtoken一式")


#カードテーブルの要素のうち以下をフロントから受け取る
class CardData(BaseModel):
    card_id: str = Field(..., title="カードid", description="カードのID(ハッシュ値)")
    card_pos: int = Field(..., title="カードの位置", description="カテゴリ内でのカードの位置を示す番号")
    col_id: str = Field(..., title="カテゴリid", description="カテゴリのID(ハッシュ値)") 

class Request(BaseModel):
    cards: List[CardData] = Field(..., title="カード情報リスト")

#fugaさんの各カードの情報を受け取り更新。「中間発表資料の作成」カードを「未着手」→「完了」にD&Dした想定。
RequestExample = {
    "cards": [
        {
            "card_id": "61eae2b5-d109-a5e3-7a38-01970911cd12",
            "card_pos": 2,
            "col_id": "7d2fc6b5-58be-6257-2b40-b0b848062c07"
        },
        {
            "card_id": "61eae2b5-d109-a5e3-7a38-01970911cd14",
            "card_pos": 1,
            "col_id": "7d2fc6b5-58be-6257-2b40-b0b848062c07"
        },
        {
            "card_id": "61eae2b5-d109-a5e3-7a38-01970911cd15",
            "card_pos": 1,
            "col_id": "7d2fc6b5-58be-6257-2b40-b0b848062b07"
        }
    ]
}

class Response(BaseModel):
    status: int = Field(
        ...,
        title="ステータス",
        description="正しい場合1、不正の場合0",
    )
    message: str = Field(..., title="更新した旨のメッセージ")


#必要に応じて後で作成
ResponseExamples = {}
