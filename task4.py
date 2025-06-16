
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
        
    def __str__(self):
        self.all_grades = [self.grade for self.grades_list in self.grades.values() for self.grade in self.grades_list]
        self.average = sum(self.all_grades) / len(self.all_grades) if self.all_grades else 0
        self.str_courses_in_progress = (', '.join(self.courses_in_progress)) if len(self.courses_in_progress) > 0 else 'нет'
        self.str_finished_courses = (', '.join(self.finished_courses)) if len(self.finished_courses) > 0 else 'нет'
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.average} \nКурсы в процессе изучения: {self.str_courses_in_progress} \nЗавершенные курсы: {self.str_finished_courses}'

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

    def __str__(self):
        self.all_grades = [self.grade for self.grades_list in self.grades.values() for self.grade in self.grades_list]
        self.average = sum(self.all_grades) / len(self.all_grades) if self.all_grades else 0
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average}'

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

student_1 = Student('Алёхина', 'Ольга', 'Ж')
student_1.courses_in_progress += ['Python', 'C++']
student_1.finished_courses += ['Введение']

student_2 = Student('Коля', 'Петухов', 'М')
student_2.courses_in_progress += ['Python', 'Java']
student_2.finished_courses += ['Введение']
 
lecturer_1 = Lecturer('Билл', 'Гейтс')
lecturer_1.courses_attached += ['Python', 'C++']

lecturer_2 = Lecturer('Дональд', 'Трамп')
lecturer_2.courses_attached += ['Python', 'Java']

reviewer_1 = Reviewer('Павел', 'Дуров')
reviewer_1.courses_attached += ['Python', 'C++']
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'C++', 8)
reviewer_1.rate_hw(student_2, 'Python', 2)
reviewer_1.rate_hw(student_2, 'Java', 4)

reviewer_2 = Reviewer('Илон', 'Маск')
reviewer_2.courses_attached += ['Python', 'Java']
reviewer_2.rate_hw(student_1, 'Python', 5)
reviewer_2.rate_hw(student_1, 'C++', 3)
reviewer_2.rate_hw(student_2, 'Python', 7)
reviewer_2.rate_hw(student_2, 'Java', 8)

student_1.rate_lecture(lecturer_1, 'Python', 5)
student_1.rate_lecture(lecturer_1, 'C++', 10)
student_1.rate_lecture(lecturer_2, 'Python', 2)
student_1.rate_lecture(lecturer_2, 'Java', 4)

student_2.rate_lecture(lecturer_1, 'Python', 2)
student_2.rate_lecture(lecturer_1, 'C++', 3)
student_2.rate_lecture(lecturer_2, 'Python', 7)
student_2.rate_lecture(lecturer_2, 'Java', 8)

def average_rate_for_students(students, course):
    list_rate = []
    for i in students:
        if isinstance(i, Student):
            if course in i.grades:
                list_rate.append(i.grades[course])
            else:
                None
        else:
            raise ValueError
    
    num_list = []
    for k in list_rate:
        for j in k:
            num_list.append(j)
    average_rate = sum(num_list)/len(num_list)       
    return f'Средняя оценка по домашним заданиям на курсе {course} составляет {average_rate} баллов'

def average_rate_for_lectors(lecturers, course):
    list_rate = []
    for i in lecturers:
        if isinstance(i, Lecturer):
            if course in i.grades:
                list_rate.append(i.grades[course])
            else:
                None
        else:
            raise ValueError
        
    num_list = []
    for k in list_rate:
        for j in k:
            num_list.append(j)
    average_rate = sum(num_list)/len(num_list)       
    return f'Средняя оценка лекций на курсе {course} составляет {average_rate} баллов'
 
stud_list = [student_1, student_2]
lecturers_list = [lecturer_1, lecturer_2]


print(average_rate_for_students(stud_list, 'C++'))
print(average_rate_for_lectors(lecturers_list, 'Python'))