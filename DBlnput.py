#-*-coding: utf-8-*-
import MySQLdb
if__name__=="__main__":
	connector = MySQLdb.connect(host="localhost", db="j14017", user="root", passwd="teikyo", charset="utf8")
	cursor = connector.cursor()
	sql = u"insert into led_light values('データ','データ2')"
	cursor.execute(sql)

	connector.commit()
	cursor.close()
	connector.close()
