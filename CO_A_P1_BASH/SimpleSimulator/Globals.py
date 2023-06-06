def reset_Flags()->None:
    global registers
    registers['111']="0"*16
memory={}
registers={"000":"0"*16,"001":"0"*16,"010":"0"*16,"011":"0"*16,"100":"0"*16,"101":"0"*16,"110":"0"*16,"111":"0"*16}
pc=0