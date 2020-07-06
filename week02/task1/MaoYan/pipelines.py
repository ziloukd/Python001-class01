
import pymysql

dbInfo = {
    'host':'localhost',
    'port':3306,
    'user':'root',
    'password':'a123456',
    'db':'maoyan_movies'
    }

class MaoyanPipeline:
#    def process_item(self, item, spider):
#        return item

    #每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或者raise DropItem异常
    def process_item(self,item,spider):
        movie_name = item['movie_name']
        movie_type = item['movie_type']
        movie_time = item['movie_time']
        conn = pymysql.connect(
            host = dbInfo['host'],
            port = dbInfo['port'],
            user = dbInfo['user'],
            password = dbInfo['password'],
            db = dbInfo['db']
        )
        # 游标建立的时候就开启了一个隐形的事务
        cur = conn.cursor()
        try:
            data = [movie_name,movie_type,movie_time]
            cur.execute('create table if not exists test.movie(movie_name varchar(10),movie_type varchar(100),movie_time DATE)')
            cur.execute('insert into movie(movie_name,movie_type,movie_time) values(%s,%s,%s)',data)
        #关闭游标
            conn.commit()
            cur.close()
        except Exception as e:
            conn.rollback()
            conn.close()
            print(e)
        return item