 #Description  
 The purpose of this project was to create an internal reporting tool
 for a newspaper site. The tool uses logs from the newspaper's server to help answer
 the following questions regarding the user traffic on the website:  
 1) Which are the three most popular articles?  
 2) What's the relative popularity of each article author?  
 3) Were there any days with a 404 error rate above 1% of the overall traffic volume?  

 #Prerequisites
 In order to run the tool, you'll need to install a Linux-based virtual machine (VM)
 This will provide you with the necessary environment (including Python 3 and an empty PostgreSQL database).
 You'll also need to download the sql file containing the news site's user-traffic data and
 use it to populate the database.
 ##Install the virtual machine  
 First, download and install Virtual Box: https://www.virtualbox.org/wiki/Downloads  
 Then, download and install Vagrant: https://www.vagrantup.com/downloads.html  
 Finally, select a folder on your PC from which you'd like to run the tool.  
 Fork and clone the following repository into the folder you've just selected: https://github.com/udacity/fullstack-nanodegree-vm
 Navigate to the repository you've just created and cd to the subdirectory called "vagrant".
 At this step, download the repository containing this README file and copy report.py into the "vagrant" directory.  
 From the terminal, run ```vagrant up```.
 The virtual machine is now being installed - it may take a while.

 ##Download the data
 The data can be found under the following link: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip  
 Make sure to unzip the file and move it to the vagrant directory.

 Once the VM has been installed, run ```vagrant up``` to start the machine.
 Then run ```vagrant ssh``` to log in.
 (You can always log out of the virtual machine with the ```logout``` command.)

 ##Populate the database
 You can use the following command: ```psql -d news -f newsdata.sql```.

 ##Install the dependencies
 This project is written in Python and requires a PostgreSQL adapter called psycopg2.
 Use ```pip install psycopg2``` or ```pip3 install psycopg2``` to install it.


 #Running the report
1. Ensure you have the 'news' database in your current working directory.
2. In your Terminal, run ```psql news``` to access the database.
3. Create the necessary views:
### For top three articles:
```create view top_three_articles as select title, count(status) from articles, log where concat('/article/', articles.slug) = log.path group by title order by count desc limit 3;```
### For list of top authors:
```create view top_authors as select name, count(status) from articles, authors, log where concat('/article/', articles.slug) = log.path and articles.author = authors.id group by name order by count desc;```
### For client errors report:
```create view request_success as select time::date as date, count(status)::float as successful_requests from log where status like '200%' group by date;```  

```create view request_error as select time::date as date, count(status)::float as errors from log where status not like '200%' group by date;```  

```create or replace view high_error_days as select to_char(a.date,'DD Mon YYYY'), (errors / (successful_requests + errors) * 100)::decimal(5,2) as percentage from request_success as a, request_error as b where a.date = b.date and (errors / (successful_requests + errors) > 0.01);```  

4. Exit psql by Ctrl+D  
5. Run: ```python3 report.py```  

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
    17 Jul 2016 - 2.26% errors
