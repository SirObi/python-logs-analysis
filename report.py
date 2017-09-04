#!/usr/bin/python3
import psycopg2


# Can be reused to connect to database
def execute_query(query):
    '''Connects to database, outputs results'''
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


# Generate top articles report
def get_top_articles():
    '''Prints top 3 articles from database'''
    query = "select * from top_three_articles"
    results = execute_query(query)
    print("Top three articles of all time:")
    for article, views in results:
        print('    "{}" - {} views'.format(article, views))


# Generate top authors report
def get_top_authors():
    '''Prints list of top authors from database'''
    query = "select * from top_authors"
    results = execute_query(query)
    print("\nThe most popular article authors of all time:")
    for author, views in results:
        print("    {} - {} views".format(author, views))


# Generate client error report
def get_high_error_days():
    '''Outputs list of days with high request error rate'''
    query = "select * from high_error_days"
    results = execute_query(query)
    print("\nDays with error rate > 1%:")
    for date, percentage in results:
        print("    {} - {}% errors".format(date, percentage))


if __name__ == "__main__":
    get_top_articles()
    get_top_authors()
    get_high_error_days()
