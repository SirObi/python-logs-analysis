#Running the report
1. Ensure you have the 'news' database in your current working directory.
2. In your Terminal, run ```psql news``` to access the database.
3. Create the necessary views:
###For top three articles
```create view top_three_articles as select title, count(status) from articles, log where concat('/article/', articles.slug) = log.path group by title order by count desc limit 3;```
###For list of top authors:
```create view top_authors as select name, count(status) from articles, authors, log where concat('/article/', articles.slug) = log.path and articles.author = authors.id group by name order by count desc;```
###For client errors report:
```create view request_success as select time::date as date, status, count(status)::float as successful_requests from log where status like '200%' group by date, status limit 100;```
```create view request_error as select time::date as date, status, count(status)::float as errors from log where status not like '200%' group by date, status limit 100;```
```create view high_error_days as select to_char(a.date,'DD Mon YYYY'), successful_requests, errors, (errors / successful_requests * 100)::decimal(5,2) as percentage from request_success as a, request_error as b where a.date = b.date and (errors / successful_requests > 0.01);```
4. Exit psql by Ctrl+D
5. Depending on your Python version run:
```python report.py``` or
```python3 report.py```

You should see the following output:

Top three articles of all time:
"Candidate is jerk, alleges rival" - 338647 views
"Bears love berries, alleges bear" - 253801 views
"Bad things gone, say good people" - 170098 views

The most popular article authors of all time:
Ursula La Multa - 507594 views
Rudolf von Treppenwitz - 423457 views
Anonymous Contributor - 170098 views
Markoff Chaney - 84557 views

Days with error rate > 1%:
17 Jul 2016 - 2.32% errors
