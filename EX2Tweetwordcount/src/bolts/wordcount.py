from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

import psycopg2 #to communicate w PostreSQL

class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
        
    def process(self, tup):
        word = tup.values[0]

        # Write codes to increment the word count in Postgres
        # Use psycopg to interact with Postgres
        # Database name: Tcount 
        # Table name: Tweetwordcount 
        # you need to create both the database and the table in advance.

        # See readme for setup instructions
        conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

        # This cursor allows us to cut down on queries (doing mult rows at a time, to avoid memory overrun from large nums of rows)
        cur = conn.cursor()
        
        # Increment the local count
        self.counts[word] += 1

        if self.counts[word] == 1:
            #UPDATE DB: for new words, insert into the table        
            cur.execute("INSERT INTO Tweetwordcount (word,count) VALUES ('%s', 1)", word);
        else:
            #UPDATE DB: for existing words
            cur.execute("UPDATE Tweetwordcount SET count=%d WHERE word=%s", (self.counts[word], word))
        conn.commit()

        #compare against counter here, remove when done debugging
        print "--word: ", word, " | log count : ", self.counts[word], "db:"
        
        cur.execute("SELECT word, count from Tweetwordcount WHERE word = %s", word)
        records = cur.fetchall()
        for rec in records:
            print "word = ", rec[0], "| db count = ", rec[1], "\n"
        conn.commit()

        # Emit the tuple
        self.emit([word, self.counts[word]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))

        cur.close()
        conn.close()