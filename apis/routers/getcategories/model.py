from sqlalchemy import and_
from fastapi import status, HTTPException
from pydantic import BaseModel
from .schema import Response, TokenData, Data
from apis.services.authfunctions import database
from apis.bases.card import Category


class Model(BaseModel):
    async def exec(self, token: TokenData) -> Response:
        # loginしていない場合、拒否する。
        if not token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
            )

        query = Category.__table__.select()
        result = await database.fetch_all(query)

        arry = []  # dataリストを初期化
        for category in result:
            dt = Data(
                col_id = category.col_id,
                col_pos = category.col_pos,
                col_name = category.col_name,
                description = category.description
            )
            arry.append(dt)
        return Response(status=1, data=arry)
