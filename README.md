#Exercise 2
## Setup Envireonment and Database
1. Run the UCB MIDS W205 EX2-FULL (ami-d4dd4ec3)
2. Make sure postgress is installed
./setup_ucb_complete_plus_postgres.sh
( https://s3.amazonaws.com/ucbdatasciencew205/setup_ucb_complete_plus_postgres.sh)
3. Set up the database
    1. log into user postgress to get access to make the tables
    2. create database Tcount
    3. connect to tcount (it saves names as lower case)
    4. create table Tweetwordcount
    5. check that the table was properly created
    6. log out of psql and user postgres
4. Make sure psycopg2 is also installed

```
[root@... ~]# su -w postgres
-bash-4.1$ psql
postgres=# CREATE DATABASE Tcount;
postgres=# \connect tcount;
tcount=# CREATE TABLE Tweetwordcount(word TEXT PRIMARY KEY NOT NULL, count INT NOT NULL);
tcount=# \dt
tcount=# \q
-bash-4.1$ logout
[root@... ~]# pip install psycopg2
```

5. Get the repository
https://github.com/superbb/MIDS-W205_A5-EXERCISE2.git

## Log into w205 and run the stream
```
[root@... ~]# su - w205
[w205@... ]$ cd ex2/Tweetwordcount/
[w205@... ]$ sparse run
```
Exit using ctrl C

## Summary Programs
```
[w205@... ]$ python finalyresults.py
[w205@... ]$ python finalyresults.py some_word_here
[w205@... ]$ python histogram.py 3,5
```
* finalresults.py
  * `python finalresults.py` returns all words alphabetically sorted with counts. 
  * `python finalresults.py word` returns the count for that specific word.
* histogram.py
  * `python histogram.py k1,k2` returns words and counts betweem k1, k2

## Other Files
* plot.png - Plot after a longer run
* plot-quick.png - Plot after a minute or two

## Screenshots
* screenshots/screenshot-start.png
* screenshots/screenshot-running.png
* screenshots/screenshot-break.png
* screenshots/screenshot-finalresults-word.png
* screenshots/screenshot-finalresults.png
* screenshots/screenshot-finalresults-and-histogram.png
* screenshots/screenshot-break-after-longer-for-plot.png  
