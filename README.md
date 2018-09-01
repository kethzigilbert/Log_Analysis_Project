# Kethzi Gilbert: Log Analysis
An internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.
The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, this code will answer questions about the site's user activity.

### Getting started
To run this project, you'll need database software (provided by a Linux virtual machine) and the database news to analyze as mentioned in the lessons of the Udacity's Full Stack Developer course.

This repository contains the python file which can be run from command line.

Run the following Queries on the 'news' database 

* CREATE view topthreelog as SELECT count(path) as total,replace(path,'/article/','') as path1 FROM LOG GROUP BY path ORDER BY total desc LIMIT 4;
* CREATE VIEW removelogpath as SELECT id,replace(path,'/article/','') as path1,status,method,time,ip FROM LOG;
* CREATE VIEW linklogart as Select rpl.id,path1,status,art.slug,art.author,art.title,rpl.time FROM removelogpath as rpl LEFT JOIN articles as art ON rpl.path1=art.slug;
* CREATE view daterequests AS SELECT date(time) as date, count(date(time)) FROM LOG GROUP BY date(time);
* CREATE VIEW dateerror AS SELECT date(time) as date,status,count(status) FROM log GROUP BY date(time),status HAVING status not like '2%';


Download and unzip contents.
run news.py from command line.

## Features
* The program you write in this project will run from the command line. It won't take any input from the user. 
* It will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.
* This code relies on View statements on the news database.

### Note:
This is a project for the Full Stack I course on Udacity.
