import MySQLdb
import json
import collections



if __name__ == "__main__":

    connector = MySQLdb.connect(host="localhost", db="j14017", user="j14017", passwd='')
    cursor = connector.cursor()



    f = open('data.json', 'r')
    json_dict = json.load(f, object_pairs_hook=collections.OrderedDict)
    f.close()


    for index in json_dict:
        print json_dict[index]
        sql = "insert into  (data) values(" + str(json_dict[index]) + ")"
        cursor.execute(sql)

    connector.commit()
    cursor.close()
    connector.close()
