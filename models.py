from sqlalchemy import Column, String, Integer, TIMESTAMP,  text

from database import Base


class TestTable(Base):
    __tablename__ = "testtable"

    id = Column(Integer, nullable=False,primary_key=True)
    email = Column(String, nullable=False)
    name = Column(String, nullable=False)
    count = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("now()"))
