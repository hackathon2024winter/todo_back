from fastapi import status, HTTPException
from pydantic import BaseModel
from .schema import Request, Response, TokenData, Data
from apis.services.authfunctions import database
from apis.bases.category import Category


class Model(BaseModel):
    async def exec(self, body: Request, token: TokenData) -> Response:
        # loginしていない場合、拒否する。
        if not token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
            )

        # Categoryテーブルに挿入するクエリ作成
        query = Category.__table__.insert().values(
            col_id=body.col_id,
            col_pos=body.col_pos,
            uid=token.uid,
            col_name=body.col_name,
            description=body.description
        )
        # テーブル更新
        await database.execute(query)

        dt = Data(
            col_id=body.col_id,
            col_pos=body.col_pos,
            uid=token.uid,
            col_name=body.col_name,
            description=body.description
        )
        return Response(status=1, data=dt)
