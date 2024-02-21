from sqlalchemy import and_
from fastapi import status, HTTPException
from pydantic import BaseModel
from .schema import Response, TokenData, Data
from apis.services.authfunctions import database
from apis.bases.card import Card
from apis.bases.category import Category
from sqlalchemy import select

class Model(BaseModel):
    async def exec(self, token: TokenData) -> Response:
        # loginしていない場合、拒否する。
        if not token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
            )

        # Category と Card テーブルを結合し、ログイン中のユーザーが作成したものだけ選択する
        query = select([Card.__table__, Category.__table__]).select_from(
        Card.__table__.join(Category.__table__, Card.__table__.c.col_id == Category.__table__.c.col_id)
        ).where(Card.uid == token.uid)
        
        result = await database.fetch_all(query)

        arry = []  # dataリストを初期化
        for view in result:
            dt = Data(
                col_id = view.col_id,
                col_pos = view.col_pos,
                col_name = view.col_name,
                card_id=view.card_id,
                card_pos = view.card_pos,
                card_name = view.card_name,
                color = view.color,
                input_date = view.input_date,
                due_date = view.due_date,
                description = view.description #categoryテーブルにもdescriptionは存在しているが、これでcardの方のdescriptionが取得されるのでいったんOK
            )
            arry.append(dt)
        return Response(status=1, data=arry)
