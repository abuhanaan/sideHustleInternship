def checkPassMarks():

    lst = []
    population = int(input('How many students are in the class: '))
    for student in range(population):
        score = int(input('Enter student score '))
        lst.append(score)
    total_score = sum(lst)
    average_score = total_score/population
    print("Sum of scores of students in the class is :", total_score)
    print("Population of student is :", population)
    print("Average score is :", average_score)

    min_score = 0

    for i in range(len(lst)):
        if average_score > 60:
            min_score = average_score
        else:
            min_score = 60
        if lst[i] > min_score:
            print("Student {} passed - his score is {} and pass mark is {}".format(i+1, lst[i], min_score))
        else:
            print("Student {} failed - his score is {} and pass mark is {}".format(i+1, lst[i], min_score))

checkPassMarks()
