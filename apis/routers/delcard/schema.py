from pydantic import BaseModel, Field
from typing import Optional


class TokenData(BaseModel):
    data: str = Field(
        ..., title="デコードされたtoken", description="cookieから取得したtoken一式"
    )


class Request(BaseModel):
    card_id: str = Field(..., title="カードid", description="カードのID(ハッシュ値)")


RequestExample = {"card_id": "card-05236ffd-eefd-42b1-a895-b474c24"}


class Data(BaseModel):
    card_id: str = Field(..., title="カードid", description="カードのID(ハッシュ値)")
    card_name: str = Field(..., title="カード名", description="カードの名前(タスク名)")


class Response(BaseModel):
    status: int = Field(
        ...,
        title="ステータス",
        description="正しい場合1、不正の場合0",
    )
    data: Optional[Data] = Field(None, title="削除したカードの情報")


# 必要に応じて後で作成
ResponseExamples = {}
