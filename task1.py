stu_marks = {'Alice':85,'Sam':79,'David':87,'Rony':67}

try:
    name = str(input('Enter the student\'s name:'))
    print('{}\'s marks: {}'.format(name,stu_marks[name]))
except:
    print('Student not found.')