import os
dir = os.path.dirname(__file__)
file_name = input('Enter a class file to grade (i.e. class1 for class1.txt): ')
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
answer_split = answer_key.split(",")
while True:
    real_name = file_name+".txt"
    try:
        file = open(os.path.join(dir, 'Text Files', real_name), 'r')
    except FileNotFoundError:
        print("File cannot be found.")
        file_name = input(
            'Enter a class file to grade (i.e. class1 for class1.txt): ')
    else:
        print(f"Successfully opened {file_name}")
        print()
        print("**** ANALYZING ****")
        students = file.read()
        students = students.split("\n")
        total_lines = len(students)
        invalid = 0
        score_all = []
        for i in range(total_lines):
            line_detail = students[i]
            line_split = line_detail.split(",")
            student_id = line_split[0]
            line_split = line_split[1:]
            length_each_line = len(line_split)
            to_be_removed = []
            if (len(student_id) != 9) or (student_id[0] != "N"):
                print()
                print("Invalid line of data: N# is invalid")
                print(line_detail)
                invalid += 1
                to_be_removed.append(line_detail)
            if not student_id[1:9].isdigit():
                print()
                print("Invalid line of data: N# is invalid")
                print(line_detail)
                invalid += 1
                to_be_removed.append(line_detail)
            if len(line_split) != 26:
                print()
                print("Invalid line of data: does not contain exactly 26 values:")
                print(line_detail)
                invalid += 1
                to_be_removed.append(line_detail)

            score = 0

            if length_each_line == 25:
                for index in range(length_each_line):
                    if line_split[index] == answer_split[index]:
                        score += 4
                    elif not line_split[index]:
                        continue
                    else:
                        score -= 1
                score_all.append(score)

        if invalid == 0:
            print()
            print("No errors found!")
            print()

        for item in to_be_removed:
            students.remove(item)

        print()
        print("**** REPORT ****")
        print()
        print(f"Total valid lines of data: {total_lines-invalid}")
        print(f"Total invalid lines of data: {invalid}")
        print()
        mean_score = sum(score_all)/len(score_all)
        print(f"Mean (average) score: {round(mean_score, 2)}")
        print(f"Highest score: {max(score_all)}")
        print(f"Lowest score: {min(score_all)}")
        print(f"Range f scores: {max(score_all)-min(score_all)}")
        score_all.sort()
        if total_lines % 2 == 1:
            # 7:3,3:1
            median_position = total_lines//2
            print(f"Median score: {score_all[median_position]}")
        elif total_lines % 2 == 0:
            # 8:3+4,4:1+2
            median_position_1 = int((total_lines/2)-1)
            median_position_2 = int((total_lines/2))
            median_score = (
                (score_all[median_position_1])+(score_all[median_position_2]))/2
            print(f"Median score: {round(median_score, 1)}")

        break
