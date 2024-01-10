from fastapi import status, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from apis.services.authfunctions import get_current_user


class Model(BaseModel):
    async def exec(self, token: str):
        user = await get_current_user(token)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token"
            )

        content = {"detail": "Access token removed"}
        response = JSONResponse(content=content)
        response.set_cookie(
            key="access_token",
            value="",
            httponly=True,
            samesite="Strict",
            secure=False,
            max_age=0
            # domain=".local.dev",
        )

        return response
