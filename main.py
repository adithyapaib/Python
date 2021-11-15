#Given a age of a  Person  and gender determine the Eligibilty for marraige.

age  = int(input("Enter the age "))
gender = input("Enter the gender (B/G): ")
if gender== 'G' and age >=18:
     print("The girl is eligiblie for marraige")
elif gender == 'B' and age>=21 :
    print("The boys is eligible for marraige")
else:
    print("Child marraige is Illegal")

