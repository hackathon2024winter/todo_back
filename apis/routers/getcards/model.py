from sqlalchemy import and_
from fastapi import status, HTTPException
from pydantic import BaseModel
from .schema import Response, TokenData, Data
from apis.services.authfunctions import database
from apis.bases.card import Card


class Model(BaseModel):
    async def exec(self, token: TokenData) -> Response:
        # loginしていない場合、拒否する。
        if not token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
            )

        query = Card.__table__.select()
        result = await database.fetch_all(query)

        arry = []  # dataリストを初期化
        for card in result:
            dt = Data(
                card_id=card.card_id,
                card_pos = card.card_pos,
                col_id = card.col_id,
                card_name = card.card_name,
                input_date = card.input_date,
                due_date = card.due_date,
                color = card.color,
                description = card.description
            )
            arry.append(dt)
        return Response(status=1, data=arry)
