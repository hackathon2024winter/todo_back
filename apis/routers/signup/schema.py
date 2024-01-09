from pydantic import BaseModel, Field, validator
from typing import Optional
import re


class Request(BaseModel):
    username: str = Field(..., title="ユーザー名", description="ユーザー名")
    email: str = Field(..., title="email", description="メールアドレス")
    password1: str = Field(..., title="パスワード", description="パスワード")
    password2: str = Field(..., title="パスワード再入力", description="パスワード再入力")

    # usernameが空欄でないことをチェック
    @validator("username")
    def validate_empty_username(cls, value):
        if not value:
            raise ValueError("Username cannot be empty")
        return value

    # emailが空欄でないことをチェック
    @validator("email", pre=True)
    def validate_empty_email(cls, value):
        if not value:
            raise ValueError("Email cannot be empty")
        return value

    # メールアドレスの形式を確認
    @validator("email")
    def validate_email_format(cls, email):
        pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if re.match(pattern, email) is None:
            raise ValueError("Invalid email format")
        return email

    # password1が空欄でないことをチェック
    @validator("password1")
    def validate_empty_password1(cls, password):
        if not password:
            raise ValueError("Password cannot be empty")
        return password

    # password2が空欄でないことをチェック
    @validator("password2", pre=True)
    def validate_empty_password2(cls, password):
        if not password:
            raise ValueError("Password cannot be empty")
        return password

    # password1とpassword2が不一致のチェック
    @validator("password2")
    def validate_passwords_match(cls, password2, values):
        if "password1" in values and password2 != values["password1"]:
            raise ValueError("Passwords do not match")
        return password2


RequestExample = {
    "username": "hogehoge",
    "email": "hoge@gmail.com",
    "password1": "fugafuga",
    "password2": "fugafuga",
}


class Data(BaseModel):
    uid: str = Field(..., title="uuid", description="一意のid")
    username: str = Field(..., title="ユーザー名", description="ユーザー名")


class Response(BaseModel):
    status: int = Field(
        ...,
        title="返却値ステータス",
        description="返却値が存在する場合は1,検索基準日に未来が指定されたときなどが原因でデータが存在しない場合は0が返されます。",
    )
    data: Optional[Data] = Field(
        None, title="実績データ", description="実績データ。データが存在しない場合はこのフィールドは存在しません。"
    )


ResponseExamples = {
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "examples": {
                    "success": {
                        "summary": "成功",
                        "value": {
                            "status": 1,
                            "data": {
                                "uid": "550e8400-e29b-41d4-a716-446655440000",
                                "username": "hogehoge",
                            },
                        },
                    },
                    "error": {"summary": "エラーケース1", "value": {"status": 0}},
                }
            }
        },
    }
}
