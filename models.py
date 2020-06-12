from sqlalchemy import BigInteger, Column, DateTime, Integer, SmallInteger, String, Table, Text, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Accesslog(Base):
    __tablename__ = 'accesslog'

    clientip = Column(Text)
    time = Column(DateTime(True))
    method = Column(Text)
    uri = Column(Text)
    query = Column(Text)
    status = Column(SmallInteger)
    bytes = Column(BigInteger)
    id = Column(Integer, primary_key=True, server_default=text("nextval('accesslog_id_seq'::regclass)"))


t_rawlog = Table(
    'rawlog', metadata,
    Column('record', String)
)

