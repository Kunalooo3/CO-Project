#$ sign ka me confirm karta hoo kya matlab hai
import re

def check_label(L):
    global is_error
    c=0
    labels=[]
    D={}
    for i in L:
        num_semicolon=0
        for j in range(0,len(i[0])):
            if i[0][j]==":":
                num_semicolon=num_semicolon+1
                D[c]=i[0][:j]
                if i[0][:j] not in labels:
                    labels.append(i[0][:j])
                else:
                    print (f"error multiple definitions of {i[0][:j]}")
                    is_error=True
                    break
            if (num_semicolon>1):
                print("invalid name")
                is_error=True
                break
        c=c+1
    D_new = {v: k for k, v in D.items()}
    for key in D_new .keys():
        binary_str = bin(D_new [key])[2:]  
        D_new [key] = binary_str.zfill(7)
    return D_new

def check_hlt(L):
    c=0
    for i in range(0,len(L)):
        if (L[i].strip()=='hlt'):
            c=c+1
    if (c>1):
        raise SyntaxError("hlt used multiple times")
    if (c==0):
        raise SyntaxError("hlt not used")
    if (L[-1].strip()=='hlt'):
        return None
    else:
        raise SyntaxError("hlt not used as last instruction")


    
syntax={
    "00000":{"mnemonic":"add","num_registers":3,"other":0,"type":"A"},
    "00001":{"mnemonic":"sub" ,"num_registers":3,"other":0,"type":"A"},
    "00110":{"mnemonic":"mul" ,"num_registers":3,"other":0,"type":"A"},
    "00111":{"mnemonic":"div" ,"num_registers":3,"other":0,"type":"C"},
    "00010":{"mnemonic":"mov","num_registers":1,"other":0,"type":"B"},
    "00011":{"mnemonic":"mov","num_registers":2,"other":0,"type":"C"},
    "00100":{"mnemonic":"ld","num_registers":1,"other":"mem_addr","type":"D"},
    "00101":{"mnemonic":"st","num_registers":1,"other":"mem_addr","type":"D"},
    "01000":{"mnemonic":"rs","num_registers":1,"other":0,"type":"B"},#$ i/o is a 7 bit value
    "01001":{"mnemonic":"ls","num_registers":1,"other":0,"type":"B"},#$ i/o is a 7 bit value
    "01010":{"mnemonic":"xor","num_registers":3,"other":0,"type":"A"},
    "01011":{"mnemonic":"or","num_registers":3,"other":0,"type":"A"},
    "01100":{"mnemonic":"and","num_registers":3,"other":0,"type":"A"},
    "01101":{"mnemonic":"not","num_registers":3,"other":0,"type":"C"},
    "01110":{"mnemonic":"cmp","num_registers":2,"other":0,"type":"C"},
    "01111":{"mnemonic":"jmp","num_registers":0,"other":"mem_addr","type":"E"},
    "11100":{"mnemonic":"jlt","num_registers":0,"other":"mem_addr","type":"E"},
    "11101":{"mnemonic":"jgt","num_registers":0,"other":"mem_addr","type":"E"},
    "11111":{"mnemonic":"je","num_registers":0,"other":"mem_addr","type":"E"},
    "11010":{"mnemonic":"hlt","num_registers":0,"other":0,"type":"E"}
    }
registers ={'R0':'000', 'R1':'001', 'R2':'010', 'R3':'011','R4':'100', 'R5':'101','R6':'110','flags':'111'}
mnemonics=["add","sub","mul","div","mov","ld","st","rs","ls","xor","or","and","not","cmp","jmp","jgt","je","hlt"]
flags={'V':0,'L':0,'G':0,'E':0}
with open('assembler.txt','r') as f:
    s=f.read()
    L=s.split('\n')
check_hlt(L)
L1=[i.strip().split() for i in L]
semantics=[(i,syntax[i]["mnemonic"])for i in syntax.keys()]
print(semantics)
print("L1",L1)
mem_address=[]
var_count = len(re.findall(r'^\s*var\s+\w+', s, re.MULTILINE))
var_addresses = [i + 1 for i in range(var_count)]
for i, addr in enumerate(var_addresses):
    mem_address.append(f"var{i + 1}, {addr:07b}")
t= [(s.split(',')[0], s.split(',')[1]) for s in mem_address]
print(mem_address)
print(var_count)
print(var_addresses)
print(t)
def m_address(x):                                       # MEMORY ADDRESS OF TYPE D RESISTOR
    for a in range(0,var_count):
        if x==t[a][0]:
            return t[a][1]
def resistore(x):
    y=check_label(L1)  
    if x in y:
        return(y[x])

print(check_label(L1))

        

print(L1)


for i in L1:
    c=1
    if len(i)>1:
        if i[1]=="flag":
            raise SyntaxError("invalid use of flag")

    if i[0]=="var":
        pass
    elif i[0][-1]==":":
        pass
    elif i[0] in mnemonics:
        if (i[0]=="hlt"):
            s1="11010"+" "+"0"*11
            print(s1)
        #i[0]=syntax[i[0]]["mnemonic"]
        for j in range(0,len(semantics)):
            if (semantics[j][1]==i[0]):
                i[0]=semantics[j][0]
                
        if (syntax[i[0]]["type"]=="A"):                                                    #FOR TYPE A ISA
            s1=i[0]+" "+"0"*2+" "+registers[i[1]]+" "+registers[i[2]]+" "+registers[i[3]]
        if (syntax[i[0]]["mnemonic"]=="mov"and i[2] not in registers.keys()):              #TypeB:register and immediate type
            v=bin(int(i[2][1:]))[2:]
            #print("**********\n",i[2],"\n***********")
            if (len(v)==7):
                s1=i[0]+" "+"0"+" "+registers[i[1]]+" "+v
            elif (len(v)<7):
                v="0"*(7-len(v))+v
                s1=i[0]+" "+"0"+" "+registers[i[1]]+" "+v
            else:
                raise OverflowError("cannot take input more than 7 bits")
        if (syntax[i[0]]["mnemonic"]=="mov"and i[2] in registers.keys()):
            s1="00011"+" "+"0"*5+" "+registers[i[1]]+" "+registers[i[2]]

        if (syntax[i[0]]["type"]=="B"):                                                   #FOR TYPE B ISA
            v=bin(int(i[2][1:]))[2:]
            #print("**********\n",i[2],"\n***********")
            if (len(v)==7):
                s1=i[0]+" "+"0"+" "+registers[i[1]]+" "+v
            elif (len(v)<7):
                v="0"*(7-len(v))+v
                s1=i[0]+" "+"0"+" "+registers[i[1]]+" "+v
            else:
                raise OverflowError("cannot take input more than 7 bits")
            
        if (syntax[i[0]]["type"]=="C"):                                                  #FOR TYPE C ISA
            s1=i[0]+" "+"0"*5+" "+registers[i[1]]+" "+registers[i[2]]

        if (syntax[i[0]]["type"]=="D"):                                                  #FOR TYPE D ISA
            s1=i[0]+" "+"0"+" "+registers[i[1]]+str(m_address(i[2].strip()))

        if (syntax[i[0]]["type"]=="E"): 
            s1=i[0]+" "+"0"*4+" "+"memory_address"                                                 #FOR TYPE E ISA
        

        if (syntax[i[0]]["type"]=="F"):                                                  #FOR TYPE F ISA
            s1=i[0]+" "+"0"*11
        print(s1)
        c=c+1
    else:
        raise SyntaxError("syntax error on line {}".format(c))
#print(syntax)
