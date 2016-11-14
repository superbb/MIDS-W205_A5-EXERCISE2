from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

import psycopg2 

class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()

    def process(self, tup):
        word = tup.values[0]
        # Increment the local count
        self.counts[word] += 1
        # Emit the tuple
        self.emit([word, self.counts[word]])
        print(word, self.counts[word])
        # Write codes to increment the word count in Postgres
        # Use psycopg to interact with Postgres
        # Database name: Tcount 
        # Table name: Tweetwordcount 
        # you need to create both the database and the table in advance.

        # See readme for setup instructions
        conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
        cur = conn.cursor()
        cur.execute("SELECT count FROM Tweetwordcount WHERE word = '%s'" % (word))
        db_count = cur.fetchone()
        conn.commit()


        print(db_count)

        if db_count:
            #print("\n\na\n\n(UPDATE Tweetwordcount SET count = %d  WHERE word = '%s'" % (self.counts[word], word))
            cur.execute("UPDATE Tweetwordcount SET count = %d  WHERE word = '%s'" % (self.counts[word],word))
        else:
            #print("\n\nb\n\n(INSERT INTO Tweetwordcount (word, count) VALUES ('%s',%d)" % (word, self.counts[word]))
            db_count = 0
            cur.execute("INSERT INTO Tweetwordcount (word, count) VALUES ('%s',%d)" % (word,self.counts[word]))

        #print("\n\nc\n\n")
        conn.commit()
        cur.close()
        conn.close()
        # Log the count - just to see the topology running
        self.log("%s: int: %d" % (word, self.counts[word]))
        print(word, "local", self.counts[word],"db", db_count)


#if __name__ == '__main__':
#    print(1111)
#    wordlist = (['bb-cat',9], ['bb-dog',1], ['bb-kangoo',2])
#    
#    for w,c in wordlist:
#       conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
#       cur = conn.cursor()
#       cur.execute("SELECT count FROM Tweetwordcount WHERE word = '%s'" % (w))
#       db_count = cur.fetchone()
#       print(db_count)
#       if db_count:
#            print("UPDATE Tweetwordcount SET count = %d  WHERE word = '%s'" % (c,w))
#            cur.execute("UPDATE Tweetwordcount SET count = %d  WHERE word = '%s'" % (c,w))
#       else:
#            print("INSERT INTO Tweetwordcount (word, count) VALUES ('%s', %d)" % (w,c))
#            db_count = 0
#            cur.execute("INSERT INTO Tweetwordcount (word, count) VALUES ('%s', %d)" % (w,c))
#       conn.commit()
#       cur.close()
#       conn.close()

