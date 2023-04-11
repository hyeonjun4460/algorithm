a = 7

if a == 7:
    print('lucky')

# and
if 0 < a < 10:
    print('yes')
if a > 0 and a < 10:
    print('yes')

a = -1
# else
if a > 10:
    print('양수')
else:
    print('음수')

# elif
a = 60
if a >= 90:
    print('A')
elif 80 <= a < 90:
    print('B')
elif 70 < a < 80:
    print('C')
else:
    print('FAIL')