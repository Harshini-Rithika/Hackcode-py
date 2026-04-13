if __name__ == '__main__':
    records=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    scores=[record[1] for record in records]
    second_lowest_scores=sorted(list(set(scores)))[1]
    
    second_lowest_students=[record[0] for record in records if record[1]
    ==second_lowest_scores]
    for student in sorted(second_lowest_students):
        print(student)
        
