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
```
[root@... ~]# su -w postgres
-bash-4.1$ psql
postgres=# CREATE DATABASE Tcount;
postgres=# \connect tcount;
tcount=# CREATE TABLE Tweetwordcount(word TEXT PRIMARY KEY NOT NULL, count INT NOT NULL);
tcount=# \dt
tcount=# \q
-bash-4.1$ logout
```

## Log into w205
```
su - w205
cd exercise_2/ex2/ EX2Tweetwordcount/
```
exit using ctrl C

## Key Files
* finalresults.py
  * `python finalresults.py` returns all words alphabetically sorted with counts. 
  * `python finalresults.py word` returns the count for that specific word.
* histogram.py
  * `python histogram.py k1,k2` returns words and counts betweem k1, k2





