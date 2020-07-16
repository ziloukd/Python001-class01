import pymysql


class MoviesinfospiderPipeline():

    def open_spider(self):
        self.db_conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='lwy12345678',

            charset='utf8'
        )

        self.db_cur = self.db_conn.cursor()

        # 判断数据库是否存在，存在则pass,不存在则创建数据库
        exist = self.db_cur.execute('show databases like "%s"' % 'demo1')
        if not exist:
            self.db_cur.execute('create database %s' % 'demo1')
        
        self.db_cur.execute('use demo1')
        # # 判断表是否存在
        exist = self.db_cur.execute('show tables like "%s"' % 'maoyan_movies')

        if not exist:
            sql = '''
            create table if not exists maoyan_movies(
                电影 char(32),
                类型 char(32),
                上映时间 datetime)'''
            self.db_cur.execute(sql)

object1 = MoviesinfospiderPipeline()
object1.open_spider()