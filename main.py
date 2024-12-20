# def get_applications():
#     applications = []
#     n = int(input("Enter the number of applications: "))
#     for _ in range(n):
#         name = input("Enter the applicant's name: ")
#         years_of_experience = int(input("Enter the years of experience: "))
#         skills = input("Enter the skills (comma-separated): ").split(',')
#         skills = set(skill.strip() for skill in skills)  # Convert to a set of trimmed skills
#         applications.append((name, years_of_experience, skills))
#     return applications

# def shortlist_applications(applications, min_experience, required_skills):
#     shortlisted = []
#     for app in applications:
#         name, years_of_experience, skills = app
#         if years_of_experience >= min_experience and all(skill in skills for skill in required_skills):
#             shortlisted.append(app)
#     return shortlisted

# print("Enter the minimum years of experience required: ")
# min_experience = int(input())
# print("Enter the required skills (comma-separated): ")
# required_skills = input().split(',')
# required_skills = set(skill.strip() for skill in required_skills)  # Convert to a set of trimmed skills

# applications = get_applications()
# shortlisted_apps = shortlist_applications(applications, min_experience, required_skills)

# print("\nShortlisted Applicants:")
# for app in shortlisted_apps:
#  name, years_of_experience, skills = app
#  print(f"Name: {name}, Years of Experience: {years_of_experience}, Skills: {', '.join(skills)}")


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









