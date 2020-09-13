# Automated-Course-Grading-Assistant

Python script run via the command line that processes csv files to produce a final score report in json.

First four csv files need to be created. The csv files found in this repo show the template that needs to be followed for courselists, student lists, mark breakdowns and test scores. 

Import libraries necessary - json, sys, pandas

To run:

python main.py courses.csv students.csv tests.csv marks.csv output.json
