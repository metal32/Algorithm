def convertGrade(grade):
    if grade=="F":
        return 0
    else:
        return 4-(ord(grade)-ord("A"))
def getGrade():
    semester_info=[]
    more_grades=True
    empty_string=""
    while more_grades:
        course_grade=raw_input("Enter grade ( hit enter when you are done): ")
        if course_grade in ("A","B","C","D","E","F"):
            credit=int(input("Enter number of credits: "))
            semester_info.append([credit,course_grade])
        else:
            if course_grade==empty_string:
                more_grades=False
            else:
                course_grade=raw_input("Invalid entry, Enter grade between A-F: ")   
    return semester_info

def calculation(sem_grades_info,cumm_gpa_info):
    sem_quality_points=0
    sem_credits=0
    current_cumm_gpa, total_credits=cumm_gpa_info
    for k in range(len(sem_grades_info)):
                   num_credits, letter_grade=sem_grades_info[k]
                   sem_quality_points=sem_quality_points+num_credits*convertGrade(letter_grade)
                   sem_credits=sem_credits+num_credits
    sem_CGPA=float(sem_quality_points)/sem_credits
    new_cumm_gpa=(current_cumm_gpa*total_credits+sem_quality_points)/(total_credits+sem_credits)
    return (sem_CGPA,new_cumm_gpa)

print "This program calulates your semester GPA and cummulative GPA "
total_credits=int(input("Enter the total earned credits till now: "))
cumm_gpa=float(input("Enter current cummulative GPA: "))
cumm_gpa_info=(cumm_gpa,total_credits)
print ''
semester_grade=getGrade()
semester_gpa, cumm_gpa=calculation(semester_grade,cumm_gpa_info)
print "Your Semester GPA ",format(semester_gpa,".2f")
print "Your Cummulative GPA ",format(cumm_gpa,".2f")





