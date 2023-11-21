consumed_unit = 129
life_line = "No"
demand_charge = 70

c = consumed_unit
l = life_line
d = demand_charge

if(c==0 or c==1):
    print("Consumed Unit:" , c)
else:
    print("Consumed Units:" , c)

print("Demand Charge:" , d)

if(l=="Yes"):
    print("Life Line: Yes")
else:
    print("Life Line: No")

if(c<0):
    print("Error Entry")
else:
    if(l=="Yes" and c>=0 and c<=50):
        print("Bill:" , (4.14*c) + ((4.14*c)*0.05) + d , "BDT")
    elif(0<=c and c<=75):
        print("Bill:" , (4.62*c) + ((4.62*c)*0.05) + d , "BDT")
    elif(75<c and c<=200):
        print("Bill:" , (6.31*c + 6.31*c*0.05 + d) , "BDT")
    elif(201<=c and c<=300):
        print("Bill:" , (6.62*c + 6.62*c*0.05 + d) , "BDT")
    elif(300<c and c<=400):
        print("Bill:" , (6.99*c + 6.99*c*0.05 + d) , "BDT")
    elif(400<c and c<=600):
        print("Bill:" , (10.96*c + 10.96*c*0.05 + d) , "BDT")
    else:
        print("Bill:" , (12.63*c + 12.63*c*0.05 + d) , "BDT")