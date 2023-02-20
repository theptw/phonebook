

def class_list():
    pathA = 'seminars.py\elec_journal.py\семьА.txt'
    pathB = 'seminars.py\elec_journal.py\семьБ.txt'
    pathC = 'seminars.py\elec_journal.py\семьС.txt'
    clas_lst = ['7a',
                '7b',
                '7c']
    print('Выберите класс')
    for i in range(len(clas_lst)):
        print(f'    {i+1}. {clas_lst[i]}')
    clas = int(input('Введите номер класса: '))
    if clas == 1:
        return pathA
    elif clas == 2:
        return pathB
    elif clas == 3:
        return pathC
    else:
        return print('Такого класса нет')
    
def subject_list(journal):
    name_and_grades = []
    subject = ['Математика', 
               'Русский',
               'Английский']
    print('Выберите предмет')
    for i in range(len(subject)):
        print(f'    {i+1}. {subject[i]}')
    subject_inp = int(input('Введите номер предмета: '))
    print(journal[subject_inp - 1][0]) # print subject
    for i in range(1, len(journal[subject_inp - 1])):
        # print(journal[subject_inp - 1][i]) # print name and grades
        name_and_grades.append(journal[subject_inp - 1][i])
    return name_and_grades

def answer_lesson(list):
    name = ''
    for i in range(len(list)):
        print(f'{i+1}. {list[i]}')

    student_id = int(input('Кто будет отвечать? Введите id ученика: '))
    for i in range(len(list[student_id - 1])):
        if not list[student_id - 1][i].isdigit():
            name += list[student_id - 1][i]
    grade = input(f'Отвечает {name}\n На какую оценку ответил ученик? ')
    list[student_id - 1] += ' ' + grade
    print(list)


    

