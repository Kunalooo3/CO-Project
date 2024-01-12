import Globals
def jmp(address:str)->None:
    Globals.pc=int(address,2)
    Globals.reset_Flags()
def jlt(address:str)->None:
    is_jlt=False
    if (Globals.registers['111']=='0'*13+'1'+'0'*2):
        is_jlt=True
        Globals.reset_Flags()
    if (is_jlt==True):
        Globals.pc=int(address,2)
        Globals.reset_Flags()
        return
    Globals.pc=Globals.pc+1
    Globals.reset_Flags()
def jgt (address:str)->None:
    is_jgt=False
    if (Globals.registers['111']=="0"*14+'1'+'0'):
        is_jgt=True
        Globals.reset_Flags()
    if (is_jgt==True):
        Globals.pc=int(address,2)
        Globals.reset_Flags()
        return
    Globals.pc=Globals.pc+1
    Globals.reset_Flags()
def je(address:str)->None:
    is_je=False
    if (Globals.registers['111']=="0"*15+'1'):
        is_je=True
        Globals.reset_Flags()
    if (is_je==True):
        Globals.pc=int(address,2)
        Globals.reset_Flags()
        return
    Globals.pc=Globals.pc+1
    Globals.reset_Flags()
def type_E(instruction:str)->None:
    if (instruction[0:5]=="01111"):
        jmp(instruction[9:])
    if (instruction[0:5]=="11100"):
        jlt(instruction[9:])
    if (instruction[0:5]=="11101"):
        jgt(instruction[9:])
    if (instruction[0:5]=="11111"):
        je(instruction[9:])
    x=''
    for i in Globals.registers.values():
        x+=i+' '
    print(x[:-1])