def applicationinfo():
    applications=[]
    n =int(input("Present number of application : "))
    for _ in range(n):
        name =input("Enter Applicant's name : ")
        age=int(input("Enter age : "))
        experience =int(input("Enter your work experience : "))
        skills=input("Enter the skills :").split(',')
        skills=set(skill.strip() for skill in skills)
        applications.append((name,age,experience,skills))
    return applications

def shortlistapplication(application,reqage,reqexperience,reqskills):
    shortlisting=[]
    for app in application : 
        name,age, experience, skills =app
        if age<=reqage and experience>=reqexperience and all(skill in skills for skill in reqskills):
            shortlisting.append(app)
    return shortlisting


reqexperience = int(input("Enter the minimum years of experience required: "))
reqage = int(input("Enter the maximum age required : "))
reqskills = input("Enter the required skills (comma-separated): ").split(',')
reqskills = set(skill.strip() for skill in reqskills)  

applications = applicationinfo()
shortlisted_app = shortlistapplication(applications, reqage, reqexperience, reqskills)

print("\nShortlisted Applicants:")
for app in shortlisted_app:
 name, age, experience, skills, = app
 print(f"Name: {name}, Age: {reqage}, Work Experience: {reqexperience}, Skills: {', '.join(skills)}")









