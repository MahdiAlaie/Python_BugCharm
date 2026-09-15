StudentsGrades = { 
    "Ali": [18, 19, 17, 18],
    "Sara": [20, 15, 12, 14],
    "Reza": [10, 9, 11, 12],
    "Mina":[18,19,20,19]
        }
avrrage=0
StudentsGradesAvrrage={

}
StudentStatus={

}

for name , grade in StudentsGrades.items():
    for i in grade:
        avrrage+=i
        StudentsGradesAvrrage[name]= avrrage/len(grade)
    avrrage=0

for key , av in StudentsGradesAvrrage.items():
    if av >= 17:
        StudentStatus[key]= {
            "avrage":av,
            "status":"Excelent"}
    elif 12<av<17:
      StudentStatus[key]= {
            "avrage":av,
            "status":"Normal"}  
    elif av < 12:
         StudentStatus[key]= {
            "avrage":av,
            "status":"Conditional"} 
print(StudentStatus)