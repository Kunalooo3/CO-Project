import Globals
def convert_float_to_binary(n:float)->str:
    w= int(n)
    fraction= n- w
    f=n-w
    whole_binary = bin(w)[2:] 
    fractional= ''
    while fraction > 0:
        fraction *= 2
        bit = int(fraction)
        fractional += str(bit)
        fraction -= bit
    if f==0:
        fractional="0"
    binary_representation = str(whole_binary) + '.' + fractional
    return binary_representation

def binary_to_scientific(binary:str)->str:
    p=[]
    ind=0
    for i in binary:
        p.append(i)
    for i in range(0,len(p)-1):
        if p[i]==".":
            ind=i
            p.remove(".")
    p.insert(1, ".")
    e=ind-1
    exponent_decimal=e+3
    binary_exponent = format(exponent_decimal, '03b')
    s=""
    for i in p:
        s=s+str(i)
    x = s.split(".")
    mantissa=str(x[1])+"0"*(5-len(x[1]))
    ans=s+" X "+"10^"+str(e)
    return binary_exponent+mantissa
def binaryToInt(m,ex):
    exponent=0
    fraction=1
    lis=[]
    lis1=[]
    for i in range(len(ex)-1,-1,-1):
        lis.append(ex[i])
    #return(lis)
    for i in range(0,len(lis)):
        if lis[i]=="0":
            continue
        if lis[i]=="1":
            lis[i]=str(2**int(i))
    for i in lis:
        exponent=exponent+int(i)
    for i in m:
        lis1.append(i)
    for i in range(0,len(lis1)):
        if lis1[i]=="0":
            continue
        if lis1[i]=="1":
            fraction=fraction+(1/(2**(i+1)))
    real=(fraction)*(2**(exponent-3))
    return real
def addf(r1:str,r2:str,r3:str)->None:
    R2=binaryToInt(Globals.registers[r2][11:],Globals.registers[r2][8:11])
    R3=binaryToInt(Globals.registers[r3][11:],Globals.registers[r3][8:11])
    x=R2+R3
    R1_incomplete=convert_float_to_binary(x)
    R1=binary_to_scientific(R1_incomplete)
    if len(R1)>8:
        Globals.registers[r1]="0"*16
        Globals.registers['111']="0"*11+"1"+"0"*3
        return
    Globals.registers[r1]="0"*(16-len(R1))+R1
def subf(r1:str,r2:str,r3:str)->None:
    R2=binaryToInt(Globals.registers[r2][11:],Globals.registers[r2][8:11])
    R3=binaryToInt(Globals.registers[r2][11:],Globals.registers[r2][8:11])
    x=R2-R3
    if x<0:
        Globals.registers[r1]="0"*16
        Globals.registers['111']="0"*11+"1"+"0"*3
        return
    R1_incomplete=convert_float_to_binary(x)
    R1=binary_to_scientific(R1_incomplete)
    Globals.registers[r1]="0"*(16-len(R1))+R1
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
    if (instruction[0:5]=="10000"):
        addf(instruction[7:10],instruction[10:13],instruction[13:])
    if (instruction[0:5]=="10001"):
        subf(instruction[7:10],instruction[10:13],instruction[13:])