import Globals
def Cmp(r1:str,r2:str)->None:
    if (int(Globals.registers[r1],2)==int(Globals.registers[r2],2)):
        Globals.registers['111']="0"*15+'1'
    if (int(Globals.registers[r1],2)>int(Globals.registers[r2],2)):
        Globals.registers['111']="0"*14+'1'+'0'
    if (int(Globals.registers[r1],2)<int(Globals.registers[r2],2)):
        Globals.registers['111']='0'*13+'1'+'0'*2
def mov(r1:str,r2:str)-> None:
    r=Globals.registers[r1.zfill(3)]
    Globals.registers[r2.zfill(3)]=r.zfill(16)
    Globals.reset_Flags()
def div(r1:str,r2:str)-> None:
    R2=int(Globals.registers[r1],2)
    R3=int(Globals.registers[r2],2)
    if (R3==0):
        Globals.registers['111']="0"*11+"1"+"0"*3
        return
    R0=bin(R2//R3)[2:]
    R1=bin(R2%R3)[2:]
    Globals.registers["000"]=R0.zfill(16)
    Globals.registers["001"]=R1.zfill(16)
def nOt(r1:str,r2:str)-> None:
    b = ''.join('0' if bit == '1' else '1' for bit in r2)
    Globals.registers[r1]=b.zfill(16)
def type_C(instruction:str)->None:
    if (instruction[0:5]=="00011"):
        mov(instruction[11:14],instruction[14:])
    if (instruction[0:5]=="00111"):
        div(instruction[11:14],instruction[14:])
    if (instruction[0:5]=="01101"):
        nOt(instruction[11:14],instruction[14:])
    if (instruction[0:5]=="01110"):
        Cmp(instruction[10:13],instruction[13:]) 
#aur 1 more funtion flag reset jo flag ki value ko firse 0 banade yeh nahi hua hai