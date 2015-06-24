#!/usr/bin/env python

import sys
import csv
import pdb
student=[]
with open('stats.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter = ',', quotechar = '"')
    students_max = []
    students=[]
    max_grade = -1
    index=0
    nr=0
    for idx, row in enumerate(spamreader):
        #pdb.set_trace()
        student = {
            'test_name' : row[0],
            'highschool' : row[1],
            'student_name' : row[2],
            'student_grade' : int(row[3])
                    }
        if idx == 0:
            students.append(student)
            nr=nr+1
        elif students[nr-1]['test_name']!=student['test_name']:
            i=0
            for s in students:
        		students_max.append(students[i])
        		index=index+1
        		i=i+1
            students=[]
            students.append(student)
            nr=1
        else:
        	ok=0;
        	i=0
        	while i<nr:
        		if students[i]['highschool']==student['highschool']:
        			ok=1;
        			if students[i]['student_grade']<student['student_grade']:
        			    students[i]['student_name']=student['student_name']
        			    students[i]['student_grade']=student['student_grade']
        		i=i+1
        	if ok==0:
        	    students.append(student)
        	    nr=nr+1
for i in range(index):
    print "%s: %s, %s, %d" % (students_max[i]['test_name'], students_max[i]['highschool'], students_max[i]['student_name'], students_max[i]['student_grade'])
