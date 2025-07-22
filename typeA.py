import Globals
def add(r1:str,r2:str,r3:str)->None:
    R2=int(Globals.registers[r2],2)
    R3=int(Globals.registers[r3],2)
    sUm=bin(R2+R3)[2:]
    if (len(sUm)>16):
        Globals.registers['111']='0'*12+'1'+'0'*2
        Globals.registers[r1]='0'*16
        return
    Globals.registers[r1]=sUm.zfill(16)
def sub(r1:str,r2:str,r3:str)->None:
    R2=int(Globals.registers[r2],2)
    R3=int(Globals.registers[r3],2)
    if (R3>R2):
        Globals.registers['111']='0'*11+'1'+'0'*3
        Globals.registers[r1]='0'*16
        return 
    diff=bin(R2-R3)[2:]
    Globals.registers[r1]=diff.zfill(16)
def mul(r1:str,r2:str,r3:str)->None:
    R2=int(Globals.registers[r2],2)
    R3=int(Globals.registers[r3],2)
    prod=bin(R2*R3)[2:]
    if (len(prod)>16):
        Globals.registers['111']="0"*12+"1"+"0"*2
        return
    Globals.registers[r1]=prod.zfill(16)
def aNd(r1:str,r2:str,r3:str)->None:
    R2=int(Globals.registers[r2],2)
    R3=int(Globals.registers[r3],2)
    R1=R2&R3
    Globals.registers[r1]=bin(R1)[2:].zfill(16)
def oR(r1:str,r2:str,r3:str)->None:
    R2=int(Globals.registers[r2],2)
    R3=int(Globals.registers[r3],2)
    R1=R2|R3
    Globals.registers[r1]=bin(R1)[2:].zfill(16)
def xOr(r1:str,r2:str,r3:str)->None:
    R2=int(Globals.registers[r2],2)
    R3=int(Globals.registers[r3],2)
    R1=R2^R3
    Globals.registers[r1]=bin(R1)[2:].zfill(16)
def type_A(instruction:str)->None:
    if (instruction[0:5]=="00000"):
        add(instruction[7:10],instruction[10:13],instruction[13:])
    if (instruction[0:5]=="00001"):
        sub(instruction[7:10],instruction[10:13],instruction[13:])
    if (instruction[0:5]=="00110"):
        mul(instruction[7:10],instruction[10:13],instruction[13:])
    if (instruction[0:5]=="01010"):
        xOr(instruction[7:10],instruction[10:13],instruction[13:])
    if (instruction[0:5]=="01011"):
        oR(instruction[7:10],instruction[10:13],instruction[13:])
    if (instruction[0:5]=="01100"):
        aNd(instruction[7:10],instruction[10:13],instruction[13:])