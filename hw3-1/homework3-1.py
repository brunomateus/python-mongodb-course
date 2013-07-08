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
    projection = {'_id': 0, 'scores.type': 0}

    try:

        cursor = students.find(query, projection).sort([('_id', pymongo.ASCENDING)])


    except:
        print "Unexpected error:", sys.exc_info()[0]


    for doc in cursor:
        print doc      
        print "1111111"
        new_grades = remove_lowest_grade(doc['scores'])
        update_grades(doc, new_grades)
        print doc      


def compare(grade1, grade2):
    if grade1['score'] > grade2['score']:
        return -1
    else: 
        if grade1['score'] == grade2['score']:
            return 0
        else:
            return 1



def remove_lowest_grade(grades):
    grades.sort(cmp=compare)   
    grades.pop()
    print grades
    print "22222"
    return grades


def update_grades(doc, new_grades):
    try:
        doc['scores'] = new_grades
        print "---"
        print doc
        print "***"
        students.save(doc)

    except:
        print "Unexpected error:", sys.exc.info()[0]
        raise

do_it()

