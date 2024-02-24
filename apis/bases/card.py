from sqlalchemy import Column, String, ForeignKey, Date
from sqlalchemy.dialects.mysql import INTEGER as Integer
from apis.bases.base import Base
from apis.bases.category import Category
from apis.bases.user import User

class Card(Base):
    __tablename__ = "cards"  # テーブル名をcardsと指定 __tablename__はsqlalchemyの特別な変数
    __table_args__ = {"extend_existing": True}  # 既存テーブルの再定義を認める
    card_id = Column(String(36), primary_key=True)
    card_pos = Column(Integer(unsigned=True))
    col_id = Column(String(36), ForeignKey(Category.col_id, ondelete="CASCADE") , nullable=False)
    uid = Column(String(36), ForeignKey(User.uid), nullable=False)
    card_name = Column(String(255), nullable=False, index=True)
    input_date = Column(Date, nullable=True)
    due_date = Column(Date, nullable=True)
    color = Column(String(10), nullable=True)
    description = Column(String(255), nullable=True)
