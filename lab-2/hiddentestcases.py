import sys
from interface_template import StudentRecord
from interface_template import EntityArray 
from interface_template import LinkedList
from interface_template import read_input_file

failed_tests = 0

def test1():
    entity_name = "Commerce"
    entity = ""
    for i in EntityArray:
        if i.name == entity_name:
            entity = i
            break

    ite = entity.get_iterator()
    student = ""
    
    while(ite != None):
        if ite.get_element().studentName == "EthanMartinez":
            student = ite.get_element()
            break
        ite = ite.get_next()

    assert student.studentName == "EthanMartinez", "Student EthanMartinez is not present in the Commerce Entity"

def test2():
    entity_name = "MBA"
    entity = ""
    for i in EntityArray:
        if i.name == entity_name:
            entity = i
            break

    ite = entity.get_iterator()
    student = ""
    
    while(ite != None):
        if ite.get_element().studentName == "MichaelWilson":
            student = ite.get_element()
            break
        ite = ite.get_next()

    assert student.studentName == "MichaelWilson", "Student MichaelWilson is not present in the MBA Entity"

def test3():
    entity_name = "DSA"
    entity = ""
    for i in EntityArray:
        if i.name == entity_name:
            entity = i
            break

    ite = entity.get_iterator()
    size = 0
    
    while(ite != None):
        size += 1
        ite = ite.get_next()

    assert size == 69, "Incorrect count of records in DSA course"



def test4():
    entity_name = "Programming"
    entity = ""
    for i in EntityArray:
        if i.name == entity_name:
            entity = i
            break

    ite = entity.get_iterator()
    size = 0
    
    while(ite != None):
        size += 1
        ite = ite.get_next()

    assert size == 87, "Incorrect count of records in Programming Club"

def test5():
    entity_name = "Networking"
    entity = ""
    studentname = "NoahHernandez"
    for i in EntityArray:
        if i.name == entity_name:
            entity = i
            break

    entity.delete_student(studentname)
    ite = entity.get_iterator()
    
    if_exists = 0
    while(ite != None):
        if ite.get_element().studentName == studentname:
            if_exists = 1
            break
        ite = ite.get_next()

    assert if_exists == 0, "Record still exists, Delete function not working!"

def test6():
    entity_name = "Econometrics"
    entity = ""
    studentname = "ShaheenClark"
    studentroll = "B22ECON1721"
    student = StudentRecord()
    student.studentName = studentname
    student.rollNumber = studentroll

    for i in EntityArray:
        if i.name == entity_name:
            entity = i
            break

    entity.add_student(student)
    ite = entity.get_iterator()
    
    if_exists = 0
    while(ite != None):
        if ite.get_element().studentName == studentname:
            if_exists = 1
            break
        ite = ite.get_next()

    assert if_exists == 1, "Record is not added, Add Student Record function not working!"

def test7():
    entity_name = "Commerce"
    entity = ""
    studentname = "WilliamJones"
    for i in EntityArray:
        if i.name == entity_name:
            entity = i
            break

    entity.delete_student(studentname)
    ite = entity.get_iterator()
    
    if_exists = 0
    while(ite != None):
        if ite.get_element().studentName == studentname:
            if_exists = 1
            break
        ite = ite.get_next()

    assert if_exists == 0, "Record still exists, Delete function not working!"

def test8():
    entity_name = "G6"
    entity = ""
    studentname = "KoshimoDiago"
    studentroll = "B22POLSCI1078"
    student = StudentRecord()
    student.studentName = studentname
    student.rollNumber = studentroll

    for i in EntityArray:
        if i.name == entity_name:
            entity = i
            break

    entity.add_student(student)
    ite = entity.get_iterator()
    
    if_exists = 0
    while(ite != None):
        if ite.get_element().studentName == studentname:
            if_exists = 1
            break
        ite = ite.get_next()

    assert if_exists == 1, "Record is not added, Add Student Record function not working!"

def test9():
    entity_name = "Thermodynamics"
    entity = ""
    for i in EntityArray:
        if i.name == entity_name:
            entity = i
            break

    ite = entity.get_iterator()
    size = 0
    
    while(ite != None):
        size += 1
        ite = ite.get_next()

    assert size == 2, "Incorrect count of records in Thermodynamics course"

def test10():
    entity_name = "Finance"
    entity = ""
    for i in EntityArray:
        if i.name == entity_name:
            entity = i
            break

    ite = entity.get_iterator()
    size = 0
    
    while(ite != None):
        size += 1
        ite = ite.get_next()

    assert size == 13, "Incorrect count of records in Finance course"

def test11():
    entity_name = "English Literature"
    entity = ""
    for i in EntityArray:
        if i.name == entity_name:
            entity = i
            break

    ite = entity.get_iterator()
    size = 0
    
    while(ite != None):
        size += 1
        ite = ite.get_next()

    assert size == 6, "Incorrect count of records in English Literature course"

def test12():
    entity_name = "G1"
    entity = ""
    studentname = "JamesWilson"
    studentroll = "B22CHEM1016"

    #if_exists == 1

    student = StudentRecord()
    student.studentName = studentname
    student.rollNumber = studentroll

    for i in EntityArray:
        if i.name == entity_name:
            entity = i
            break

    entity.add_student(student)
    ite = entity.get_iterator()
    
    if_exists = 0
    while(ite != None):
        if ite.get_element().studentName == studentname:
            if_exists = 1
            break
        ite = ite.get_next()

    assert if_exists == 1, "Record already exist"

def test13():
    entity_name = "Commerce"
    entity = ""
    for i in EntityArray:
        if i.name == entity_name:
            entity = i
            break

    ite = entity.get_iterator()
    student = ""
    
    while(ite != None):
        if ite.get_element().studentName == "OliviaTaylor":
            student = ite.get_element()
            break
        ite = ite.get_next()

    assert student.studentName == "OliviaTaylor", "Student OliviaTaylor is not present in the Commerce Entity"

def test14():
    entity_name = "Social Science"
    entity = ""
    studentname = "NoahMartin"
    for i in EntityArray:
        if i.name == entity_name:
            entity = i
            break

    entity.delete_student(studentname)
    ite = entity.get_iterator()
    
    if_exists = 0
    while(ite != None):
        if ite.get_element().studentName == studentname:
            if_exists = 1
            break
        ite = ite.get_next()

    assert if_exists == 0, "Record still exists, Delete function not working!"


# if __name__ == "__main__":
def testcase():

    alltestcase = []
    unit_tests_list = [
        test1, test2, test3, test4, test5, test6,
        test7, test8, test9, test10, test11, test12,
        test13, test14]
    total = len(unit_tests_list)
    try:
        read_input_file("newDetails.txt")
    except:
        print("Could not read Sample Input File! Ensure that the file 'details.txt' is in the folder and try again!")
        sys.exit(1)
        
    for i, test_fn in enumerate(unit_tests_list):
        try:
            test_fn()
            alltestcase.append(1)
        except Exception as e:
            #failed_tests += 1
            alltestcase.append(0)
            #print(f"Unit test #{i+1} failure: {str(e)}")
    print(alltestcase)

    # if failed_tests == 0:
    #     print("All tests have passed successfully!")
    # else:
    #     print(f"{failed_tests} tests failed!")
    #sys.exit(failed_tests)


testcase()