import pymysql
dbInfo = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : 'lxp123456',
    'db' : 'test'
}

class MaoyanmoviePipeline:
#    def process_item(self, item, spider):
#        return item

    # 每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或raise DropItem异常
     def process_item(self, item, spider):
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
        # 建立游标
         cur = conn.cursor()
         try:
             values = [movie_name,movie_type, movie_time]
             print(values)
             cur.execute('INSERT INTO  tb2 values(%s,%s,%s)' ,values)
             # 关闭游标
             cur.close()
             conn.commit()
         except:
             conn.rollback()
        # 关闭数据库连接
         conn.close()

         return item