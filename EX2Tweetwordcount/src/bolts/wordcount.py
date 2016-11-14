from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

import psycopg2 #to communicate w PostreSQL

print(99999999999999999999999999999999l);


class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
        print('1111111111111111111111111111111111111111111111111111111111111111111111111')

    def process(self, tup):
        word = tup.values[0]
        print(word,tup.values[1],self.counts[word])
        print('22222222222222222222222222222222222222222222222222222222222222222222222222\n\n')
        # Increment the local count
        self.counts[word] += 1

        # Emit the tuple
        print('emit 33333 emit 33333333333333333333333333\n\n')
        self.emit([word, self.counts[word]])

        # Write codes to increment the word count in Postgres
        # Use psycopg to interact with Postgres
        # Database name: Tcount 
        # Table name: Tweetwordcount 
        # you need to create both the database and the table in advance.

        print('3333333333333333333333333333333333333333333333333333333333\n\n')
        # See readme for setup instructions
        conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

        # This cursor allows us to cut down on queries (doing mult rows at a time, to avoid memory overrun from large nums of rows)
        cur = conn.cursor()
        print('444444444444444444444444444444444444444444444444444444444444\n\n')
        if self.counts[word] == 1:
            #UPDATE DB: for new words, insert into the table        
            cur.execute("INSERT INTO Tweetwordcount (word,count) VALUES ('%s', 1)", word);
        else:
            #UPDATE DB: for existing words
            cur.execute("UPDATE Tweetwordcount SET count=%s WHERE word=%s", (self.counts[word], word))
        conn.commit()
        #cur.close()

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))

