score = int(input('Enter your score: '))

# NESTED CONDITIONAL
validated_and = score >= 0 and score <= 100

if not validated_and:
    print('Invalid Entry')
else:
    if (score >= 60):
        print('you passed')
    else:
        if (score < 20):
            print('you failed miserably')
        else:
            print('you failed')

'''
❯ py cond.py
Enter your score: 10
you failed miserably
❯ py cond.py
Enter your score: 30
you failed
❯ py cond.py
Enter your score: 60
you passed
❯ py cond.py
Enter your score: 100
you passed
❯ py cond.py
Enter your score: 1000
Invalid Entry
❯ py cond.py
Enter your score: -20
Invalid Entry
'''

# ELIF
if (score < 0):
    print('invalid, too low')
elif (score > 100):
    print('invalid, too high')
elif (score > 60):
    print('you passed')
elif (score < 20):
    print('you failed miserably')
else:
    print('you failed')
