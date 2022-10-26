if __name__ == '__main__':
    final_list = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        final_list.append([name, score])

    sorted_score = sorted(list(set([x[1] for x in final_list])))
    second_lowest = sorted_score[1]

    low_final_list = []
    for student in final_list:
        if second_lowest == student[1]:
            low_final_list.append(student[0])

    for student in sorted(low_final_list):
        print(student)  
