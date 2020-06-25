# !/usr/bin/python3
# -*- encoding: utf-8 -*-

import dbutil.config as cfg
from sqlalchemy import Column, String, Integer, BigInteger, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Wage(Base):
    __tablename__ = 'python_engineer_wage'
    autoID = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    companyName = Column(String(255))
    locate = Column(String(16))
    wage = Column(String(10))


def _init_link():
    # 初始化连接
    engine = create_engine(cfg.SQLALCHEMY_DATABASE_URI)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session


class Model:
    ss = _init_link()
    @classmethod
    def set_info(cls, cmp_name, loc, wage):
        # 插入记录
        try: 
            record = Wage(companyName=cmp_name, locate=loc, wage=wage)
            cls.ss.add(record)
            cls.ss.commit()
        except Exception as e:
            print(e)
    
    @classmethod
    def find_bj_info(cls):
        # 寻找有关北京地区的记录
        try: 
            res_set = cls.ss.query(Wage).filter(Wage.locate.like('%北京%')).all()
            cls.ss.commit()
            return res_set
        except Exception as e:
            print(e)

    @classmethod
    def close_link(cls):
        cls.ss.close()