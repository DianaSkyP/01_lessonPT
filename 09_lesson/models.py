from sqlalchemy import (Column, Integer, String, DateTime,
                        Boolean, Date, create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, autoincrement=True)
    is_active = Column(Boolean, nullable=False, default=True)
    create_timestamp = Column(DateTime, nullable=False,
                              default=datetime.utcnow)
    change_timestamp = Column(DateTime, nullable=False,
                              default=datetime.utcnow,
                              onupdate=datetime.utcnow)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    middle_name = Column(String(20), nullable=True)
    phone = Column(String(15), nullable=False)
    email = Column(String(256), nullable=True)
    birthdate = Column(Date, nullable=True)
    company_id = Column(Integer, nullable=False)

    def __repr__(self):
        return (f"<Employee(id={self.id}, "
                f"name='{self.first_name} {self.last_name}', "
                f"email='{self.email}')>")

    def soft_delete(self):
        self.is_active = False
        self.change_timestamp = datetime.utcnow()


class DatabaseManager:

    def __init__(self, connection_string: str):
        self.engine = create_engine(connection_string)
        self.SessionLocal = sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=self.engine)

    def create_tables(self):
        pass

    def get_session(self):
        return self.SessionLocal()

    def drop_tables(self):
        pass


def get_db_connection_string():
    db_user = os.getenv('DB_USER', 'qa')
    db_password = os.getenv('DB_PASSWORD', 'skyqa')
    db_host = os.getenv('DB_HOST', '5.101.50.27')
    db_port = os.getenv('DB_PORT', '5432')
    db_name = os.getenv('DB_NAME', 'x_clients')

    return (f"postgresql://{db_user}:{db_password}"
            f"@{db_host}:{db_port}/{db_name}")
