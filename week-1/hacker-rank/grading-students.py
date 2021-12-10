def gradingStudents(grades):
    # Write your code here
    new_grade=[]
    for i in range(len(grades)):
        x=(grades[i]//5)
        y=x*5
        new_grade.append(y+5) if grades[i]-y>=3 and grades[i]>=38 else new_grade.append(grades[i])
        
    return new_grade
