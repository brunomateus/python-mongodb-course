#Write a program in the language of your choice that will remove the grade of
#type "homework" with the lowest score for each student from the dataset that you
#imported in HW 2.1. Since each document is one grade, it should remove one
#document per student.


import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.school
students = db.students


def do_it():

    print "Homework3-1"

    query = {}
    projection = {}

    try:

        cursor = students.find(query).sort([('_id', pymongo.ASCENDING)])


    except:
        print "Unexpected error:", sys.exc_info()[0]


    for student in cursor:
        print student      
        new_grades = remove_lowest_homework(student['scores'])
        update_grades(student, new_grades)


def remove_lowest_homework(grades):
    lowest_homework = {'score':1000}
    
    for grade in grades:
		if (grade['type'] == 'homework' and grade['score'] < lowest_homework['score']):
			lowest_homework=grade
    grades.remove(lowest_homework)            
    return grades


def update_grades(doc, new_grades):
	try:
		doc['scores'] = new_grades
		students.save(doc)
		print doc
		print "------"

	except:
		print "Unexpected error:", sys.exc.info()[0]
		raise

do_it()

