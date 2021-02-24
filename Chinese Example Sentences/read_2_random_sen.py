import random
import sqlite3

def get_sentence():
    con = sqlite3.connect("sen_data.db")
    cur = con.cursor()

    char = "是"

    sql = "Select simplified, traditional, pinyin, english from examples where simplified like " + "'%" + char + "%'"

    cur.execute(sql)
    sent = cur.fetchall()

    sent_list = []
    r1 = random.choice(sent)
    r2 = random.choice(sent)

    print(r1)
    print(r2)
# get_sentence()
