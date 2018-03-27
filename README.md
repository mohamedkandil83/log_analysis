# log_analysis

The third project in Udacity Full Stack Nanodegree

How to set up environment for the project

- install VirtualBox
- install Vagrant

How to Run 
Use these commands:
- vagrant up 
- vagrant ssh
- psql -d news -f newsdata.sql

Create the following views:

CREATE VIEW success_log AS SELECT * from log where status like '%200%';
CREATE VIEW error_days AS SELECT date(time)  , count(status) as total, SUM(CASE WHEN status NOT LIKE '%200%' THEN 1 ELSE 0 END) as errors FROM log GROUP BY date(time);


Clone the repo
Using Python 2.7
Run the command in the file directory
python newsdataretrieve.py

Enjoy!!
