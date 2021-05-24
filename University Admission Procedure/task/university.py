# number of students that can be accepted into each department
N = int(input())

departments = {'Biotech': [], 'Chemistry': [], 'Engineering': [], 'Mathematics': [], 'Physics': []}
not_sorted_applicants = {}

file = open('applicants.txt', encoding='utf-8')
not_sorted_applicants = [line.rstrip('\n').split() for line in file]
file.close()

# applicant input
# first name, last name, physics exam, chemistry exam, math exam, cs exam, special exam, first priority, second pr, third pr

# sorting applicants by exam result, first name, last name
physics_applicants = sorted(not_sorted_applicants, key=lambda x: (-max(((float(x[2]) + float(x[4])) / 2), float(x[6])), x[0], x[1]))
chemistry_applicants = sorted(not_sorted_applicants, key=lambda x: (-max(float(x[3]), float(x[6])), x[0], x[1]))
math_applicants = sorted(not_sorted_applicants, key=lambda x: (-max(float(x[4]), float(x[6])), x[0], x[1]))
cs_applicants = sorted(not_sorted_applicants, key=lambda x: (-max(((float(x[5]) + float(x[4])) / 2), float(x[6])), x[0], x[1]))
biotech_applicants = sorted(not_sorted_applicants, key=lambda x: (-max(((float(x[2]) + float(x[3])) / 2), float(x[6])), x[0], x[1]))

# applicants = sorted(not_sorted_applicants, key=lambda x: (-float(x[2]), x[0], x[1]))
not_accepted_applicants = physics_applicants[:]

print("---Physics---")
for student in physics_applicants:
    print(student)
print("---Chemistry---")
for student in chemistry_applicants:
    print(student)
print("---Math---")
for student in math_applicants:
    print(student)
print("---Engineering---")
for student in cs_applicants:
    print(student)
print("---Biotech---")
for student in biotech_applicants:
    print(student)


def applicants_waves(wave):
    global departments
    global not_accepted_applicants
    for depart, students_list in departments.items():
        if depart == 'Biotech':
            subject_list = biotech_applicants
        elif depart == 'Chemistry':
            subject_list = chemistry_applicants
        elif depart == 'Engineering':
            subject_list = cs_applicants
        elif depart == 'Mathematics':
            subject_list = math_applicants
        else:
            subject_list = physics_applicants

        for student1 in subject_list:
            if student1[wave] == depart:
                if len(students_list) < N:
                    students_list.append(student1)
                    not_accepted_applicants.remove(student1)


for i in range(7, 10):
    applicants_waves(i)
    physics_applicants = sorted(not_accepted_applicants, key=lambda x: (-max(((float(x[2]) + float(x[4])) / 2), float(x[6])), x[0], x[1]))
    chemistry_applicants = sorted(not_accepted_applicants, key=lambda x: (-max(float(x[3]), float(x[6])), x[0], x[1]))
    math_applicants = sorted(not_accepted_applicants, key=lambda x: (-max(float(x[4]), float(x[6])), x[0], x[1]))
    cs_applicants = sorted(not_accepted_applicants, key=lambda x: (-max(((float(x[5]) + float(x[4])) / 2), float(x[6])), x[0], x[1]))
    biotech_applicants = sorted(not_accepted_applicants, key=lambda x: (-max(((float(x[2]) + float(x[3])) / 2), float(x[6])), x[0], x[1]))


for dep, students in departments.items():
    file = open(dep.lower() + '.txt', 'w', encoding='utf-8')
    if dep == 'Biotech':
        sorted_students = sorted(students, key=lambda x: (-max(((float(x[2]) + float(x[3])) / 2), float(x[6])), x[0], x[1]))
        for st in sorted_students:
            file.write(st[0] + ' ' + st[1] + ' ' + str(max(((float(st[2]) + float(st[3])) / 2), float(st[6]))) + '\n')
    elif dep == 'Chemistry':
        sorted_students = sorted(students, key=lambda x: (-max(float(x[3]), float(x[6])), x[0], x[1]))
        for st in sorted_students:
            file.write(st[0] + ' ' + st[1] + ' ' + str(max(float(st[3]), float(st[6]))) + '\n')
    elif dep == 'Engineering':
        sorted_students = sorted(students, key=lambda x: (-max(((float(x[5]) + float(x[4])) / 2), float(x[6])), x[0], x[1]))
        for st in sorted_students:
            file.write(st[0] + ' ' + st[1] + ' ' + str(max((float(st[5]) + float(st[4])) / 2, float(st[6]))) + '\n')
    elif dep == 'Mathematics':
        sorted_students = sorted(students, key=lambda x: (-max(float(x[4]), float(x[6])), x[0], x[1]))
        for st in sorted_students:
            file.write(st[0] + ' ' + st[1] + ' ' + str(max(float(st[4]), float(st[6]))) + '\n')
    else:
        sorted_students = sorted(students, key=lambda x: (-max(((float(x[2]) + float(x[4])) / 2), float(x[6])), x[0], x[1]))
        for st in sorted_students:
            file.write(st[0] + ' ' + st[1] + ' ' + str(max(((float(st[2]) + float(st[4])) / 2), float(st[6]))) + '\n')
    file.close()
