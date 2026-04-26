from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from database import Base
import datetime
import enum

class DocType(enum.Enum):
    invoice = "invoice"
    report = "report"
    contract = "contract"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    role_id = Column(Integer, ForeignKey("roles.id"))
    role = relationship("Role")

class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True) # Admin, Analyst, Auditor, Client


class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    company_name = Column(String, nullable=True)
    document_type = Column(String) # invoice, report, contract
    uploaded_by = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


