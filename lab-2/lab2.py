import csv
EntityArray = []
Students = []

class StudentRecord:
    def __init__(self):
        self.studentName = ""
        self.rollNumber = ""

    def get_studentName(self):
        return self.studentName

    def set_studentName(self, name):
        self.studentName = name

    def get_rollNumber(self):
        return self.rollNumber

    def set_rollNumber(self, rollnum):
        self.rollNumber = rollnum


class Node:
    def __init__(self):
        self.next = None
        self.element = None

    def get_next(self):
        return self.next

    def get_element(self):
        return self.element

    def set_next(self, value):
        self.next = value

    def set_element(self, student):
        self.element = student


class Entity:
    def __init__(self):
        self.name = ""
        self.iterator = None

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_iterator(self):
        return self.iterator

    def set_iterator(self, iter):
        self.iterator = iter

class LinkedList(Entity):
    def add_student(self, Student : StudentRecord):
        newNode = Node()
        newNode.set_element(Student)
        it = self.get_iterator()
        # print(self.get_iterator())
        # print(self)
        if it is None:
            self.set_iterator(newNode)
            # print(self.get_iterator())
            # print(self)
            # print(self.name)
            return
        while it.get_next() is not None:
            it = it.get_next()
        it.set_next(newNode)
        return
    def delete_student(self, studentname: str):
        it = self.get_iterator()
        if it.get_element().get_studentName() == studentname:
            self.set_iterator(it.get_next())
            del it
            return
        
        
        while it.get_next() is not None:
            previous = it
            it = it.get_next()
            if it.get_element().get_studentName() == studentname:
                previous.set_next(it.get_next())
                del it
                return
            
        

def read_input_file(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file,)
        # print(csv_reader.__next__()[0].rsplit(' ', 1))
        for line in csv_reader:
            newStudent = StudentRecord()
            
            newStudent.set_studentName(line[0])
            
            newStudent.set_rollNumber(line[1])
            Students.append(newStudent)

            arr_entities = []
            for i in range(len(line)):
                if (i > 1):
                    mod_str = line[i].replace('[','')
                    mod_str = mod_str.replace(']','')
                    arr_entities.append(mod_str)

            for entity in arr_entities:
                checklist = list(filter(lambda i: EntityArray[i].get_name() == entity, range(len(EntityArray)) ))
                if(len(checklist) == 0):
                    
                    newEntity = LinkedList()
                    newEntity.set_name(entity)
                    newEntity.add_student(newStudent)
                    EntityArray.append(newEntity)
                    
                else:
                    iter = checklist[0]
                    EntityArray[iter].add_student(newStudent)
                    
                    

                
                    

            
    
