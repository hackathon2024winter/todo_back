from fastapi import status, HTTPException
from pydantic import BaseModel
from .schema import Request, Response, TokenData
from apis.services.authfunctions import database
from apis.bases.card import Card
import json

class Model(BaseModel):
    async def exec(self, body: Request, token: TokenData) -> Response:
        # loginしていない場合、拒否する。
        if not token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
            )

        # Cardテーブルの中で、受け取ったリクエスト中のcard_idと一致するレコードを更新するクエリ
        for card in body.cards:
            query = Card.__table__.update().where((Card.card_id == card.card_id)
            ).values(
                card_pos=card.card_pos,
                col_id=card.col_id
            )
            # テーブル更新
            await database.execute(query)

        return Response(status=1, message="カードの位置情報(card_posおよびcol_id)を更新しました")
