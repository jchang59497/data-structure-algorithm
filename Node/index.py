class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        

class City:
    def __init__(self, name, state, pop):
        self.name = name
        self.state = state
        self.pop = pop
    

class Classroom:
    def __init__(self)
        self.teacher = ''
        self.num = 0
        self.studentlist = []
    def insert_student(self, student) 
        self.studentlist.append(student)

class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.chapters = []
    def insert_chapter(self,chapter)
        self.chapters.append(chapter)

        
class Chapter:
    def __init__(self, name, page_num):
        self.name = name
        self.page_num = page_num

class Session:
    def __init__(self, day, subject):
        self.day = day
        self.subject = subject
        self.nextSession = None
        
    def changeTime(self, day):
        self.day = day
        
    def addSession(self,nextSession):
        self.nextSession = nextSession
        
    def emptyNextSession(self):
        self.nextSession = None