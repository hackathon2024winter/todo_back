from pydantic import BaseModel, Field
from typing import Optional, List


class TokenData(BaseModel):
    uid: str = Field(..., title="デコードされたtoken", description="cookieから取得したtoken一式")

class Data(BaseModel):
    isUserCreated: bool = Field(..., title="カテゴリの作成者か", description="カテゴリの作成者かどうかの判定")
    col_id: str = Field(..., title="カテゴリid", description="カテゴリのID(ハッシュ値)")
    col_pos: int = Field(..., title="カテゴリの位置", description="カテゴリの位置を示す番号")
    col_name: str = Field(..., title="カテゴリ名", description="カテゴリの名前(未着手／完了などのステータス名)")
    description: str = Field(None, title="カテゴリの説明", description="カテゴリの説明")

class Response(BaseModel):
    status: int = Field(
        ...,
        title="ステータス",
        description="正しい場合1、不正の場合0",
    )
    data: Optional[List[Data]] = Field(
        None, title="カテゴリ情報リスト"
    )


#swaggerUIのドキュメント生成用：あとで必要に応じて作成
ResponseExamples = {}
