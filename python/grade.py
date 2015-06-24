#!/usr/bin/env python

import sys
import csv
student=[]
with open('stats.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter = ',', quotechar = '"')
    students_max = []
    max_grade = -1
    index=0
    for idx, row in enumerate(spamreader):
        student = {
            'test_name' : row[0],
            'highschool' : row[1],
            'student_name' : row[2],
            'student_grade' : int(row[3])
                    }
        if idx == 0:
            students_max.append(student)    
        elif students_max[index]['test_name']!=student['test_name']:
            students_max.append(student)
            index=index+1
        elif students_max[index]['student_grade']<student['student_grade']:
            students_max[index]['test_name']=student['test_name']
            students_max[index]['highschool']=student['highschool']
            students_max[index]['student_name']=student['student_name']
            students_max[index]['student_grade']=student['student_grade']
for i in range(index+1):
    print "%s %s %s %d" % (students_max[i]['test_name'], students_max[i]['highschool'], students_max[i]['student_name'], students_max[i]['student_grade'])
