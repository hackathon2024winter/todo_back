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

        # Categoryテーブルの中で、受け取ったリクエスト中のcategory_idと一致するレコードを更新するクエリ（idの更新は想定しない）
        query = Category.__table__.update().where((Category.col_id == body.col_id)
        ).values(
            col_pos=body.col_pos,
            col_name=body.col_name,
            description=body.description
        )
        # テーブル更新
        await database.execute(query)

        dt = Data(
            col_id=body.col_id,
            col_pos=body.col_pos,
            # uid=token.uid,
            col_name=body.col_name,
            description=body.description
        )
        return Response(status=1, data=dt)
