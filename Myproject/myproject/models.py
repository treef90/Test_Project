#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

from sqlalchemy import (
    Integer,
    Column,
    Index,
    Text,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    email = Column(Text)
    topic_treatment = Column(Text)
    text_treatment = Column(Text)

Index('my_index', MyModel.email, unique=True, mysql_length=255)
