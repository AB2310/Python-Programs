class Course:
    def __init__(self, coureseName, duration):
        self.courseName = coureseName
        self.duration = duration
        
    def printCourse(self):
        print(self.courseName, self.duration)
    
class Subject(Course):
    def __init__(self, courseName, duration ):
        Course.__init__(self, courseName, duration )
        super().__init__(courseName, duration )
        
        
x = Subject("MCA", "2 yrs")
x.printCourse()