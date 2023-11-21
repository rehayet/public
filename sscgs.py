print(" ")
print("-----------------------------------------------------------------------------------------")
print("  Subject Name                                    Marks         Grade       Grade Point")
print("-----------------------------------------------------------------------------------------")
bangla_1st_paper = 62
bangla_2nd_paper = 62
english_1st_paper = 62
english_2nd_paper = 62
general_math = 80
higher_math = 50
higher_math_practical = 19
biology = 44
biology_practical = 19
physics = 75
physics_practical = 18
chemistry = 44
chemistry_practical = 18
Islamic_Religion = 72
social_science = 72
information_and_communications_technology = 80
optional_subject = "Biology"     # Optional: Biology or Higher Math

b1st = bangla_1st_paper
if(0>b1st or b1st>100):
    print("  Bangla 1st Paper:                              Invalid         -               -")
else:
    
    if(0<=b1st<33):
        print("  Bangla 1st Paper:""                               ",b1st,"           ""F""               ""0")  
    elif(33<=b1st<40):
        print("  Bangla 1st Paper:""                               ",b1st,"           ""D""               ""1")
    elif(40<=b1st<50):
        print("  Bangla 1st Paper:""                               ",b1st,"           ""C""               ""2")
    elif(50<=b1st<60):
        print("  Bangla 1st Paper:""                               ",b1st,"           ""B""               ""3")
    elif(60<=b1st<70):
        print("  Bangla 1st Paper:""                               ",b1st,"           ""A-""              ""3.5")
    elif(70<=b1st<80):
        print("  Bangla 1st Paper:""                               ",b1st,"           ""A""               ""4")
    elif(b1st==100):
        print("  Bangla 1st Paper:""                               ",b1st,"          ""A+""              ""5")
    else:
        print("  Bangla 1st Paper:""                               ",b1st,"           ""A+""              ""5")
print("-----------------------------------------------------------------------------------------")


b2nd = bangla_2nd_paper
if(0>b2nd or b2nd>100):
    print("  Bangla 2nd Paper:                              Invalid         -               -")
else:
    
    if(0<=b2nd<33):
        print("  Bangla 2nd Paper:""                               ",b2nd,"           ""F""               ""0")  
    elif(33<=b2nd<40):
        print("  Bangla 2nd Paper:""                               ",b2nd,"           ""D""               ""1")
    elif(40<=b2nd<50):
        print("  Bangla 2nd Paper:""                               ",b2nd,"           ""C""               ""2")
    elif(50<=b2nd<60):
        print("  Bangla 2nd Paper:""                               ",b2nd,"           ""B""               ""3")
    elif(60<=b2nd<70):
        print("  Bangla 2nd Paper:""                               ",b2nd,"           ""A-""              ""3.5")
    elif(70<=b2nd<80):
        print("  Bangla 2nd Paper:""                               ",b2nd,"           ""A""               ""4")
    elif(b2nd==100):
        print("  Bangla 2nd Paper:""                               ",b2nd,"          ""A+""              ""5")
    else:
        print("  Bangla 2nd Paper:""                               ",b2nd,"           ""A+""              ""5")

b1 = bangla_1st_paper
b2 = bangla_2nd_paper
if(b1<0 or b1>100 or b2<0 or b2>100):
    ban = "Invalid"
else:
    if(b1<33 or b2<33):
        ban = 0
    else:
        ban = ((b1+b2)/2)
        if(ban==0):
          ban = 0
        else:
         if(33<=ban and ban<40):
          ban = 1
         elif(40<=ban<50):
          ban = 2
         elif(50<=ban<60):
          ban = 3
         elif(60<=ban<70):
          ban = 3.5
         elif(70<=ban<80):
          ban = 4
         else:
             ban = 5

print("-----------------------------------------------------------------------------------------")
e1st = english_1st_paper
if(0>e1st or e1st>100):
    print("  English 1st Paper:                             Invalid         -               -")
else:
    
    if(0<=e1st<33):
        print("  English 1st Paper:""                              ",e1st,"           ""F""               ""0")  
    elif(33<=e1st<40):
        print("  English 1st Paper:""                              ",e1st,"           ""D""               ""1")
    elif(40<=e1st<50):
        print("  English 1st Paper:""                              ",e1st,"           ""C""               ""2")
    elif(50<=e1st<60):
        print("  English 1st Paper:""                              ",e1st,"           ""B""               ""3")
    elif(60<=e1st<70):
        print("  English 1st Paper:""                              ",e1st,"           ""A-""              ""3.5")
    elif(70<=e1st<80):
        print("  English 1st Paper:""                              ",e1st,"           ""A""               ""4")
    elif(e1st==100):
        print("  English 1st Paper:""                              ",e1st,"          ""A+""              ""5")
    else:
        print("  English 1st Paper:""                              ",e1st,"           ""A+""              ""5")

print("-----------------------------------------------------------------------------------------")

e2nd = english_2nd_paper
if(0>e2nd or e2nd>100):
    print("  English 2nd Paper:                             Invalid         -               -")
else:
    
    if(0<=e2nd<33):
        print("  English 2nd Paper:""                              ",e2nd,"           ""F""               ""0")  
    elif(33<=e2nd<40): 
        print("  English 2nd Paper:""                              ",e2nd,"           ""D""               ""1")
    elif(40<=e2nd<50):
        print("  English 2nd Paper:""                              ",e2nd,"           ""C""               ""2")
    elif(50<=e2nd<60):
        print("  English 2nd Paper:""                              ",e2nd,"           ""B""               ""3")
    elif(60<=e2nd<70):
        print("  English 2nd Paper:""                              ",e2nd,"           ""A-""              ""3.5")
    elif(70<=e2nd<80):
        print("  English 2nd Paper:""                              ",e2nd,"           ""A""               ""4")
    elif(e2nd==100):
        print("  English 2nd Paper:""                              ",e2nd,"          ""A+""              ""5")
    else: 
        print("  English 2nd Paper:""                              ",e2nd,"           ""A+""              ""5")

e1 = english_1st_paper
e2 = english_2nd_paper
if(e1<0 or e1>100 or e2<0 or e2>100):
    eng = "Invalid"
else:
    if(e1<33 or e2<33):
        eng = 0
    else:
        eng = ((e1+e2)/2)
        if(eng==0):
         eng = 0
        else:
         if(33<=eng<40):
          eng = 1
         elif(40<=eng<50):
          eng = 2
         elif(50<=eng<60):
           eng = 3
         elif(60<=eng<70):
           eng = 3.5
         elif(70<=eng<80):
           eng = 4
         else:
           eng = 5


print("-----------------------------------------------------------------------------------------")

gm = general_math
if(0>gm or gm>100):
    gm = "Invalid"
    print("  General Math:                                  Invalid         -               -")
else:
    
    if(0<=gm<33):
        gm = 0
        print("  General Math:""                                   ",general_math,"           ""F""               ""0")  
    elif(33<=gm<40):
        gm = 1
        print("  General Math:""                                   ",general_math,"           ""D""               ""1")
    elif(40<=gm<50): 
        gm = 2
        print("  General Math:""                                   ",general_math,"           ""C""               ""2")
    elif(50<=gm<60):
        gm = 3
        print("  General Math:""                                   ",general_math,"           ""B""               ""3")
    elif(60<=gm<70):
        gm = 3.5
        print("  General Math:""                                   ",general_math,"           ""A-""              ""3.5")
    elif(70<=gm<80):
        gm = 4
        print("  General Math:""                                   ",general_math,"           ""A""               ""4")
    elif(gm==100):
        print("  General Math:""                                   ",general_math,"          ""A+""              ""5")
    else:
        gm = 5
        print("  General Math:""                                   ",general_math,"           ""A+""              ""5")
print("-----------------------------------------------------------------------------------------")
hm = higher_math
if(0>hm or hm>75):
    print("  Higher Math:                                   Invalid         -               -")
else:
    if(0<=hm<10):
        print("  Higher Math:""                                    ",higher_math,"            ""F""               ""0")
    elif(10<=hm<25):
        print("  Higher Math:""                                    ",higher_math,"           ""F""               ""0")
    elif(25<=hm<30):
        print("  Higher Math:""                                    ",higher_math,"           ""D""               ""1")
    elif(30<=hm<37.5):
        print("  Higher Math:""                                    ",higher_math,"           ""C""               ""2")
    elif(37.5<=hm<45):
        print("  Higher Math:""                                    ",higher_math,"           ""B""               ""3")
    elif(45<=hm<52.5):  
        print("  Higher Math:""                                    ",higher_math,"           ""A-""              ""3.5")
    elif(52.5<=hm<60):
        print("  Higher Math:""                                    ",higher_math,"           ""A""               ""4")
    else:
        print("  Higher Math:""                                    ",higher_math,"           ""A+""              ""5")
print("-----------------------------------------------------------------------------------------")

hmp = higher_math_practical
if(0>hmp or hmp>25):
    print("  Higher Math Practical:                         Invalid         -               -")
else:
    if(0<=hmp<8):
        print("  Higher Math Practical:""                          ",higher_math_practical,"            ""F""               ""0")
    elif(8<=hmp<10):
        print("  Higher Math Practical:""                          ",higher_math_practical,"            ""D""               ""1")
    elif(10<=hmp<12):
        print("  Higher Math Practical:""                          ",higher_math_practical,"           ""C""               ""2")
    elif(12<=hmp<15):
        print("  Higher Math Practical:""                          ",higher_math_practical,"           ""B""               ""3")
    elif(15<=hmp<18):
        print("  Higher Math Practical:""                          ",higher_math_practical,"           ""A-""              ""3.5")
    elif(18<=hmp<20):
        print("  Higher Math Practical:""                          ",higher_math_practical,"           ""A""               ""4")
    else:
        print("  Higher Math Practical:""                          ",higher_math_practical,"           ""A+""              ""5")

hm = higher_math
hmp = higher_math_practical
if(0>hm or 0>hmp or 75<hm or 25<hmp):
    hmhmp = "Invalid"
else:
    hmhmp = hm + hmp
    if((0<=hm<25 or 0<=hmp<8) and optional_subject == "Higher Math"):
     hmhmp = 0 
    else:
     if(33<=hmhmp<40 and optional_subject == "Higher Math"):
        hmhmp = 0
     elif(40<=hmhmp<50 and optional_subject == "Higher Math"):
        hmhmp = 0
     elif(50<=hmhmp<60 and optional_subject == "Higher Math"):
        hmhmp = 1
     elif(60<=hmhmp<70 and optional_subject == "Higher Math"):
        hmhmp = 1.5
     elif(70<=hmhmp<80 and optional_subject == "Higher Math"):
        hmhmp = 2
     elif(80<=hmhmp<=100 and optional_subject == "Higher Math"):
        hmhmp = 3
     elif(0<=hm<25 or 0<=hmp<8):
        hmhmp = 0
     elif(33<=hmhmp<40):
        hmhmp = 1
     elif(40<=hmhmp<50):
        hmhmp = 2
     elif(50<=hmhmp<60):
        hmhmp = 3
     elif(60<=hmhmp<70):
        hmhmp = 3.5
     elif(70<=hmhmp<80):
        hmhmp = 4
     else:
        hmhmp = 5

print("-----------------------------------------------------------------------------------------")
b = biology
if(0>b or b>75):
    print("  Biology:                                       Invalid         -               -")
else:
    if(0<=b<10):
        print("  Biology:""                                        ",biology,"            ""F""               ""0")
    elif(10<=b<25):
        print("  Biology:""                                        ",biology,"           ""F""               ""0")
    elif(25<=b<30):
        print("  Biology:""                                        ",biology,"           ""D""               ""1")
    elif(30<=b<37.5):
        print("  Biology:""                                        ",biology,"           ""C""               ""2")
    elif(37.5<=b<45):
        print("  Biology:""                                        ",biology,"           ""B""               ""3")
    elif(45<=b<52.5):
        print("  Biology:""                                        ",biology,"           ""A-""              ""3.5")
    elif(52.5<=b<60):
        print("  Biology:""                                        ",biology,"           ""A""               ""4")
    else:
        print("  Biology:""                                        ",biology,"           ""A+""              ""5")
print("-----------------------------------------------------------------------------------------")

bp = biology_practical
if(0>bp or bp>25):
    print("  Biology Practical:                             Invalid         -               -")
else:
    if(0<=bp<8):
        print("  Biology Practical:""                              ",biology_practical,"            ""F""               ""0")
    elif(8<=bp<10):
        print("  Biology Practical:""                              ",biology_practical,"            ""D""               ""1")
    elif(10<=bp<12):
        print("  Biology Practical:""                              ",biology_practical,"           ""C""               ""2")
    elif(12<=bp<15):
        print("  Biology Practical:""                              ",biology_practical,"           ""B""               ""3")
    elif(15<=bp<18):
        print("  Biology Practical:""                              ",biology_practical,"           ""A-""              ""3.5")
    elif(18<=bp<20):
        print("  Biology Practical:""                              ",biology_practical,"           ""A""               ""4")
    else:
        print("  Biology Practical:""                              ",biology_practical,"           ""A+""              ""5")
       
b = biology
bp = biology_practical
if(0>b or 0>bp or 75<b or 25<bp):
    bbp = "Invalid"
else:
    bbp = b + bp
    if((0<=b<25 or 0<=bp<8) and optional_subject == "Biology"):
      bbp = 0 
    else:
     if(33<=bbp<40 and optional_subject == "Biology"):
        bbp = 0
     elif(40<=bbp<50 and optional_subject == "Biology"):
        bbp = 0
     elif(50<=bbp<60 and optional_subject == "Biology"):
        bbp = 1
     elif(60<=bbp<70 and optional_subject == "Biology"):
        bbp = 1.5
     elif(70<=bbp<80 and optional_subject == "Biology"):
        bbp = 2
     elif(80<=bbp<=100 and optional_subject == "Biology"):
        bbp = 3
     elif(0<=b<25 or 0<=bp<8):
        bbp = 0
     elif(33<=bbp<40):
        bbp = 1
     elif(40<=bbp<50):
        bbp = 2
     elif(50<=bbp<60):
        bbp = 3
     elif(60<=bbp<70):
        bbp = 3.5
     elif(70<=bbp<80):
        bbp = 4
     else:
        bbp = 5


print("-----------------------------------------------------------------------------------------")
p = physics
if(0>p or p>75):
    print("  Physics:                                       Invalid         -               -")
else:
    if(0<=p<10):
        print("  Physics:""                                        ",physics,"            ""F""               ""0")
    elif(10<=p<25):
        print("  Physics:""                                        ",physics,"           ""F""               ""0")
    elif(25<=p<30):
        print("  Physics:""                                        ",physics,"           ""D""               ""1")
    elif(30<=p<37.5):
        print("  Physics:""                                        ",physics,"           ""C""               ""2")
    elif(37.5<=p<45):
        print("  Physics:""                                        ",physics,"           ""B""               ""3")
    elif(45<=p<52.5):
        print("  Physics:""                                        ",physics,"           ""A-""              ""3.5")
    elif(52.5<=p<60):
        print("  Physics:""                                        ",physics,"           ""A""               ""4")
    else:
        print("  Physics:""                                        ",physics,"           ""A+""              ""5")
print("-----------------------------------------------------------------------------------------")

pp = physics_practical
if(0>pp or pp>25):
    print("  Physics Practical:                             Invalid         -               -")
else:
    if(0<=pp<8):
        print("  Physics Practical:""                              ",physics_practical,"            ""F""               ""0")
    elif(8<=pp<10):
        print("  Physics Practical:""                              ",physics_practical,"            ""D""               ""1")
    elif(10<=pp<12): 
        print("  Physics Practical:""                              ",physics_practical,"           ""C""               ""2")
    elif(12<=pp<15):
        print("  Physics Practical:""                              ",physics_practical,"           ""B""               ""3")
    elif(15<=pp<18):
        print("  Physics Practical:""                              ",physics_practical,"           ""A-""              ""3.5")
    elif(18<=pp<20):
        print("  Physics Practical:""                              ",physics_practical,"           ""A""               ""4")
    else:
        print("  Physics Practical:""                              ",physics_practical,"           ""A+""              ""5")


p = physics
pp = physics_practical
if(0>p or 0>pp or 75<p or 25<pp):
    ppp = "Invalid"
else:
    ppp = p + pp
    if(0<=p<25 or 0<=pp<8):
        ppp = 0
    else:
     if(33<=ppp<40):
        ppp = 1
     elif(40<=ppp<50):
        ppp = 2
     elif(50<=ppp<60):
        ppp = 3
     elif(60<=ppp<70):
        ppp = 3.5
     elif(70<=ppp<80):
        ppp = 4
     else:
        ppp = 5


print("-----------------------------------------------------------------------------------------")
c = chemistry
if(0>c or c>75):
    print("  Chemistry:                                     Invalid         -               -")
else:
    if(0<=c<10):
        print("  Chemistry:""                                      ",chemistry,"           ""F""               ""0")
    elif(10<=c<25):
        print("  Chemistry:""                                      ",chemistry,"           ""F""               ""0")
    elif(25<=c<30):
        print("  Chemistry:""                                      ",chemistry,"           ""D""               ""1")
    elif(30<=c<37.5):
        print("  Chemistry:""                                      ",chemistry,"           ""C""               ""2")
    elif(37.5<=c<45):
        print("  Chemistry:""                                      ",chemistry,"           ""B""               ""3")
    elif(45<=c<52.5):
        print("  Chemistry:""                                      ",chemistry,"           ""A-""              ""3.5")
    elif(52.5<=c<60):
        print("  Chemistry:""                                      ",chemistry,"           ""A""               ""4")
    else:
        print("  Chemistry:""                                      ",chemistry,"           ""A+""              ""5")
print("-----------------------------------------------------------------------------------------")

cp = chemistry_practical
if(0>cp or cp>25):
    print("  Chemistry Practical:                           Invalid         -               -")
else:
    if(0<=cp<8):
        print("  Chemistry Practical:""                            ",chemistry_practical,"            ""F""               ""0")
    elif(8<=cp<10):
        print("  Chemistry Practical:""                            ",chemistry_practical,"            ""D""               ""1")
    elif(10<=cp<12):
        print("  Chemistry Practical:""                            ",chemistry_practical,"           ""C""               ""2")
    elif(12<=cp<15):
        print("  Chemistry Practical:""                            ",chemistry_practical,"           ""B""               ""3")
    elif(15<=cp<18):
        print("  Chemistry Practical:""                            ",chemistry_practical,"           ""A-""              ""3.5")
    elif(18<=cp<20):
        print("  Chemistry Practical:""                            ",chemistry_practical,"           ""A""               ""4")
    else:
        print("  Chemistry Practical:""                            ",chemistry_practical,"           ""A+""              ""5")


c = chemistry
cp = chemistry_practical
if(0>c or 0>cp or 75<c or 25<cp):
    ccp = "Invalid"
else:
    ccp = c + cp
    if(0<=c<25 or 0<=cp<8):
        ccp = 0
    else:
     if(33<=ccp<40):
        ccp = 1
     elif(40<=ccp<50):
        ccp = 2
     elif(50<=ccp<60):
        ccp = 3
     elif(60<=ccp<70):
        ccp = 3.5
     elif(70<=ccp<80):
        ccp = 4
     else:
        ccp = 5



print("-----------------------------------------------------------------------------------------")

ir = Islamic_Religion
if(0>ir or ir>100):
    ir = "Invalid"
    print("  Islamic Religion:                              Invalid         -               -")
else:
    
    if(0<=ir<33):
        ir = 0
        print("  Islamic Religion:""                               ",Islamic_Religion,"           ""F""               ""0")  
    elif(33<=ir<40):
        ir = 1
        print("  Islamic Religion:""                               ",Islamic_Religion,"           ""D""               ""1")
    elif(40<=ir<50):
        ir = 2
        print("  Islamic Religion:""                               ",Islamic_Religion,"           ""C""               ""2")
    elif(50<=ir<60):
        ir = 3
        print("  Islamic Religion:""                               ",Islamic_Religion,"           ""B""              ""3")
        ir = 3.5
        print("  Islamic Religion:""                               ",Islamic_Religion,"           ""A-""              ""3.5")
    elif(70<=ir<80):
        ir = 4
        print("  Islamic Religion:""                               ",Islamic_Religion,"           ""A""               ""4")
    elif(ir==100):
        print("  Islamic Religion:""                               ",Islamic_Religion,"          ""A+""              ""5")
    else:
        ir = 5
        print("  Islamic Religion:""                               ",Islamic_Religion,"           ""A+""              ""5")
print("-----------------------------------------------------------------------------------------")


ss = social_science
if(0>ss or ss>100):
    ss = "Invalid"
    print("  Social Science:                                Invalid         -               -")
else:
    
    if(0<=ss<33):
        ss = 0
        print("  Social Science:""                                 ",social_science,"           ""F""               ""0")  
    elif(33<=ss<40):
        ss = 1
        print("  Social Science:""                                 ",social_science,"           ""D""               ""1")
    elif(40<=ss<50):
        ss = 2
        print("  Social Science:""                                 ",social_science,"           ""C""               ""2")
    elif(50<=ss<60):
        ss = 3
        print("  Social Science:""                                 ",social_science,"           ""B""               ""3")
    elif(60<=ss<70):
        ss = 3.5
        print("  Social Science:""                                 ",social_science,"           ""A-""              ""3.5")
    elif(70<=ss<80):
        ss = 4
        print("  Social Science:""                                 ",social_science,"           ""A""               ""4")
    elif(ss==100):
        print("  Social Science:""                                 ",social_science,"          ""A+""              ""5")
    else:
        ss = 5
        print("  Social Science:""                                 ",social_science,"           ""A+""              ""5")
print("-----------------------------------------------------------------------------------------")



ict = information_and_communications_technology
if(0>ict or ict>100):
    ict = "Invalid"
    print("  Information and Communications Technology:     Invalid         -               -")
else:
    
    if(0<=ict<33):
        ict = 0
        print("  Information and Communications Technology:""      ",information_and_communications_technology,"           ""F""               ""0")  
    elif(33<=ict<40):
        ict = 1
        print("  Information and Communications Technology:""      ",information_and_communications_technology,"           ""D""               ""1")
    elif(40<=ict<50):
        ict = 2
        print("  Information and Communications Technology:""      ",information_and_communications_technology,"           ""C""               ""2")
    elif(50<=ict<60):
        ict = 3
        print("  Information and Communications Technology:""      ",information_and_communications_technology,"           ""B""               ""3")
    elif(60<=ict<70):
        ict = 3.5
        print("  Information and Communications Technology:""      ",information_and_communications_technology,"           ""A-""              ""3.5")
    elif(70<=ict<80):
        ict = 4
        print("  Information and Communications Technology:""      ",information_and_communications_technology,"           ""A""               ""4")
    elif(ict==100):
        print("  Information and Communications Technology:""      ",information_and_communications_technology,"          ""A+""              ""5")
    else:
        ict = 5
        print("  Information and Communications Technology:""      ",information_and_communications_technology,"           ""A+""              ""5")



print("-----------------------------------------------------------------------------------------")

am = "Invalid"

if(ban=="Invalid" or eng=="Invalid" or gm=="Invalid" or hmhmp=="Invalid" or bbp=="Invalid" or ppp=="Invalid" or ccp=="Invalid" or ir=="Invalid" or ss=="Invalid" or ict=="Invalid"):
    t = "Invalid"
else:
    t = bangla_1st_paper + bangla_2nd_paper + english_1st_paper + english_2nd_paper + general_math + higher_math + higher_math_practical + biology + biology_practical + physics + physics_practical + chemistry + chemistry_practical + Islamic_Religion + social_science + information_and_communications_technology
    if(t == bangla_1st_paper + bangla_2nd_paper + english_1st_paper + english_2nd_paper + general_math + higher_math + higher_math_practical + biology + biology_practical + physics + physics_practical + chemistry + chemistry_practical + Islamic_Religion + social_science + information_and_communications_technology):
        am = t/12
    else:
        am = "Invalid"





print("                   Total Mark:"      ,t,        )
print(" ")
print("                 Average Mark:"      ,am,       )

print(" ")


if(ban=="Invalid" or eng=="Invalid" or gm=="Invalid" or hmhmp=="Invalid" or bbp=="Invalid" or ppp=="Invalid" or ccp=="Invalid" or ir=="Invalid" or ss=="Invalid" or ict=="Invalid"):
    print("  Result: Invalid")
else:
    if(optional_subject=="Higer Math" and (ban==0 or eng==0 or gm==0 or bbp==0 or ppp==0 or ccp==0 or ir==0 or ss==0 or ict==0)):
        print("Result: Fail")
    elif(optional_subject=="Biology" and (ban==0 or eng==0 or gm==0 or hmhmp==0 or ppp==0 or ccp==0 or ir==0 or ss==0 or ict==0)):
        print("Result: Fail")
    else:
        sum = ban + eng + gm + hmhmp + bbp + ppp + ccp + ir + ss + ict
        average = sum/9
        if(45<sum):
            print("Result: GPA: 5")
        else:
            print("Result: GPA:" , average)

print(" ")
