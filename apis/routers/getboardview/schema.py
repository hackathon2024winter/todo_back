from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date


class TokenData(BaseModel):
    uid: str = Field(..., title="デコードされたtoken", description="cookieから取得したtoken一式")

class Data(BaseModel):
    col_id: str = Field(..., title="カテゴリid", description="カテゴリのID(ハッシュ値)")
    col_pos: int = Field(..., title="カテゴリの位置", description="カテゴリの位置を示す番号")
    col_name: str = Field(..., title="カテゴリ名", description="カテゴリの名前(未着手／完了などのステータス名)")
    card_id: str = Field(..., title="カードid", description="カードのID(ハッシュ値)")
    card_pos: int = Field(..., title="カードの位置", description="カテゴリ内でのカードの位置を示す番号")
    card_name: str = Field(..., title="カード名", description="カードの名前(タスク名)")
    color: str = Field(..., title="色id", description="色のid")

class Response(BaseModel):
    status: int = Field(
        ...,
        title="ステータス",
        description="正しい場合1、不正の場合0",
    )
    data: Optional[List[Data]] = Field(
        None, title="カード情報リスト"
    )


#あとで必要に応じて作成
ResponseExamples = {}
