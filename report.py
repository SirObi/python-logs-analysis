import psycopg2

# Generate top articles report
def get_top_articles():
    '''Outputs top 3 articles from database'''
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute("select * from top_three_articles")
    return c.fetchall()
    db.close()

top_articles = get_top_articles()
print("Top three articles of all time:")
for i in range (0, len(top_articles)):
    print('"{}" - {} views'.format(top_articles[i][0], top_articles[i][1]))

# Generate top authors report
def get_top_authors():
    '''Outputs list of top authors from database'''
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute("select * from top_authors")
    return c.fetchall()
    db.close()

top_authors = get_top_authors()
print("\nThe most popular article authors of all time:")
for i in range (0, len(top_authors)):
    print("{} - {} views".format(top_authors[i][0], top_authors[i][1]))

# Generate client error report
def get_high_error_days():
    '''Outputs list of days with high request error rate'''
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute("select * from high_error_days")
    return c.fetchall()
    db.close()

high_error_days = get_high_error_days()
print ("\nDays with error rate > 1%:")
for i in range (0, len(high_error_days)):
    print("{} - {}% errors".format(high_error_days[i][0], high_error_days[i][3]))
