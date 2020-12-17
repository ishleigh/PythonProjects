#hospital patient registration
#enter the names of the patients
#schedule appointments


PatientNames= [] #list to store patients names, now its empty
while True:
    print('Enter the name of patient ' + str(len(PatientNames) + 1) +
      ' (Or enter nothing to stop.):') #len(PatientNames) counts the number of list elements
    name = input() #get the name as input
    if name == '': #if name is empty exit the while
        break
    PatientNames = PatientNames + [name]  # list concatenation
print('The Patient names are:')
for name in PatientNames: #name is an element in catNames
    print('***  ' + name)


#scheduling appointments for each patient
#enter time for each patient and print
#create a list with appointment time
#schedule= ['10am','10.30am','11am']
#enter schedules equal to number of patients...
time=input()


for i in range(len(PatientNames)):
    print('Index ' + str(i) + ' in PatientNames is: ' + PatientNames[i])
len(schedule)

for i in range(len(PatientNames))
    print
