import os
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
from .routers.delchannel import view as view7
from .routers.getchannels import view as view8
from .routers.getmessages import view as view9
from .routers.getcards import view as view10
from .routers.getcategories import view as view11
from .routers.addcard import view as view12
from .routers.addcategory import view as view13
from .routers.getboardview import view as view14
from .routers.updatecard import view as view15
from .routers.getboarddetail import view as view16
from .routers.delcard import view as view17
from .routers.updatecardsposition import view as view18

is_with_proxy = os.getenv("IS_WITH_PROXY")
if is_with_proxy == "True":
    # コンテナ単体の.envでは宣言せず、ルートの.envだけで宣言すると正しく読み込まれる。
    app = FastAPI(
        root_path="/fastapi",
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )
else:
    app = FastAPI(docs_url="/docs", redoc_url="/redoc", openapi_url="/openapi.json")


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

for v in [
    view1,
    view2,
    view3,
    view4,
    view5,
    view6,
    view7,
    view8,
    view9,
    view10,
    view11,
    view12,
    view13,
    view14,
    view15,
    view16,
    view17,
    view18,
]:
    app.include_router(v.router)
