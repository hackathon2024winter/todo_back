from sqlalchemy import Column, String, ForeignKey, Date
from sqlalchemy.dialects.mysql import INTEGER as Integer
from apis.bases.base import Base
from apis.bases.category import Category #別途作成するcategory.pyからCategoryクラスをインポート（Category.idがFKとなる）
# from apis.bases.color import Color #別途作成するcolor.pyからColorクラスをインポート（Color.idがFKとなる）

class Card(Base):
    __tablename__ = "cards"  # テーブル名をcardsと指定 __tablename__はsqlalchemyの特別な変数
    __table_args__ = {"extend_existing": True}  # 既存テーブルの再定義を認める
    card_id = Column(String(36), primary_key=True)
    card_pos = Column(Integer(unsigned=True))
    col_id = Column(String(36), ForeignKey(Category.col_id) ,nullable=False)
    card_name = Column(String(255), unique=True, nullable=False, index=True)
    input_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=False)
    color = Column(String(10), nullable=False) #色ID　あとで「ForeignKey(Color.id)」を追加
    description = Column(String(255), nullable=True)
