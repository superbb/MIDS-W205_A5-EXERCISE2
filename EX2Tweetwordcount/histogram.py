"""
This script gets two integers k1,k2 and returns all the words that their total number of
occurrences in the stream is more or equal than k1 and less or equal than k2. For
example:
$ python histogram.py 3,8
$ <word2>: 8
<word3>: 6
<word1>: 3
"""
import psycopg2
import sys

def hist(k1,k2):
    conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
    cur = conn.cursor()
    try:
        cur.execute("SELECT word, count FROM Tweetwordcount ORDER BY word ASC WHERE count BETWEEN %d AND %d ORDER BY count DESC" % (k1,k2))
        records = cur.fetchall()    
        for rec in records:
            print (rec[0], rec[1])
    
    except psycopg2.ProgrammingError:
        print("No words between %d and %d. Try another range.", % (k1,k2))
    cur.close()
    conn.close()
    return True

if __name__ == '__main__':
    print sys.argv, len(sys.argv)
    try:
        if(len(sys.argv) == 2):
            args = sys.argv[1].split(',')
            k1 = int(args[0])
            k2 = int(args[1])
        elif(len(sys.argv) == 3):
            k1 = int(sys.argv[1].split(',')[0])
            k2 = int(sys.argv[2])
        if(k1 > k2):
            raise Exception()
        hist(k1,k2)
    except (ValueError, NameError, Exception):
        print('Error: User "python histogram.py k1,k2" where k1 and k2 are the inclusive lower and upper bounds of thehistogram. For example "python histogram.py 143,999"')