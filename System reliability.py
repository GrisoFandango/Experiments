import math
system={}
print("Welcome to the system reliability calculator")
print("We are going to calculate the system reliability with a parallel of 2,3 and 4 systems")
print("Based on your request, we are going to find the best combination of components and costs that suit your needs")
rel = float(input("Please insert the final reliabity you want to achieve: "))
user ="y"
while user == "y":
    
    sys=float(input("Insert system reliability:"))
    cost=float(input("Insert system cost:"))
    system[sys]=cost
    user=input("Do you want to add another component?")


i=1
for key in system.keys():
    print ('system '+str(i)+' = %s, value = %s' % (key, system[key])+"\n")
    i += 1

system2=system
system3=system
system4=system

for key in system.keys():
    
    for key2 in system2.keys():
        
        result=(1-(1-key)*(1-key2))
        
        if float("{0:.2f}".format(result)) == float(rel):
            print("The system "+str(key)+" plus the system "+str(key2)+" give a reliability of: "+str(rel))
            print("The total cost is: " + str(float(system[key])+float(system2[key2]))+" and use 2 components \n\n")

        for key3 in system3.keys():
            result=(1-(1-key)*(1-key2)*(1-key3))
            
                    
            if float("{0:.2f}".format(result)) == float(rel):
                print("The system "+str(key)+" plus the system "+str(key2)+"and "+str(key3)+" give a reliability of: "+str(rel))
                print("The total cost is: " + str(float(system[key])+float(system2[key2])+float(system3[key3]))+"and use 3 components \n\n")

                for key4 in system4.keys():
                    result=(1-(1-key)*(1-key2)*(1-key3)*(1-key4))

                    if float("{0:.2f}".format(result)) == float(rel):
                        print("The system "+str(key)+" plus the system "+str(key2)+"and "+str(key3)+"and "+str(key4)+" give a reliability of: "+str(rel))
                        print("The total cost is: " + str(float(system[key])+float(system2[key2])+float(system3[key3])+float(system4[key4]))+" and use 4 components \n\n")
                
            

                
