from pydantic import BaseModel, Field
from typing import Optional


class TokenData(BaseModel):
    data: str = Field(
        ..., title="デコードされたtoken", description="cookieから取得したtoken一式"
    )


class Request(BaseModel):
    col_id: str = Field(..., title="カテゴリid", description="カテゴリのID(ハッシュ値)")


# fugaさんの「完了」カテゴリを削除
RequestExample = {"col_id": "category-7414208f-560c-4641-8d08-f7e"}


class Data(BaseModel):
    col_id: str = Field(..., title="カテゴリid", description="カテゴリのID(ハッシュ値)")
    col_name: str = Field(
        ..., title="カテゴリ名", description="カテゴリの名前(タスク名)"
    )


class Response(BaseModel):
    status: int = Field(
        ...,
        title="ステータス",
        description="正しい場合1、不正の場合0",
    )
    data: Optional[Data] = Field(None, title="削除したカテゴリの情報")
    message: str = Field(..., title="挙動の説明")


# 必要に応じて後で作成
ResponseExamples = {}
