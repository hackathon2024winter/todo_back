from fastapi import status, HTTPException
from pydantic import BaseModel
from .schema import Request, Response, TokenData, Data
from apis.services.authfunctions import database
from apis.bases.card import Card    


class Model(BaseModel):
    async def exec(self, body: Request, token: TokenData) -> Response:
        # loginしていない場合、拒否する。
        if not token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
            )

        # Cardテーブルに挿入するクエリ作成
        query = Card.__table__.insert().values(
            card_id=body.card_id,
            card_pos=body.card_pos,
            col_id=body.col_id,
            uid=token.uid,
            card_name=body.card_name,
            input_date=body.input_date,
            due_date=body.due_date,
            color=body.color,
            description=body.description
        )
        # テーブル更新
        await database.execute(query)

        dt = Data(
            card_id=body.card_id,
            card_pos=body.card_pos,
            col_id=body.col_id,
            uid=token.uid,
            card_name=body.card_name,
            input_date=body.input_date,
            due_date=body.due_date,
            color=body.color,
            description=body.description
        )
        return Response(status=1, data=dt)
