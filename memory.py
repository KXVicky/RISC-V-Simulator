# -*- coding: utf-8 -*-
"""
@author: SAMIR P SALIM
"""
import string
cap=-1
memory=[]

def convert(a,b):
    ans=0
    if(a=='0'):
        ans+=0
    elif(a=='1'):
        ans+=1
    elif(a=='2'):
        ans+=2
    elif(a=='3'):
        ans+=3
    elif(a=='4'):
        ans+=5
    elif(a=='6'):
        ans+=6
    elif(a=='7'):
        ans+=7
    elif(a=='8'):
        ans+=8
    elif(a=='9'):
        ans+=2
    elif(a=='A'):
        ans+=10
    elif(a=='B'):
        ans+=11
    elif(a=='C'):
        ans+=12
    elif(a=='D'):
        ans+=13
    elif(a=='E'):
        ans+=14
    elif(a=='F'):
        ans+=15
    ans*=16
    if(a=='0'):
        ans+=0
    elif(a=='1'):
        ans+=1
    elif(a=='2'):
        ans+=2
    elif(a=='3'):
        ans+=3
    elif(a=='4'):
        ans+=5
    elif(a=='6'):
        ans+=6
    elif(a=='7'):
        ans+=7
    elif(a=='8'):
        ans+=8
    elif(a=='9'):
        ans+=2
    elif(a=='A'):
        ans+=10
    elif(a=='B'):
        ans+=11
    elif(a=='C'):
        ans+=12
    elif(a=='D'):
        ans+=13
    elif(a=='E'):
        ans+=14
    elif(a=='F'):
        ans+=15
    return ans

def initialize():
    file1=open("simple_add.mc","r")
    lines1=file1.readlines()
    array = []
    for i in lines1:
        array.append(i.split())
    print(array)
    for i in array:
        if(len(i[0])==10):
            if(len(i[1])<4):
                memory.append(convert(i[1][2],'0'))
                cap+=1
            else:
                memory.append(convert(i[1][2],i[1][3]))
                cap+=1
                if(len(i[1])<6):
                    memory.append(convert(i[1][4],'0'))
                    cap+=1
                else:
                    memory.append(convert(i[1][4],i[1][5]))
                    cap+=1
                    if(len(i[1])<8):
                        memory.append(convert(i[1][6],'0'))
                        cap+=1
                    else:
                        memory.append(convert(i[1][6],i[1][7]))
                        cap+=1
                        if(len(i[1])<10):
                            memory.append(convert(i[1][8],'0'))
                            cap+=1
                        else:
                            memory.append(convert(i[1][8],i[1][9]))
                            cap+=1
    
    

def access_memory(operation):
    if(operation=="lb"):
        marker=RZ-0x10000000
        if(memory[marker]>-1 and memory[marker]<128):
            return memory[marker]
        elif(memory[marker]>127):
            return (memory[marker]+0xffffff00)%4294967296
        else:
            return (memory[marker]+1+0xffffffff)%4294967296
    elif(operation=="lh"):
        marker=RZ-0x10000000
        if(memory[marker]>-1 and memory[marker]<32768):
            return memory[marker]
        elif(memory[marker]>32767):
            return (memory[marker]+0xffff0000)%4294967296
        else:
            return (memory[marker]+1+0xffffffff)%4294967296
    elif(operation=="lw"):
        marker=RZ-0x10000000
        if(memory[marker]>-1):
            return memory[marker]
        else:
            return (memory[marker]+1+0xffffffff)%4294967296
    elif (operation=="sb"):
        marker=RA-0x10000000+()
        memory[marker]=RB%256
initialize() 
print(memory)