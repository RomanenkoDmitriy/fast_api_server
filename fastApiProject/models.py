from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class PhoneNumber(Base):
    __tablename__ = 'phone_number'

    hash_number = Column(String, primary_key=True)
    phone_number = Column(String)




