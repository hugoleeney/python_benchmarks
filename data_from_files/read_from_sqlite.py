import sqlite3

from timer import timer
from trials.gen_trials import get_trials

conn = sqlite3.connect('example.db')

#conn.execute('''CREATE TABLE stocks (number integer)''')
for t in get_trials(1000000, 10):
    for i in t[3]:
        conn.execute("INSERT INTO stocks VALUES (%s)"%(i))


conn.commit()

with timer('select'):
    result = [x[0] for x in conn.execute("select * from stocks")]

