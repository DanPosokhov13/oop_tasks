from statistics import mean

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def for_average_grade(self):
        self.all_grades = [self.grade for self.grades_list in [self.grades.values()] for self.grade in self.grades_list]
        self.average = sum(self.all_grades) / len(self.all_grades) if self.all_grades else 0
        return self.average

    @classmethod
    def check_grades(cls, other):
        if not isinstance(other, Student):
            return f'{other} не существует'
        return other.for_average_grade()
        
    
    def __lt__(self, other):
        oth = self.check_grades(other)
        return self.for_average_grade() < oth
    
    def __eq__(self, other):
        oth = self.check_grades(other)
        return self.for_average_grade() == oth
    
    def __gt__(self, other):
        oth = self.check_grades(other)
        return self.for_average_grade() > oth
    
    
    def __str__(self):
        self.average_grade = mean(self.grades.values()) if len(self.grades) > 0 else 'нет'
        self.str_courses_in_progress = (', '.join(self.courses_in_progress)) if len(self.courses_in_progress) > 0 else 'нет'
        self.str_finished_courses = (', '.join(self.finished_courses)) if len(self.finished_courses) > 0 else 'нет'
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.average_grade} \nКурсы в процессе изучения: {self.str_courses_in_progress} \nЗавершенные курсы: {self.str_finished_courses}'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def for_average_grade(self):
        self.all_grades = [self.grade for self.grades_list in [self.grades.values()] for self.grade in self.grades_list]
        self.average = sum(self.all_grades) / len(self.all_grades) if self.all_grades else 0
        return self.average
    
    @classmethod
    def check_grades(cls, other):
        if not isinstance(other, Lecturer):
            return f'{other} не существует'
        return other.for_average_grade()       
    
    def __lt__(self, other):
        oth = self.check_grades(other)
        return self.for_average_grade() < oth
    
    def __eq__(self, other):
        oth = self.check_grades(other)
        return self.for_average_grade() == oth
    
    def __gt__(self, other):
        oth = self.check_grades(other)
        return self.for_average_grade() > oth

    def __str__(self):
        self.average_grade = mean(self.grades.values()) if len(self.grades) > 0 else 'нет'
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_grade}'

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'
 
lecturer = Lecturer('Иван', 'Иванов')
lecturer_1 = Lecturer('Илон', 'Маск')

reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')
student_1 = Student('Вася', 'Акулов', 'М')

student.grades.update({'Python': 5, 'Java': 10})
student_1.grades.update({'Python': 7, 'Java': 8})
lecturer.grades.update({'Python': 5, 'Java': 10})
#student.finished_courses += ['Введение']
student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student)
print(lecturer)
print(reviewer)

print(student.for_average_grade())

print(student_1 < student)  
print(student_1 == student) 
print(student_1 > student) 
print(lecturer_1 < lecturer) 
print(lecturer_1 == lecturer) 
print(lecturer_1 > lecturer) 