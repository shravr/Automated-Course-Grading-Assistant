# -*- coding: utf-8 -*-
import pandas as pd
import json
import sys

course_file = sys.argv[1]
students_file = sys.argv[2]
tests_file = sys.argv[3]
marks_file = sys.argv[4]

course_rows = pd.read_csv(course_file)
mark_rows = pd.read_csv(marks_file)
test_rows = pd.read_csv(tests_file)
student_rows = pd.read_csv(students_file)

class course:
    def __init__(self):
        self.id = 0
        self.name = 'n/a'
        self.teacher = 'n/a'
        self.courseAverage = 0

leng = len(course_rows.index)
courses = [course() for i in range(leng)]
for i in range(leng):
    courses[i].id = course_rows['id'].iloc[i]
    courses[i].name = course_rows['name'].iloc[i]
    courses[i].teacher = course_rows['teacher'].iloc[i]
    
class mark:
    def __init__(self):
        self.test_id = 0
        self.student_id = 0
        self.mark = 0

leng = mark_rows.shape[0]
marks = [mark() for i in range(leng)]
for i in range(leng):
    marks[i].test_id = mark_rows['test_id'].iloc[i]
    marks[i].student_id = mark_rows['student_id'].iloc[i]
    marks[i].mark = mark_rows['mark'].iloc[i]
    
class test:
    def __init__(self):
        self.id = 0
        self.course_id = 0
        self.weight = 0

leng = test_rows.shape[0]
tests = [test() for i in range(leng)]
for i in range(leng):
    tests[i].id = test_rows['id'].iloc[i]
    tests[i].course_id = test_rows['course_id'].iloc[i]
    tests[i].weight = test_rows['weight'].iloc[i]

class student:
    def __init__(self):
        self.id = 0
        self.name = 'n/a'

leng = student_rows.shape[0]
students = [student() for i in range(leng)]
for i in range(leng):
    students[i].id = student_rows['id'].iloc[i]
    students[i].name = student_rows['name'].iloc[i]


for test in tests:
    total = 0
    total += test.weight
    for test1 in tests:
        if test1.id != test.id and test.course_id == test1.course_id:
            total += test1.weight
            if total > 100:
                print(total)
                result = dict([('error', 'Invalid course weights')])
                with open('output.json', 'w') as outfile:
                    json.dump(result, outfile)
                sys.exit()
output_dict = {}
student_list = []
for student in students:
    details = {
        'id': '{}'.format(student.id),
        'name': '{}'.format(student.name)
    }
    totalCourseMarks = 0
    courseCount = set()
    courselist = []
    for course in courses:
        score = 0
        item = {}
        for test in tests:
            for mark in marks:
                if (mark.test_id == test.id):
                    if (course.id == test.course_id):
                        if student.id == mark.student_id:
                            courseCount.add(course.id)
                            score += test.weight * mark.mark * 0.01
                            totalCourseMarks += test.weight * mark.mark * 0.01
                            item = {
                                'id': '{}'.format(course.id),
                                'name': '{}'.format(course.name),
                                'teacher': '{}'.format(course.teacher),
                                'courseAverage': '{}'.format(score)
                            }
        courselist.append(item)
    details['courses'] = courselist
    lengthp = len(courseCount)
    totalCourseAverage = totalCourseMarks/lengthp
    details['totalAverage'] = '{}'.format(totalCourseAverage)
    student_list.append(details)

output_dict['students'] = student_list
    
with open('output.json', 'w') as outfile:
    json.dump(output_dict, outfile)

