# EDIT THE FILE WITH YOUR SOLUTION
import re

from itertools import product
filename = input("Which text file do you want to use for the puzzle? ")
#filename = "test_44.txt"
with open(filename) as file:
    text = file.read()
text = text. replace('\n', ' ')
name=[]
name=re.findall('Sir (\w+)',text)
for e in re.findall('Sirs (\w+) and (\w+)', text):
    name.append(e[0])
    name.append(e[1])
for e in re.findall('Sirs (\w+) or (\w+)', text):
    name.append(e[0])
    name.append(e[1])
for e in re.findall('Sirs (\w+)((, \w+)+) and (\w+)', text):
    #print(e)
    name.append(e[0])
    #print(name)
    name.append(e[3])
    name += re.findall(', (\w+)', e[1])
for e in re.findall('Sirs (\w+)((, \w+)+) or (\w+)', text):
    #print(e)
    name.append(e[0])
    #print(name)
    name.append(e[3])
    name += re.findall(', (\w+)', e[1])
name=list(set(name))
#print(name)
sirs_sentence = []
speaker = []
for e in re.findall( 'Sir (\w+)[^.!?]* ("[^:"]*")',text):
    speaker.append(e[0])
    sirs_sentence.append(e[1])
for e in re.findall('("[^:"]*,")[^".!?]* Sir (\w+)',text):
    speaker.append(e[1])
    sirs_sentence.append(e[0])
#print(speaker)
#print(sirs_sentence)
person_in_sen = []
name_in_sen = []
for i in range(len(sirs_sentence)):
    if re.search("I ", sirs_sentence[i]) :
        name_in_sen.append(speaker[i])
        #print(speaker[i])
    if re.search(" us ", sirs_sentence[i]) :
        name_in_sen=name
    for e in re.findall('Sir (\w+)', sirs_sentence[i]):
        
        name_in_sen.append(e)
        #print(name_in_sen)
    for e in re.findall('Sir  (\w+)', sirs_sentence[i]):
        
        name_in_sen.append(e)
    for e in re.findall('Sirs (\w+) and (\w+)', sirs_sentence[i]):
        #print(e)
        name_in_sen.append(e[0])
        name_in_sen.append(e[1])
    for e in re.findall('Sirs (\w+) or (\w+)', sirs_sentence[i]):
        name_in_sen.append(e[0])
        name_in_sen.append(e[1])
    for e in re.findall('Sirs (\w+)((, \w+)+) and (\w+)', sirs_sentence[i]):
        #print(e)
        name_in_sen.append(e[0])
        #print(name)
        name_in_sen.append(e[3])
        name_in_sen.append(re.findall(', (\w+)', e[1]))
    person_in_sen.append(name_in_sen)
    name_in_sen=[]
#print(person_in_sen)   
n = len(name)
truthtable=set(product([0,1],repeat=n))
truthtable1=set(product([0,1],repeat=n))
name.sort()
#print(name)
for i in range(len(speaker)) :
    if re.search("[Aa]t least ", sirs_sentence[i]) or re.search(" or ", sirs_sentence[i]) :
        #print(1)
        if re.search(" Knight", sirs_sentence[i]) :
            for v in truthtable:
                a=0
                for sir in person_in_sen[i]:
                    a += v[name.index(sir)]
                if a == 0 and v[name.index(speaker[i])]==1 :
                    truthtable1 -={v}
                if a >= 1 and v[name.index(speaker[i])]== 0 :
                    truthtable1 -={v}
        if re.search(" Knave", sirs_sentence[i]) :
            for v in truthtable:
                a=0
                for sir in person_in_sen[i]:
                    a += v[name.index(sir)]
                if a == len(person_in_sen[i]) and v[name.index(speaker[i])]==1  :
                #and v[name.index(speaker[i])]== 0 :
                    truthtable1 -={v}
                if a != len(person_in_sen[i]) and v[name.index(speaker[i])]==0  :
                    truthtable1 -={v} 
        #print(truthtable1)
            
    elif re.search("[Aa]t most ", sirs_sentence[i]) :
        #print(2)
        if re.search(" Knight",sirs_sentence[i]) :
            for v in truthtable:
                a=0
                for sir in person_in_sen[i]:
                    a += v[name.index(sir)]
                if a != 1 and v[name.index(speaker[i])]==1 :
                    truthtable1 -={v}
                if a < 2 and v[name.index(speaker[i])]== 0 :
                    truthtable1 -={v}
        if re.search(" Knave", sirs_sentence[i]) :
            for v in truthtable:
                a=0
                for sir in person_in_sen[i]:
                    a += v[name.index(sir)]
                if a < len(person_in_sen[i])-1 and v[name.index(speaker[i])]==1  :
                    truthtable1 -={v}
                if a > len(person_in_sen[i])-2 and v[name.index(speaker[i])]==0  :
                    truthtable1 -={v}   
        #print(truthtable1)
    elif re.search("[Ee]xactly one of ", sirs_sentence[i]) :
        #print(3)
        if re.search(" Knight",  sirs_sentence[i]) :
            for v in truthtable:
                a=0
                for sir in person_in_sen[i]:
                    a += v[name.index(sir)]
                if a != 1 and v[name.index(speaker[i])]==1 :
                    truthtable1 -={v}
                if a == 1  and v[name.index(speaker[i])]== 0 :
                    truthtable1 -={v}
            #print(truthtable1)
        if re.search(" Knave", sirs_sentence[i]) :
            for v in truthtable:
                a=0
                for sir in person_in_sen[i]:
                    a += v[name.index(sir)]
                if a != len(person_in_sen[i])-1 and v[name.index(speaker[i])]==1  :
                    truthtable1 -={v}
                if a == len(person_in_sen[i])-1 and v[name.index(speaker[i])]==0  :
                    truthtable1 -={v}
    elif re.search("[Aa]ll of ", sirs_sentence[i]) :
        #print(4)
        if re.search(" Knight", sirs_sentence[i]) :
            for v in truthtable:
                a=0
                for sir in person_in_sen[i]:
                    a += v[name.index(sir)]
                if  a != len(person_in_sen[i]) and v[name.index(speaker[i])]==1 :
                    truthtable1 -={v}
                if  a ==  len(person_in_sen[i]) and v[name.index(speaker[i])]== 0 :
                    truthtable1 -={v}
        if re.search(" Knave", sirs_sentence[i]) :
            for v in truthtable:
                a=0
                for sir in person_in_sen[i]:
                    a += v[name.index(sir)]
                if v[name.index(speaker[i])]==1  :
                    truthtable1 -={v}
                if  a ==0 and v[name.index(speaker[i])]==0  :
                    truthtable1 -={v}
            #print(truthtable1)
    elif re.search("I am", sirs_sentence[i]) :
        #print(5)
        if re.search(" Knight", sirs_sentence[i]) :
            for v in truthtable:
                a=0
                for sir in person_in_sen[i]:
                    a += v[name.index(sir)]
                if a != 1 and v[name.index(speaker[i])]==1 :
                    truthtable1 -={v}
                if a != 0  and v[name.index(speaker[i])]== 0 :
                    truthtable1 -={v}
        if re.search(" Knave", sirs_sentence[i]) :
            for v in truthtable:
                a=0
                for sir in person_in_sen[i]:
                    a += v[name.index(sir)]
                if  v[name.index(speaker[i])]==1 :
                    truthtable1 -={v}
                if  v[name.index(speaker[i])]== 0 :
                    truthtable1 -={v}
    elif re.search("Sir (\w+) is", sirs_sentence[i]) :
        #print(6)
        if re.search(" Knight", sirs_sentence[i]) :
            for v in truthtable:
                a=0
                for sir in person_in_sen[i]:
                    a += v[name.index(sir)]
                if a != 1 and v[name.index(speaker[i])]==1 :
                    truthtable1 -={v}
                if a != 0  and v[name.index(speaker[i])]== 0 :
                    truthtable1 -={v}
                    
        if re.search(" Knave", sirs_sentence[i]) :
            for v in truthtable:
                a=0
                for sir in person_in_sen[i]:
                    a += v[name.index(sir)]
                if a == len(person_in_sen[i]) and v[name.index(speaker[i])]==1 :
                    truthtable1 -={v}
                
                if a == 0  and v[name.index(speaker[i])]== 0 :
                    truthtable1 -={v}
        #print(truthtable1)
    else :
       # print(7)
        if re.search(" Knight", sirs_sentence[i]) :
            for v in truthtable:
                a=0
                for sir in person_in_sen[i]:
                    a += v[name.index(sir)]
                if a != len(person_in_sen[i]) and v[name.index(speaker[i])]==1 :
                    truthtable1 -={v}
                if a == len(person_in_sen[i])  and v[name.index(speaker[i])]== 0 :
                    truthtable1 -={v}
            #print(truthtable1)
        if re.search(" Knave", sirs_sentence[i]) :
            for v in truthtable:
                a=0
                for sir in person_in_sen[i]:
                    a += v[name.index(sir)]
                if a != 0 and v[name.index(speaker[i])]==1  :
                    truthtable1 -={v}
                if a == 0 and v[name.index(speaker[i])]==0  :
                    truthtable1 -={v}    
#print(truthtable1
print("The Sirs are:",end='')
for i in name:
    o = str(i)
    print(" "+o,end='')
print()
if len(truthtable1) == 0:
    print("There is no solution.")
if len(truthtable1) > 1 :   
    print("There are "+str(len(truthtable1))+" solutions.")
if len(truthtable1) == 1:
    print("There is a unique solution:")
    ttt=list(truthtable1)
    rrr=list(ttt[0])
    www=[]
    for i in rrr:
        if i == 0 :
            www.append("Knave")
        if i == 1 :
            www.append("Knight")          
    for i in range(len(www)):
        print("Sir "+str(name[i])+" is a "+str(www[i])+".")

    
