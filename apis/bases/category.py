from sqlalchemy import Column, String, ForeignKey, Date
from sqlalchemy.dialects.mysql import INTEGER as Integer
from apis.bases.base import Base

class Category(Base):
    __tablename__ = "categories"  # テーブル名をcategoriesと指定 __tablename__はsqlalchemyの特別な変数
    __table_args__ = {"extend_existing": True}  # 既存テーブルの再定義を認める
    col_id = Column(String(36), primary_key=True)
    col_pos = Column(Integer(unsigned=True))
    col_name = Column(String(255), unique=True, nullable=False, index=True)
    description = Column(String(255), nullable=True)