#!/usr/bin/python
# "Database code" for the DB News.

import datetime
import psycopg2


def get_cursor():
    conn = psycopg2.connect(database="news")
    c = conn.cursor()
    return c


def get_popu_three_articles():
    c = get_cursor()
    c.execute("""Select art.title, ttl.total FROM articles
                 as art, topthreelog as ttl
                 WHERE art.slug=ttl.path1 ORDER BY ttl.total desc""")
    logspop = c.fetchall()
    print "Popular Articles"
    for i in range(0, 3):
        print '"{}" - {} views'.format(logspop[i][0], logspop[i][1])


def get_popular_authors():
    c = get_cursor()
    c.execute("""SELECT count(aut.name) as autcount, aut.name
                from linklogart as lla, authors as aut
                WHERE lla.author=aut.id GROUP BY aut.name
                ORDER BY autcount desc""")
    logspop = c.fetchall()
    print "\nPopular Authors"
    for i in range(0, len(logspop)):
        print '"{}" - {} views'.format(logspop[i][1], logspop[i][0])


def get_error_perc():
    c = get_cursor()
    c.execute("""SELECT dr.date, ((de.count / dr.count :: float) * 100)
    :: numeric(10, 2)
    as errorperc FROM daterequests as dr, dateerror as de
    WHERE dr.date=de.date and (de.count/dr.count :: float) * 100 > 1""")
    logspop = c.fetchall()
    print '\nOn which days did more than 1% of requests lead to errors?'
    for i in range(0, len(logspop)):
        print '{} - {} %'.format(logspop[i][0].strftime("%d,%B,%Y"),
                                 logspop[i][1])

if __name__ == '__main__':
    get_popu_three_articles()
    get_popular_authors()
    get_error_perc()
