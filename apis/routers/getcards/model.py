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
                id=card.id,
                category_id = card.category_id,
                color_id = card.color_id,
                name = card.name,
                position = card.position,
                due_date = card.due_date,
                detail = card.detail
            )
            arry.append(dt)
        return Response(status=1, data=arry)
