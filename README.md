# Chinese-Example-Sentences
Chinese sentences from [Tatoeba](https://tatoeba.org/eng/downloads) with simplified, traditional, pinyin and english translation for offline use in app.

# Download
### TSV file
This is tab separated file.
**| id | Simplified | Traditional | Pinyin | English |**
```
10	我不知道。	我不知道。	wǒ bù zhīdào 。	I do not know.
```
[Chinese Sentences with pinyin and translation](Chinese%20Example%20Sentences/cmn_sen_db_2.tsv)

### sqlite .db file
The [sen_data.db](Chinese%20Example%20Sentences/sen_data.db) contains table ```examples``` with ```id, simplified, traditional, pinyin, english```.

[sen_data.db](Chinese%20Example%20Sentences/sen_data.db)

# Usage
Get two random sentences with pinyin, traditional characters and translation<br>
View [read_2_random_sen.py](Chinese%20Example%20Sentences/read_2_random_sen.py)

# Create
1. Download sentences database from [Tatoeba](https://tatoeba.org/eng/downloads)
2. Use Google translate to translate the sentences
3. Use Python module ```pinyin_jyutping_sentence``` and ```hanziconv``` to generate pinyin and traditional characters for sentences
4. Use [gen_sen.py](Chinese%20Example%20Sentences/gen_sen.py) and write data to ```.tsv``` file 
5. Use [tsv_to_db.py](Chinese%20Example%20Sentences/tsv_to_db.py) python code to create databases.

## View this for creating tsv and db files for other language
[Simple 中文](https://simplezhongwen.blogspot.com/2021/03/create-language-database-with.html)