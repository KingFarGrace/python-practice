import pymysql
from datetime import datetime

"""
设计一个留言本的表（ID，留言内容，留言人，留言时间，是否删除）（表名，和字段名自己设计成英文：注意，不要用中文，用中文的直接0分）；
使用PyMySQL 驱动模块，实现对这个表的增加，删除，修改，查询；数据库操作需要加入异常处理逻辑；
"""


def do_execute(sql_content, *args):
    try:
        cursor.execute(sql_content, args)
        conn.commit()
        flag = True
    except Exception as e_exe:
        print(e_exe)
        flag = False
        conn.rollback()
    finally:
        return flag


def add_rec():
    name = input("请输入留言人用户名：")
    comment = input("请输入留言：")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sql = """INSERT INTO comment_board (comment, username, ctime, is_delete) 
                VALUES (%s, %s, %s, %s)"""
    add_flag = do_execute(sql, comment, name, now, 0)
    return add_flag


def del_rec():
    rec_id = input("请输入要删除的留言编号：")
    sql = "UPDATE comment_board SET is_delete=1 WHERE id=%s"
    del_flag = do_execute(sql, rec_id)
    return del_flag


def upd_rec():
    rec_id = input("请输入要修改的留言编号：")
    comment = input("请输入修改后的内容：")
    sql = "UPDATE comment_board SET comment=%s WHERE id=%s"
    upd_flag = do_execute(sql, comment, rec_id)
    return upd_flag


def find_rec():
    flag = True
    rec_id = input("请输入要查询的留言编号：")
    sql = "SELECT comment, is_delete FROM comment_board WHERE id=%s"
    try:
        cursor.execute(sql, (rec_id, ))
        conn.commit()
        result = cursor.fetchone()
        if result[1] == 1:
            print("您所查找的留言已被删除")
            flag = False
        else:
            print("查找成功！留言内容为：{}".format(result[0]))
            flag = True
    except Exception as e_exe:
        print(e_exe)
        flag = False
        conn.rollback()
    finally:
        return flag


if __name__ == '__main__':
    try:
        print("正在连接数据库，请稍等...")
        conn = pymysql.connect(host="localhost",
                               user="admin",
                               passwd="132546",
                               database="test",
                               charset="utf8")
        cursor = conn.cursor()
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
        conn.close()
        print("数据库连接已关闭")
