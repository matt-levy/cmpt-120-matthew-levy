from person import Person
from course import Course

class Student(Person):

    def __init__(self, first_name, last_name, major, courses: list[Course] = []):
        self.major = major
        self.courses = courses
        super().__init__(first_name, last_name)
    
    def change_major(self, new_major):
            self.major = new_major

    def get_credits(self):
        total_credits = 0
        for course in self.courses:
            total_credits += course.credits
        return total_credits


    def get_gpa(self):
        grade_map = {
        "A"  : 4.0,
        "A-" : 3.7,
        "B+" : 3.3,
        "B"  : 3.0,
        "B-" : 2.7,
        "C+" : 2.3,
        "C"  : 2.0,
        "C-" : 1.7,
        "D+" : 1.3,
        "D"  : 1.0,
        "F"  : 0.0
        }

        total_credits = self.get_credits()
        total_points = 0

        for course in self.courses:
            number_grade = grade_map[course.grade] * course.credits
            total_points += number_grade

        return total_points/total_credits

    def add_course(self, course):
        self.courses.append(course)