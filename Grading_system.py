# 0 - 39 - F9
# 40 - 44 - P8
# 45 - 49 - P7
# 50 - 54 - C6
# 55 - 59 - C5
# 60 - 64 - C4
# 65 - 74 - C3
# 75 - 79 - D2
# 80 - 100 -D1

# Homework: Take a list of student marks and print the grades next to the marks
# marks = [45, 75, 67]
# prints out 45: P8 75: D2, 67: C3
input_mark = input('Enter students mark: ')
std_mark = int(input_mark)
if std_mark >= 0 and std_mark <= 39 : 
    print('F9')
if std_mark >= 40 and std_mark <= 44:
    print('P8')
if std_mark >= 45 and std_mark <= 49:
    print('P7')
if std_mark >= 50 and std_mark <= 54:
     print('C6')
if std_mark >= 55 and std_mark <= 59:
    print('C5')
if std_mark >= 60 and std_mark <= 64:
    print('C4')
if std_mark >= 65 and std_mark <= 74:
    print('C3')
if std_mark >= 75 and std_mark <= 79:
    print('D2')
if std_mark >= 80 and std_mark <= 100:
    print('D1')