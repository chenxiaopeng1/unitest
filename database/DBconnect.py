# coding=utf-8
import logging
import pymysql

'''
#读配置文件
config_dir = os.path.split(os.path.realpath(__file__))[0]
config_path = os.path.join(config_dir, "config.ini")
config = ConfigParser.SafeConfigParser()
config.read(config_path)
ip = config.get('config','ip')
user = config.get('config','user')
password =config.get('config','password')
db_name = config.get('config','db_name')

'''


class reqDB():

    def __init__(self, host, port, dbname, user, password):
        self.db = pymysql.connect(host=host, port=port or 3306, database=dbname,
                                  user=user, password=password)
        self.cursor = self.db.cursor()
        if not self.cursor:
            raise (NameError, " DataBase connected failed")
        else:
            print("DataBase connected sucess")

    # 查询数据库
    def selectDB(self, sql):
        logging.info("select:{} 语句：".format(sql))
        # 打开数据库连接
        # db = pymysql.connect(host="localhost", port=3306, database=dbname or "test", user="root", password="12345678")
        # 使用 cursor() 方法创建一个游标对象 cursor
        # cursor = self.db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        try:
            self.cursor.execute(sql)
            # 使用 fetchone() 方法获取单条数据.
            # data1=cursor.fetchone()
            data = self.cursor.fetchall()
            rowcount = self.cursor.rowcount
            logging.info("查询行数：", rowcount, "行", "select结果是：\n", data)
            print("查询行数:", rowcount, "select result is :\n {}".format(data))
        except Exception as e:
            print("链接数据库时发生错误", e)
        # 关闭数据库连接
        self.db.close()
        logging.info("断开数据库链接")
        return data

    # 执行更新或插入，delete等操作（select 除外的操作）
    def executeSQL(self, sql):
        logging.info("执行SQL：", sql)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            logging("SQL执行失败，操作回滚\n", e)
            self.db.rollback()

        data = self.cursor.fetchall()
        logging.info("执行结果为：\n", data)
        print("执行结果为:\n", data)
        self.db.close()
        return data

    '''
    #插入数据库
    def insertDB(self,sql):
        logging.info("插入数据库",sql)
        #cursor = self.db.cursor()
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print("连接数据库超时：", e)
            self.db.rollback()

        data=self.cursor.fetchall()

        logging.info("插入数据库：",data)
        print("插入数据库：",data)
        self.db.close()
        return data

    #更新数据库
    def updateDB(self,sql):
        logging.info("更新数据库：",sql)
        #cursor = self.db.cursor()

        try:
            self.cursor.execute(sql)
            self.db.commit()
        except TimeoutError as e:
            print("连接数据库超时：",e)
        except:
            self.db.rollback()

        data=self.cursor.fetchall()
        logging.info("更新数据库：",data)
        print("更新数据库：",data)
        self.db.close()
        return data
    '''

    def dbClose(self):
        self.db.close()
        logging.info("断开数据库链接")

    def getdbname(self):
        print(self.db.host_info)
        return self.db.host_info


if __name__ == "__main__":
    r = reqDB("localhost", 3306, "test", "root", "12345678")
    data = r.selectDB("select * from ads_dashboard_task_pig_info")

    if data.__len__() == 0:
        print("if data =()", data)

    d = reqDB("drds2219q71k0f46.drds.aliyun.boc", 3306, "yz_test_object_metrics", "yz_test_object_metrics",
              "gPq3d8lZPF4bVdaO")
    data2 = d.selectDB(
        "select * from ads_brc_idx_open_sow_rate where farm_id=170873872638279680 and dt_year='2018' and dt_type='1'")
    # print(type(data2))
    # 按 逗号分割 每行数据
    # data2.split(",")
    print(d.getdbname())
    for i in data2:
        # i.split(',')
        print(i[0])
