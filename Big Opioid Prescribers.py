import pandas as pd
import os
import re
import sqlite3

os.chdir(
    "/Users/healthpolicyanalyst/Documents/Box Sync/python/"
    "Medicare Analyses/medicare_analysis/Data")

conn = sqlite3.connect('medicare_data.db')

c = conn.cursor()

c.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()


def regexp(expr, item):
    r = re.compile(expr)
    return r.match(item) is not None

conn.create_function("regexp", 2, regexp)

conn.execute("select * from scripts where generic_name regexp "
             "'OXYCODONE|CODEINE'").fetchmany(15)

opioids = pd.read_sql_query("SELECT * from scripts", conn)