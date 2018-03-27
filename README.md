# log_analysis

## Description

In Udacity Full Stack Nanodegree program. Task number 3 is about a reporting using the logs. The program executes three given queries and print the results as plain text. The queries are about top authors, articles and error requests. Module psycopg2 is used for postegres.

## How to set up environment for the project

- install VirtualBox
- install Vagrant

## How to Run 
Use these commands:
- vagrant up 
- vagrant ssh
- psql -d news -f newsdata.sql

Create the following views:
```sql
CREATE VIEW success_log AS SELECT * from log where status like '%200%';

CREATE VIEW error_days AS SELECT date(time)  , count(status) as total, SUM(CASE WHEN status NOT LIKE '%200%' THEN 1 ELSE 0 END) as errors FROM log GROUP BY date(time);
```

Clone the repo
Using Python 2.7
Run the command in the file directory
python newsdataretrieve.py

Enjoy!!
