import view

def parse_file(path):
    stri = ''
    data = open(path, 'r', encoding= 'UTF-8')
    for line in data:
        stri += line 
        # print(line)
    data.close()
    return stri


def convert_parse(string:str):
    string = string.split('\n')
    for i in range(len(string)):
        string[i] = string[i].split(';')
    return string

journal = convert_parse(parse_file(view.class_list()))
# print(view.subject_list(journal))

view.answer_lesson(view.subject_list(journal))
