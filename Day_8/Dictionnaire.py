#Exercices: Jour 8
#1/
dog = {}
#2/
dog = {'name':'Jojo', 'color':'maron', 'breed':'Bouledogue', 'legs':'court', 'age':5}
#3/
student = {'first_name':'Toto', 'last_name':'ABALO', 'gender':'Masculin', 'age':'15',
'marital_status':'single', 'skills':{'informatique','Maths','Physique','Anglais','ECM'}, 'country':'Togo', 'city':'Lomé', 'address':'AGOE'}
#4/
print(len(student))
#5/
skills = student['skills']
print(skills)          
print(type(skills))    
#6/
student['skills'].append('CSS')      
student['skills'].extend(['React'])   
print(student['skills'])  
#7/
keys_list = list(student.keys())
print(keys_list)  

#8/
values_list = list(student.values())
print(values_list)  

#9/
items_list = list(student.items())
print(items_list)  

#10/
del student['age']  
#11/
del student  
