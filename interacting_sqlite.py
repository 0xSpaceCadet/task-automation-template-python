import sqlite3 as m_sql_db
from enum import STRICT
from os.path import exists
from pathlib import Path as m_path
import logging as m_log

print('sqlite version --',
      m_sql_db.sqlite_version)  # ==== print('sqlite version info --', m_sql_db.sqlite_version_info)

r_db_path = m_path.cwd() / 'ex.db'

conn_instance = m_sql_db.connect(database=r_db_path, isolation_level=None)  # ==== we can give paths
print(conn_instance)

ddl = 'CREATE table if not exists cats_copy (name text not null, birthdate text, fur text, weight_kg REAL) STRICT'
conn_instance.execute(ddl)

dql = 'SELECT name FROM sqlite_schema WHERE type="table"'
conn_table_list = [i for i in conn_instance.execute(dql).fetchall()]
print(*conn_table_list)

dql2 = 'PRAGMA TABLE_INFO(cats_copy)'
conn_table_list2 = conn_instance.execute(dql2).fetchall()
print(*conn_table_list2)

dml = 'INSERT INTO cats_copy (name, birthdate, weight_kg) VALUES (?, ?, ?)'
conn_instance.execute(dml, ['bob', '2nd Jan', 12])

print(conn_instance.execute('SELECT * FROM CATS_COPY').fetchall())
# conn_instance is like a CURSOR object in Pl/PGSql environment
