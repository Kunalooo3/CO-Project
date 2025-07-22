import Globals
def movI(r1:str,Imm:str)-> None:
    if (len(Imm)>7):
        Globals.registers['111']="0"*15+"1"
        Globals.registers[r1]="0"*16
        return 
    Globals.registers[r1]=Imm.zfill(16)
def rs(r1:str,Imm: str)-> None:
    T=int(Globals.registers[Imm],2)
    shifted_value = int(r1) >> T
    Globals.registers[r1]=bin(int(shifted_value))[2:].zfill(16)
def ls(r1:str,Imm:str)-> None:
    T=int(Globals.registers[Imm],2)
    shifted_value = int(r1) << T
    Globals.registers[r1]=bin(int(shifted_value))[2:].zfill(16)
def type_B(instruction:str)->None:
    if (instruction[0:5]=="00010"):
        movI(instruction[6:9],instruction[9:])
    if (instruction[0:5]=="01000"):
        rs(instruction[6:9],instruction[9:])
    if (instruction[0:5]=="01001"):
        ls(instruction[6:9],instruction[9:])