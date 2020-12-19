# _*_coding: utf-8 _*
# @Time ：2020/9/26 9:03
# @Author: AsenLi

import pymysql
import re

# username : root
# password : root


class DataBaseHandle(object):
    ''' 定义一个 MySQL 操作类'''

    def __init__(self, host, username, password, database, port):
        '''初始化数据库信息并创建数据库连接'''
        # 下面的赋值其实可以省略，connect 时 直接使用形参即可
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.port = port
        self.db = pymysql.connect(self.host, self.username, self.password, self.database, self.port, charset='utf8')

    def createTable(self, sql,table_name):
        """
        sql ：新建表语句
        table_name: 表名称
        """
        try:
            self.cursor = self.db.cursor()
            self.cursor.execute("show tables")
            table_list = self.cursor.fetchall()
            tables_list = re.findall('(\'.*?\')', str([table_list]))
            databases_list = [re.sub("'", '', each) for each in tables_list]
            if table_name.lower() in databases_list:
                print("******table exists*******")
                return '******table exists*******'
            # 新建表
            self.db.cursor().execute(sql)

            print('创建成功')
        except Exception as e:
            print('查询出错 %s' % e)
        finally:
            self.cursor.close()

    def selectDb(self, sql):
        '''
        数据库查询
        sql：查询语句
        '''
        self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            self.cursor.execute(sql)  # 返回 查询数据 条数 可以根据 返回值 判定处理结果
            data = self.cursor.fetchall()  # 返回所有记录列表
            print(data)
        except Exception as e:
                print('查询出错 %s' % e)
        finally:
            self.cursor.close()

    def updateDb(self, sql):
        '''
         更新数据库操作
         sql：更新语句
         '''

        self.cursor = self.db.cursor()

        try:
            tt = self.cursor.execute(sql) # 返回 更新数据 条数 可以根据 返回值 判定处理结果
            print('成功更新 %s 条' % tt)
            self.db.commit()
        except Exception as e:
            print('更新出错 %s' % e)
            # 发生错误时回滚
            self.db.rollback()
        finally:
            self.cursor.close()

    def insertDB(self, sql):
        ''' 插入数据库操作 '''

        self.cursor = self.db.cursor()

        try:
            tt = self.cursor.execute(sql)  # 返回 插入数据 条数 可以根据 返回值 判定处理结果
            self.db.commit()
            print('插入成功 %s 条'%tt)
        except Exception as e:
            print(e)
            # 发生错误时回滚
            self.db.rollback()
        finally:
            self.cursor.close()

    def deleteDB(self, sql):
        ''' 操作数据库数据删除 '''
        self.cursor = self.db.cursor()

        try:
            # 执行sql
            tt = self.cursor.execute(sql) # 返回 删除数据 条数 可以根据 返回值 判定处理结果
            print('成功删除 %s 条' % tt)
            self.db.commit()
        except Exception as e:
            print('删除出错 %s' % e)
            # 发生错误时回滚
            self.db.rollback()
        finally:
            self.cursor.close()

    def closeDb(self):
        ''' 数据库连接关闭 '''
        self.db.close()


if __name__ == '__main__':
    DbHandle = DataBaseHandle('127.0.0.1', 'root', 'root', 'rcw', 3306)
    # 查询
    # DbHandle.selectDb('select * from test_table where name = "1"')
    # 新建表
    DbHandle.createTable('CREATE TABLE IF NOT EXISTS USERS(ID VARCHAR (255) NOT NULL ,USERNAME VARCHAR (255)NOT NULL,groups VARCHAR (255)NOT NULL,PRIMARY KEY (ID))','USERS')
    # 插入
    # DbHandle.insertDB('insert into test_table(username, name) values ("{}","{}")'.format('FuHongXue', 'wwwww'))
    # 更新
    # DbHandle.updateDb('update test_table set username = "%s" where name = "%s"' % ('aaaaa', 'wwwww'))
    # 删除
    # DbHandle.deleteDB('delete from test_table where id = "%d"' % (25))

    DbHandle.closeDb()
