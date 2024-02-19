from pydantic import BaseModel, Field
from typing import Optional


class TokenData(BaseModel):
    uid: str = Field(..., title="デコードされたtoken", description="cookieから取得したtoken一式")


#カテゴリテーブルの要素のうち以下をフロントから受け取る（uidはtokenからログイン中のユーザーidを取得）
class Request(BaseModel):
    col_id: str = Field(..., title="カテゴリid", description="カテゴリのID(ハッシュ値)")
    col_pos: int = Field(..., title="カテゴリの位置", description="カテゴリの位置を示す番号")
    col_name: str = Field(..., title="カテゴリ名", description="カテゴリの名前(未着手／完了などのステータス名)")
    description: str = Field(None, title="カテゴリの説明", description="カテゴリの説明")


RequestExample = {}


#作成したカテゴリの情報（カテゴリテーブルの要素の全て）を返す
class Data(BaseModel):
    col_id: str = Field(..., title="カテゴリid", description="カテゴリのID(ハッシュ値)")
    col_pos: int = Field(..., title="カテゴリの位置", description="カテゴリの位置を示す番号")
    uid: str = Field(..., title="ユーザーid", description="カードの作成者のID")
    col_name: str = Field(..., title="カテゴリ名", description="カテゴリの名前(未着手／完了などのステータス名)")
    description: str = Field(None, title="カテゴリの説明", description="カテゴリの説明")


class Response(BaseModel):
    status: int = Field(
        ...,
        title="ステータス",
        description="正しい場合1、不正の場合0",
    )
    data: Optional[Data] = Field(None, title="作成したカテゴリの情報")


#必要に応じて後で作成
ResponseExamples = {}
