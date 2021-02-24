import csv, sqlite3

def sen_to_db():    
    conn = sqlite3.connect("sen_data.db")
    curs = conn.cursor()

    curs.execute("CREATE TABLE examples (id INTEGER PRIMARY KEY, simplified TEXT, traditional TEXT, pinyin TEXT, english TEXT);")

    reader = csv.reader(open('cmn_sen_db_2.tsv', 'r', encoding="utf-8"), delimiter='\t')

    for row in reader:
        to_db = [row[1], row[2], row[3], row[4]]
        curs.execute("INSERT INTO examples (simplified, traditional, pinyin, english) VALUES (?, ?, ?, ?);", to_db)
    conn.commit()

# sen_to_db()
