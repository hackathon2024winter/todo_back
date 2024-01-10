from fastapi import status, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from .schema import Request
from apis.services.authfunctions import authenticate_user, create_access_token
from datetime import timedelta

ACCESS_TOKEN_EXPIRE_MINUTES = 720


class Model(BaseModel):
    async def exec(self, body: Request):
        user = await authenticate_user(body.email, body.password)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.uid}, expires_delta=access_token_expires
        )
        response = JSONResponse(content={"token_type": "bearer"})
        response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,
            samesite="Strict",
            secure=False,
            # domain=".local.dev",
        )

        return response
