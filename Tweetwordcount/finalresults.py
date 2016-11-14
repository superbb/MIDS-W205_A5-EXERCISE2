"""
This script gets a word as an argument and returns the total number of word occurrences in the stream. For example:
$ python finalresults.py hello
$ Total number of occurences of "hello": 10

Running finalresults.py without an argument returns all the words in the stream and their total count of occurrences, sorted alphabetically in an ascending order, one word per line. For example:
$ python finalresults.py
$ (<word1>, 2), (<word2>, 8), (<word3>, 6), (<word4>, 1), ...
"""
import psycopg2
import sys

def wordcounts(word):
    conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
    cur = conn.cursor()
    if word == "":
        cur.execute("SELECT word, count FROM Tweetwordcount ORDER BY word ASC")
        records = cur.fetchall()    
        for rec in records:
            print rec[0], rec[1]
    else:
        try:
            cur.execute("SELECT word, count FROM Tweetwordcount WHERE word = '%s'" % (word))
            rec = cur.fetchone()
            if rec:
                 print('Total number of occurences of "%s": %d' % (rec[0],rec[1]))
            else:
                 print('Total number of occurences of "%s": 0' % word)
        except psycopg2.ProgrammingError:
            print("Something wrong with the query: \nSELECT word, count FROM Tweetwordcount WHERE word = '%s'" % (word))
    cur.close()
    conn.close()
    return True


if __name__ == '__main__':
    if len(sys.argv) == 1:
        wordcounts("")
    elif len(sys.argv) == 2:
        wordcounts(sys.argv[1])
    else:
        print('Error: too many args. Use "python finalresults.py" to get a list or "python finalresults.py myword" to get myword\'s count')
