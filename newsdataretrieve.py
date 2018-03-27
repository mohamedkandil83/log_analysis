import psycopg2

# queries:
# What are the most popular three articles of all time?
query_1 = (
    "SELECT articles.title, count(*) FROM articles,success_log"
    " where success_log.path LIKE concat('%',articles.slug,'%')"
    " GROUP BY title ORDER BY count(*) DESC limit 3;"
      )

# Who are the most popular article authors of all time?
query_2 = (
    "select authors.name, count(*) from articles  inner join success_log"
    " on success_log.path LIKE concat('%',articles.slug,'%')"
    " inner join authors on authors.id=articles.author group by"
    " authors.name order by count desc;"
    )

# On which days did more than 1% of requests lead to errors?
query_3 = (
    "select date, ROUND(errors * 100.0 / total, 1)"
    "AS percentage from error_days WHERE ROUND(errors * 100.0 / total, 1) > 1;"
    )

# connect to the database


def connect():

    try:
        conn = psycopg2.connect("dbname=news")
        return conn
    except:
        print ("error in connecting to database")


def top_authors():

    conn = connect()
    cur = conn.cursor()
    cur.execute(query_2)
    print(cur.fetchall())
    conn.close()


def top_articles():

    conn = connect()
    cur = conn.cursor()
    cur.execute(query_1)
    print(cur.fetchall())
    conn.close()


def high_error_requests():

    conn = connect()
    cur = conn.cursor()
    cur.execute(query_3)
    print(cur.fetchall())
    conn.close()

top_articles()
top_authors()
high_error_requests()
