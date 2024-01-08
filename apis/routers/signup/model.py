from pydantic import BaseModel
from .schema import Request, Response, Data


class Model(BaseModel):
    def exec(self, body: Request) -> Response:
        print(body.username)
        return Response(status=1, data=Data(uuid="1111", username="hahaha"))
