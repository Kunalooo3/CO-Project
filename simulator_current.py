import sys,json
import Globals,typeA,typeB,typeC,typeE
s=sys.stdin.read()
L1=s.split("\n") #list of instructions in each line in machine code  
#this part will actually execute program
output=[]
f=open("output.txt","w")
if __name__=="__main__":
    while True:
        if (L1[Globals.pc][0:5]=="11010"):#halt instruction(first five bits are opcode) # type F instructions 
            break
        if ((L1[Globals.pc][0:5]=="00000") or (L1[Globals.pc][0:5]=="00001") or (L1[Globals.pc][0:5]=="00110")  or (L1[Globals.pc][0:5]=="01010") or (L1[Globals.pc][0:5]=="01011") or (L1[Globals.pc][0:5]=="01100")):     #type A instruction ke lie
            typeA.type_A(L1[Globals.pc])
        if ((L1[Globals.pc][0:5]=="00010") or (L1[Globals.pc][0:5]=="01000") or (L1[Globals.pc][0:5]=="01001")): #type B instruction ke lie
            typeB.type_B(L1[Globals.pc])
        if ((L1[Globals.pc][0:5]=="00011") or (L1[Globals.pc][0:5]=="00111") or (L1[Globals.pc][0:5]=="01101") or (L1[Globals.pc][0:5]=="01110")): #type C instructions ke lie
            typeC.type_C(L1[Globals.pc])#flags ko reset karni wali condition theek karni hai
            if L1[Globals.pc+1][0:5] not in {'01111','11100','11101','11111'} :
                Globals.reset_Flags()
        if ((L1[Globals.pc][0:5]=="00100") or (L1[Globals.pc][0:5]=="00101")): #type D instructions ke lie 
            pass
        if ((L1[Globals.pc][0:5]=="01111") or (L1[Globals.pc][0:5]=="11100") or (L1[Globals.pc][0:5]=="11101") or (L1[Globals.pc][0:5]=="11111")): # type E instructions ke lie
            typeE.type_E(L1[Globals.pc])
            continue
        Globals.pc=Globals.pc+1
        output.append(str(Globals.registers))
    for i in output:
        f.write(i+"\n")
    f.close() 