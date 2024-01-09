from .oauth2 import OAuth2PasswordBearerWithCookie
from sqlalchemy import select
from passlib.context import CryptContext
from databases import Database
from apis.bases.user import User
import os

user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
server = os.getenv("MYSQL_HOST_FAST")
port = os.getenv("PORT_MYSQL_FAST")
db = os.getenv("MYSQL_DB_FAST")
DATABASE_URL = f"mysql+pymysql://{user}:{password}@{server}:{port}/{db}"
database = Database(DATABASE_URL)

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
oauth2_scheme = OAuth2PasswordBearerWithCookie(tokenUrl="token")


# Dependの引数にするには関数型で渡す。インスタンスはエラーになる。
def get_pwd_context():
    return CryptContext(schemes=["bcrypt"], deprecated="auto")


# ユーザーの新規登録の際、そのemailが登録済かどうかを確認。
async def select_by_email(email: str):
    query = select([User]).where(User.email == email)
    result = await database.fetch_one(query)
    return result
