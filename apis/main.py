from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apis.services.authfunctions import database
from .routers.signup import view as view1
from .routers.login import view as view2
from .routers.signout import view as view3
from .routers.addchannel import view as view4
from .routers.addmessage import view as view5
from .routers.delmessage import view as view6

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


# 起動時・終了時にデータベースと接続
@asynccontextmanager
async def app_lifespan(app):
    await startup_logic()
    yield
    await shutdown_logic()


async def startup_logic():
    print("Connecting to the database")
    await database.connect()


async def shutdown_logic():
    print("Disconnecting from the database")
    await database.disconnect()


app.router.lifespan_context = app_lifespan

for v in [view1, view2, view3, view4, view5, view6]:
    app.include_router(v.router)
