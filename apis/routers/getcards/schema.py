from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date


class TokenData(BaseModel):
    uid: str = Field(
        ..., title="デコードされたtoken", description="cookieから取得したtoken一式"
    )


class Data(BaseModel):
    card_id: str = Field(..., title="カードid", description="カードのID(ハッシュ値)")
    card_pos: int = Field(
        ..., title="カードの位置", description="カテゴリ内でのカードの位置を示す番号"
    )
    col_id: str = Field(..., title="カテゴリid", description="カテゴリのID(ハッシュ値)")
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
    data: Optional[List[Data]] = Field(None, title="カード情報リスト")


# あとで必要に応じて作成
ResponseExamples = {}
