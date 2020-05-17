from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

"""
对2中的表结构，用SQLAlchemy模块来实现同样的操作
"""

print("正在连接数据库，请稍等...")
DIALECT = "mysql"
DRIVER = "pymysql"
USERNAME = "admin"
PASSWORD = "132546"
HOST = "localhost"
PORT = "3306"
DATABASE = "test"
DB_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8"\
    .format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)

Base = declarative_base()


class CommentBoard(Base):
    __tablename__ = 'comment_board'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    comment = Column(String(255), nullable=False)
    username = Column(String(32), nullable=False)
    ctime = Column(String(20), nullable=False)
    is_delete = Column(Integer, nullable=False)


def add_rec():
    name = input("请输入留言人用户名：")
    comment = input("请输入留言：")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        new_comment = CommentBoard(username=name, comment=comment, ctime=now, is_delete=0)
        session.add(new_comment)
        session.commit()
        flag = True
    except Exception as e_exe:
        print(e_exe)
        flag = False
    finally:
        return flag


def del_rec():
    rec_id = input("请输入需要删除的留言对应编号：")
    try:
        record = session.query(CommentBoard).filter_by(id=rec_id).first()
        record.is_delete = 1
        session.commit()
        flag = True
    except Exception as e_exe:
        print(e_exe)
        flag = False
    finally:
        return flag


def upd_rec():
    rec_id = input("请输入需要修改的留言对应编号：")
    new_comment = input("请输入修改后的留言内容：")
    try:
        record = session.query(CommentBoard).filter_by(id=rec_id).first()
        record.comment = new_comment
        session.commit()
        flag = True
    except Exception as e_exe:
        print(e_exe)
        flag = False
    finally:
        return flag


def find_rec():
    rec_id = input("请输入需要查找的留言对应编号：")
    try:
        record = session.query(CommentBoard).filter_by(id=rec_id).one()
        session.commit()
        if record.is_delete == 1:
            print("您所查找的留言已被删除！")
            flag = False
        else:
            print("查找成功！留言内容为：{}".format(record.comment))
            flag = True
    except Exception as e_exe:
        print(e_exe)
        flag = False
    finally:
        return flag


if __name__ == '__main__':
    try:
        engine = create_engine(DB_URI)
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        print("欢迎进入留言板")
        while True:
            print("""请输入指令选择操作：
                    add --> 添加一条评论
                    del --> 删除一条评论
                    upd --> 修改一条评论
                    find --> 查找一条评论
                    esc --> 退出
                    """)
            cmd = input("输入指令 >>> ")
            if cmd == 'esc':
                print("已退出留言板系统")
                break
            elif cmd == 'add':
                if add_rec():
                    print("留言发布成功！")
                else:
                    print("留言发布失败！")
            elif cmd == 'del':
                if del_rec():
                    print("留言删除成功！")
                else:
                    print("留言删除失败！")
            elif cmd == 'upd':
                if upd_rec():
                    print("留言修改成功！")
                else:
                    print("留言修改失败！")
            elif cmd == 'find':
                if not find_rec():
                    print("留言查找失败！")
            else:
                print("请正确输入指令！")

    except Exception as e:
        print(e)
        print("数据库连接失败")
    finally:
        session.close()
        print("数据库连接已关闭")
