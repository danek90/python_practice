import sqlite3
import time
import datetime
import random

conn =  sqlite3.connect('tutorial.db')

c = conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp REAL, keyword REAL, value REAL)')


def data_entry():
	c.execute('INSERT INTO stuffToPlot VALUES(145, "2016-01-01", "python", 5)')
	conn.commit()
	c.close()
	conn.close()

def dynamic_data_entry():
	unix = time.clock()
	date = str(datetime.datetime.fromtimestamp(unix).strftime('%y-%m-%d %H:%M:%S'))
	keyword = 'Python'
	value = random.randrange(0,10)
	c.execute("INSERT INTO stuffToPlot(unix, datestamp, keyword, value) VALUES(?, ?, ?, ?)", (unix, date, keyword, value))
	conn.commit()

def read_from_db():
	c.execute('SELECT keyword, unix, value, datestamp FROM stuffToPlot')
	#data = c.fetchall()
	#print(data)
	for row in c.fetchall():
		print row

def del_and_update():
	c.execute('SELECT * FROM stuffToPlot')
	print [row for row in c.fetchall()]

	c.execute('DELETE FROM stuffToPlot WHERE value = 99.0')
	conn.commit()
	'''
	c.execute('UPDATE stuffToPlot SET value = 99 WHERE value = 8')
	conn.commit()
	c.execute('SELECT * FROM stuffToPlot')
	print [row for row in c.fetchall()]

create_table()
for i in range(10):
	dynamic_data_entry()

'''	

create_table()
del_and_update()
c.close()
conn.close()	
