from sqlalchemy import Column, String, ForeignKey, Date #※サンプルから変更なし
from sqlalchemy.dialects.mysql import INTEGER as Integer #※サンプルから変更なし
from apis.bases.base import Base #※サンプルから変更なし
# from apis.bases.category import Category #別途作成するcategory.pyからCategoryクラスをインポート（Category.idがFKとなる）
# from apis.bases.color import Color #別途作成するcolor.pyからColorクラスをインポート（Color.idがFKとなる）

class Card(Base):
    __tablename__ = "cards"  # テーブル名をcardsと指定 __tablename__はsqlalchemyの特別な変数
    __table_args__ = {"extend_existing": True}  # 既存テーブルの再定義を認める。※サンプルから変更なし
    id = Column(
        Integer(unsigned=True), autoincrement=True, primary_key=True, index=True
    ) #カードID
    category_id = Column(Integer(unsigned=True), nullable=False) #カテゴリID　あとで「ForeignKey(Category.id)」を追加
    color_id = Column(Integer(unsigned=True), nullable=False) #色ID　あとで「ForeignKey(Color.id)」を追加
    name = Column(String(255), unique=True, nullable=False, index=True) #カード名
    position = Column(Integer(unsigned=True)) #カードの位置
    due_date = Column(Date, nullable=False) #期限
    detail = Column(String(255), nullable=True) #カードの説明
