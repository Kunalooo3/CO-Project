import sys
import Globals,typeA,typeB,typeD,typeC,typeE
s=sys.stdin.read()
L1=s.split("\n")
if '' in L1:
    L1.remove('')
#print(L1)
# for i in range(len(L1)):
#     if L1[i][-1]==' ':
#         L1[i][-1]=''
#L1.pop()#uncomment kar dena agar input hardcode kia ja raha hai to
#print(L1) 
Globals.memory={bin(i)[2:].zfill(7):L1[i] for i in range(0,len(L1))}
if (len(Globals.memory)<128):
    for i in range(len(Globals.memory),128):
        Globals.memory[bin(i)[2:].zfill(7)]="0"*16  
L1.clear()
f=open("output.txt",'w')
if __name__=="__main__":
    while True:#this part will actually execute program(simulator)
        #print(Globals.registers)
        if (Globals.memory[bin(Globals.pc)[2:].zfill(7)][0:5]=="11010"):#halt instruction(first five bits are opcode) # type F instructions
            # print("hello")
            Globals.reset_Flags()
            print(bin(Globals.pc)[2:].zfill(7),end=' '*8)
            x=''
            for i in Globals.registers.values():
                x+=i+' '
                # print(i,end=' ')
            print(x[:-1])
            break
        if ((Globals.memory[bin(Globals.pc)[2:].zfill(7)][0:5]=="00000") or (Globals.memory[bin(Globals.pc)[2:].zfill(7)][0:5]=="00001") or (Globals.memory[bin(Globals.pc)[2:].zfill(7)][0:5]=="00110")  or (Globals.memory[bin(Globals.pc)[2:].zfill(7)][0:5]=="01010") or (Globals.memory[bin(Globals.pc)[2:].zfill(7)][0:5]=="01011") or (Globals.memory[bin(Globals.pc)[2:].zfill(7)][0:5]=="01100") or (Globals.memory[bin(Globals.pc)[2:].zfill(7)][0:5]=="10000"))or(Globals.memory[bin(Globals.pc)[2:].zfill(7)][0:5]=="10001"):     #type A instruction ke lie
            typeA.type_A(Globals.memory[bin(Globals.pc)[2:].zfill(7)])
            print(bin(Globals.pc)[2:].zfill(7),end=' '*8)
            x=''
            for i in Globals.registers.values():
                x+=i+' '
                # print(i,end=' ')
            print(x[:-1])
            Globals.reset_Flags()
        if ((Globals.memory[bin(Globals.pc)[2:].zfill(7)][0:5]=="00010") or (Globals.memory[bin(Globals.pc)[2:].zfill(7)][0:5]=="01000") or (Globals.memory[bin(Globals.pc)[2:].zfill(7)][0:5]=="01001") or (Globals.memory[bin(Globals.pc)[2:].zfill(7)][0:5]=="10010")): #type B instruction ke lie
            typeB.type_B(Globals.memory[bin(Globals.pc)[2:].zfill(7)])
            Globals.reset_Flags()
            print(bin(Globals.pc)[2:].zfill(7),end=' '*8)
            x=''
            for i in Globals.registers.values():
                x+=i+' '
                # print(i,end=' ')
            print(x)
            Globals.reset_Flags()
        if ((Globals.memory[bin(Globals.pc)[2:].zfill(7)][0:5]=="00011") or (Globals.memory[bin(Globals.pc)[2:].zfill(7)][0:5]=="00111") or (Globals.memory[bin(Globals.pc)[2:].zfill(7)][0:5]=="01101") or (Globals.memory[bin(Globals.pc)[2:].zfill(7)][0:5]=="01110")): #type C instructions ke lie
            typeC.type_C(Globals.memory[bin(Globals.pc)[2:].zfill(7)])
            print(bin(Globals.pc)[2:].zfill(7),end=' '*8)
            x=''
            for i in Globals.registers.values():
                x+=i+' '
                # print(i,end=' ')
            print(x[:-1])
            if Globals.memory[bin(Globals.pc+1)[2:].zfill(7)][0:5] not in {'01111','11100','11101','11111','00011'} :
                Globals.reset_Flags()
        if ((Globals.memory[bin(Globals.pc)[2:].zfill(7)][0:5]=="00100") or (Globals.memory[bin(Globals.pc)[2:].zfill(7)][0:5]=="00101")): #type D instructions ke lie
            typeD.type_D(Globals.memory[bin(Globals.pc)[2:].zfill(7)])
            print(bin(Globals.pc)[2:].zfill(7),end=' '*8)
            x=''
            for i in Globals.registers.values():
                x+=i+' '
                # print(i,end=' ')
            print(x[:-1])
        if ((Globals.memory[bin(Globals.pc)[2:].zfill(7)][0:5]=="01111") or (Globals.memory[bin(Globals.pc)[2:].zfill(7)][0:5]=="11100") or (Globals.memory[bin(Globals.pc)[2:].zfill(7)][0:5]=="11101") or (Globals.memory[bin(Globals.pc)[2:].zfill(7)][0:5]=="11111")): # type E instructions ke lie
            print(bin(Globals.pc)[2:].zfill(7),end=' '*8)
            typeE.type_E(Globals.memory[bin(Globals.pc)[2:].zfill(7)])
            #Globals.reset_Flags()
            continue
        #([Globals.pc,Globals.registers])
        Globals.pc=Globals.pc+1
        # print()
    content=0
    # print()
    for i in Globals.memory.values():
        print(i)
        content=content+1
    while (content<127):
        print("0"*16)
        content=content+1 