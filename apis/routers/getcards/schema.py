from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date


class TokenData(BaseModel):
    data: str = Field(..., title="デコードされたtoken", description="cookieから取得したtoken一式")
#サンプルから変更なし

class Data(BaseModel):
    id: int = Field(..., title="カードid", description="カードのID")
    category_id: int = Field(..., title="カテゴリid", description="カテゴリのid")
    color_id: int = Field(..., title="色id", description="色のid")
    name: str = Field(..., title="カード名", description="カードの名前(タスク名)")
    due_date: date = Field(..., title="期限", description="タスクの期限")
    position: int = Field(..., title="カードの位置", description="カードの位置を示す番号")
    detail: str = Field(None, title="カードの説明", description="掲示板やチャットルームの説明")
#sqlalchemyの定義（card.pyのCardクラス）と平仄をとり定義


class Response(BaseModel):
    status: int = Field(
        ...,
        title="ステータス",
        description="正しい場合1、不正の場合0",
    )
    data: Optional[List[Data]] = Field(
        None, title="カード情報リスト", description="カードid、カテゴリid、色id、カード名、期限、カードの位置、カードの説明"
    )


ResponseExamples = {
    200: {
        "description": "Success results must be list.",
        "content": {
            "application/json": {
                "examples": {
                    "success": {
                        "summary": "クエリリクエスト成功",
                        "value": {
                            "status": 1,
                            "results": [
                                {
                                    "id": 1,
                                    "category_id": 1,
                                    "color_id": 1,
                                    "name": "ハッカソン中間発表資料作成",
                                    "position": 1,
                                    "due_date": "2024-03-01",
                                    "detail": "Canvaを用いて作成する"
                                },
                                {
                                    "id": 2,
                                    "category_id": 1,
                                    "color_id": 1,
                                    "name": "基本情報の過去問を解く",
                                    "position": 2,
                                    "due_date": "2024-04-01",
                                    "detail": "参考書を一通り終わらせる"
                                },
                            ],
                        },
                    },
                    "error": {
                        "summary": "クエリリクエスト失敗",
                        "value": {"status": 0, "results": []},
                    },
                }
            }
        },
    }
}
