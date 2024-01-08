from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers.signup import view as view1

app = FastAPI(docs_url="/docs", redoc_url="/redoc")

# AWSなどにデプロイしURLのドメインが確定したら指定する。
# ブラウザからのリクエストはdockerコンテナのサービス名に基づくURLを名前解決できない。
app.add_middleware(
    CORSMiddleware,
    # allow_origins=["https://frontend.local.dev:4443"],
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for v in [view1]:
    app.include_router(v.router)
