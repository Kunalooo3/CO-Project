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
#dictionary to map registers with their code

registers ={'R0':'000', 'R1':'001', 'R2':'010', 'R3':'011','R4':'100', 'R5':'101','R6':'110','FLAGS':'111'}

#list of mnemonics,flags

mnemonics=["add","sub","mul","div","mov","ld","st","rs","ls","xor","or","and","not","cmp","jmp","jgt","je","hlt","jlt"]
flags={'V':0,'L':0,'G':0,'E':0}
is_error=False

s=sys.stdin.read()
L=s.split("\n")
check_hlt(L)
for i in L:
    count=i.count("\t")
    s=list(i)
    while count:
        s.remove("\t")
        count=count-1
    i=''.join(s)
L1=[i.strip().split() for i in L if i!='']
if (len(L1))>128:
    print("error lines exceeded 128")
    exit()
# print(L1)
# print(L)
semantics=[(i,syntax[i]["mnemonic"])for i in syntax.keys()]
c=0# c is line number
variables,num=check_variable_declaration_beginning(L1)
D_labels,label=check_label(L1)
check_flags(L1)
D=allocate_variable_address(L1,variables,num)
for i in L1:
    if L1.index(i)==len(L1)-2:
        c=c+1
    if i[0]=="var":                         
        continue
    if i[0] not in mnemonics and i[0][:-1] in label:
        i.pop(0)
    if (i[0]=="mov"):
        if ((i[2] in ['R0','R1','R2','R3','R4','R5','R6','FLAGS']) and (i[1] in  ['R0','R1','R2','R3','R4','R5','R6','FLAGS'])):
            s1="00011"+"0"*5+registers[i[1]]+registers[i[2]]
            #print(s1)
            print(s1)
            continue
        if ((i[1] not in  ['R0','R1','R2','R3','R4','R5','R6','FLAGS']) and (i[2] not in ['R0','R1','R2','R3','R4','R5','R6','FLAGS'])):
            s="line "+str(L1.index(i)-len(variables))
            print("invalid name of register"+s)
            exit()
    if i[0] in mnemonics:
        if (i[0]=="hlt"):
            s1="11010"+"0"*11
            #print(s1)
            print(s1)
            break
            
           #i[0]=syntax[i[0]]["mnemonic"]
        for j in range(0,len(semantics)):
            if (semantics[j][1]==i[0]):
                i[0]=semantics[j][0]
                break
                
        if (syntax[i[0]]["type"]=="A"):#type A
            # if ((registers[i[1]] in registers.keys()) and (registers[i[2]] in registers.keys()) and (registers[i[3]] in registers.keys())):
            try:
                s1=i[0]+"0"*2+registers[i[1]]+registers[i[2]]+registers[i[3]]
            except:
                print(f"invalid register name {L1.index(i)-len(variables)}")
                exit()
            # else:
            #     s="line "+str(L1.index(i)-len(variables))
            #     f_output.write("invalid register name "+s)
            #     exit()
        if (syntax[i[0]]["mnemonic"]=="mov"and i[2]  in variables):          
            v=bin(int(i[2][1:]))[2:]
            if (len(v)==7):
                s1="00010"+"0"+registers[i[1]]+v
            elif (len(v)<7):
                v="0"*(7-len(v))+v
                s1="00010"+"0"+registers[i[1]]+v
            else:
                s="line no. "+str(L1.index(i)-len(variables))
                print("cannot take input more than 7 bits"+s)
                exit()

        if (syntax[i[0]]["mnemonic"]=="mov"and i[2] in ['R0','R1','R2','R3','R4','R5','R6','flag']):
            s1="00011"+"0"*5+registers[i[1]]+registers[i[2]]
        if (syntax[i[0]]["type"]=="B"):
            v=bin(int(i[2][1:]))[2:]
            if (len(v)==7):
                s1=i[0]+"0"+registers[i[1]]+v                           
            elif (len(v)<7):
                v="0"*(7-len(v))+v
                s1=i[0]+"0"+registers[i[1]]+v
            else:
                s="line no. "+str(L1.index(i)-len(variables))
                print("cannot take input more than 7 bits"+s)
                exit()
        if (syntax[i[0]]["type"]=="C"):
            if (((i[1]) in registers) and (i[2] in registers)):
                s1=i[0]+"0"*5+registers[i[1]]+registers[i[2]]
            else:
                s="line "+str(L1.index(i)-len(variables))
                print("invalid registers "+s)
                exit()
        if (syntax[i[0]]["type"]=="D"):
            if i[2] not in variables:
                s="line "+str(L1.index(i)-len(variables))
                print("undeclared variable"+s)
                exit()
            else:
                reg=i[1]
                if reg in registers:
                    if len(D[i[2]])==7:
                        s1=i[0]+"0"+registers[i[1]]+D[i[2]]
                    else:
                        s1=i[0]+"0"+registers[i[1]]+"0"*(7-len(D[i[2]]))+D[i[2]]
                else:
                    s="line "+str(L1.index(i)-len(variables))
                    print("invalid registers "+s)
                    exit()
