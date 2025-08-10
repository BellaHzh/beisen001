# Exercise: Write a program that reads the contents of scores.txt and then calculates and prints the average score.
import os

# find script dir
dir = os.path.dirname(__file__)

file = open(os.path.join(dir, 'Text Files', 'scores.txt'), 'r')
scores = file.read()
scores = scores.split(',')
score_total = 0
for score in scores:
    try:
        score_total += int(score)
    except TypeError:
        print('oops type error... skipping...')
    except ValueError:
        print('oops value error... skipping...', score)
total_number = len(scores)
average = score_total/total_number
print(f"The average score is {average}")
