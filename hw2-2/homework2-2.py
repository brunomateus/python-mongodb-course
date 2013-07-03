#Write a program in the language of your choice that will remove the grade of
#type "homework" with the lowest score for each student from the dataset that you
#imported in HW 2.1. Since each document is one grade, it should remove one
#document per student.


import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.students
grades = db.grades


def do_it():

    print "Homework2-2"

    query = {'type': 'homework'}
    projection = {}

    try:

        cursor = grades.find(query).sort([('student_id', pymongo.ASCENDING),
                                          ('score',pymongo.ASCENDING)])


    except:
        print "Unexpected error:", sys.exc_info()[0]


    student_id = -1
    for doc in cursor:
        if(student_id != doc['student_id']):
            student_id = doc['student_id']
            grades.remove(doc)
        

do_it()

