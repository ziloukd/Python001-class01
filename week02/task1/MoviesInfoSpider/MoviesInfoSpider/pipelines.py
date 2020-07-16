import pymysql
from itemadapter import ItemAdapter


class MoviesinfospiderPipeline:

    def open_spider(self,spider):
        # host = spider.settings.get('MYSQL_HOST', 'localhost')
        # port = spider.settings.get('MYSQL_PORT', 3306)
        # user = spider.settings.get('MYSQL_USER', 'root')
        db_name = spider.settings.get('MYSQL_DB_NAME', 'movies_info')
        # password = spider.settings.get('MYSQL_PASSWORD', 'lwy12345678')
        # self.db_conn = pymysql.connect(
        #     host=host,
        #     port=port,
        #     user=user,
        #     password=password,
        #     charset='utf8'
        # )
        self.db_conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='lwy12345678',

            charset='utf8'
        )

        self.db_cur = self.db_conn.cursor()

        # 判断数据库是否存在，存在则pass,不存在则创建数据库
        exist = self.db_cur.execute('show databases like "%s"' % db_name)
        if not exist:
            self.db_cur.execute('create database %s' % db_name)
        
        # 切换数据库
        self.db_cur.execute('use %s' % db_name)

        # 判断表是否存在
        exist = self.db_cur.execute('show tables like "%s"' % 'maoyan_movies')

        if not exist:
            sql = '''
            create table maoyan_movies(
                电影 varchar(16),
                类型 varchar(16),
                上映时间 varchar(8))'''
            self.db_cur.execute(sql)

    def process_item(self, item, spider):
        keys = ', '.join(item.keys())
        values = ', '.join(['%s']  * len(item) )

        sql = f'insert into maoyan_movies ({keys}) values ({values})'
        self.db_cur.execute(sql, tuple(item.values()))
        return item

    def close_spider(self, spider):
        print('finished!')
        self.db_conn.commit()
        self.db_conn.close()