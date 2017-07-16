#-*- coding: utf-8 -*-

import MySQLdb
import json
import collections

if __name__=="__main__":

    f = open('s.json', 'r')
    json_dict = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()

    connector=MySQLdb.connect(host="localhost", db="j14017", user="j14017", passwd="", charset="utf8")
    cursor = connector.cursor()

    for index in json_dict:
        print json_dict[index]
        sql = "insert into users (sensor) values(" + str(json_dict[index]) + ")"
        cursor.execute(sql)

    connector.commit()
    cursor.close()
    connector.close() 
