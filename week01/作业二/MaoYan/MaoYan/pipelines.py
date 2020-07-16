# -*- coding: utf-8 -*-
import csv


class MaoyanPipeline(object):

    def open_spider(self, spider):
        self.movie_dic = {
            '电影名': [],
            '类型': [],
            '上映时间': []
        }


    def process_item(self, item, spider):
        self.movie_dic['电影名'].append(item['movie_title'])
        self.movie_dic['类型'].append(item['movie_type'])
        self.movie_dic['上映时间'].append(item['release_time'])
        # print(self.movie_dic)


    def close_spider(self,spider):
        print(self.movie_dic)
        with open ('../movies.csv', 'w', encoding='utf-8-sig') as f1:
            writer = csv.DictWriter()
            writer.writerows(self.movie_dic)
        print('finished!')