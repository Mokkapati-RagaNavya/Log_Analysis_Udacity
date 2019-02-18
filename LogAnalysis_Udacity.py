#!/usr/bin/env python
import psycopg2
#first top 3 articles execution
def Most_Pop_Articles():
    conn=psycopg2.connect(dbname="news",user='vagrant',password='vagrant')
    cur=conn.cursor()
    q1= ''' SELECT title, views FROM loganalysis_articles INNER JOIN articles ON
    articles.slug = loganalysis_articles.slug ORDER BY views desc LIMIT 3; '''
    cur.execute(q1)
    rs=cur.fetchall()
    print(" \n  *What are the most popular three articles of all time ? \n")
    count=1
    for result in rs:
        num='(' + str(count) + ') "'
        tit= result[0]
        views = '"' + str(result[1]) + " views"
        print(num + tit + views)
        count=count+1
        #print('  "{0}"===>{1} views'.format(result[0], result[1]))
#top 4 authors
def Most_Pop_Authors():
    
    conn=psycopg2.connect(dbname="news",user='vagrant',password='vagrant')
    cur=conn.cursor()
    q2= '''
    SELECT logauthors_name.name AS author,
    sum(loganalysis_articles.views) AS views FROM loganalysis_articles INNER JOIN logauthors_name
    ON logauthors_name.slug=loganalysis_articles.slug
    GROUP BY logauthors_name.name ORDER BY views desc limit 4;
    '''
    cur.execute(q2)
    rs=cur.fetchall()
    print("\n  **Who are the most popular article authors of all time ? \n")
    count=1
    for result in rs:
        num='(' + str(count) + ') "'
        tit= result[0]
        views = '"Authors' + str(result[1]) + " views"
        print(num + tit + views)
        count=count+1
        #print('  "{0}"====>{1} views'.format(result[0], result[1]))
#lead errors
def Log_Error_Analysis():
    conn=psycopg2.connect(dbname="news",user='vagrant',password='vagrant')
    cur=conn.cursor()
    q3= '''
    SELECT logerror_fail.date ,(logerror_fail.count*100.00 / loganalysis_total.count) AS
    percentage FROM logerror_fail INNER JOIN loganalysis_total
    ON logerror_fail.date = loganalysis_total.date
    AND (logerror_fail.count*100.00 / loganalysis_total.count) >1
    ORDER BY (logerror_fail.count*100.00 /loganalysis_total.count) desc;
    '''
    cur.execute(q3)
    rs=cur.fetchall()
    print(" \n  ***Days on which more than 1% of requests lead to errors ? ")
    for result in rs:
        print('\n  On ' + str(result[0]) +'   ===>   ' + '%.1f' % result[1] +'% errors\n')
Most_Pop_Articles()
Most_Pop_Authors()
Log_Error_Analysis()
c.close()
conn.close()

