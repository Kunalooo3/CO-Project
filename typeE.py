import Globals
def jmp(address:str)->None:
    Globals.pc=int(address,2)
def jlt(address:str)->None:
    if (Globals.registers['111']=='0'*12+'1'+'0'*2):
        Globals.pc=int(address,2)
        return
    Globals.pc=Globals.pc+1
def jgt (address:str)->None:
    if (Globals.registers['111']=="0"*13+'1'+'0'):
        Globals.pc=int(address,2)
        return
    Globals.pc=Globals.pc+1
def je(address:str)->None:
    if (Globals.registers['111']=="0"*14+'1'):
        Globals.pc=int(address,2)
        return
    Globals.pc=Globals.pc+1
def type_E(instruction:str)->None:
    if (instruction[0:5]=="01111"):
        jmp(instruction[9:])
        Globals.reset_Flags()
    if (instruction[0:5]=="11100"):
        jlt(instruction[9:])
        Globals.reset_Flags()
    if (instruction[0:5]=="11101"):
        jgt(instruction[9:])
        Globals.reset_Flags()
    if (instruction[0:5]=="11111"):
        je(instruction[9:])
        Globals.reset_Flags()