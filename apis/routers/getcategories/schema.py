from pydantic import BaseModel, Field
from typing import Optional, List


class TokenData(BaseModel):
    data: str = Field(..., title="デコードされたtoken", description="cookieから取得したtoken一式")

#更新ここから
class Data(BaseModel):
    col_id: str = Field(..., title="カテゴリid", description="カテゴリのID(ハッシュ値)")
    col_pos: int = Field(..., title="カテゴリの位置", description="カテゴリの位置を示す番号")
    col_name: str = Field(..., title="カテゴリ名", description="カテゴリの名前(未着手／完了などのステータス名)")
    description: str = Field(None, title="カードの説明", description="カードの説明")
#更新ここまで

class Response(BaseModel):
    status: int = Field(
        ...,
        title="ステータス",
        description="正しい場合1、不正の場合0",
    )
    data: Optional[List[Data]] = Field(
        None, title="カテゴリ情報リスト"
    )


#swaggerUIのドキュメント生成用：あとで必要に応じて更新
ResponseExamples = {
    # 200: {
    #     "description": "Success results must be list.",
    #     "content": {
    #         "application/json": {
    #             "examples": {
    #                 "success": {
    #                     "summary": "クエリリクエスト成功",
    #                     "value": {
    #                         "status": 1,
    #                         "results": [
    #                             {
    #                                 "id": 1,
    #                                 "category_id": 1,
    #                                 "color_id": 1,
    #                                 "name": "ハッカソン中間発表資料作成",
    #                                 "position": 1,
    #                                 "due_date": "2024-03-01",
    #                                 "detail": "Canvaを用いて作成する"
    #                             },
    #                             {
    #                                 "id": 2,
    #                                 "category_id": 1,
    #                                 "color_id": 1,
    #                                 "name": "基本情報の過去問を解く",
    #                                 "position": 2,
    #                                 "due_date": "2024-04-01",
    #                                 "detail": "参考書を一通り終わらせる"
    #                             },
    #                         ],
    #                     },
    #                 },
    #                 "error": {
    #                     "summary": "クエリリクエスト失敗",
    #                     "value": {"status": 0, "results": []},
    #                 },
    #             }
    #         }
    #     },
    # }
}
