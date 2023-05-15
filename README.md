def check_variable_declaration_beginning(L1,f):
    variable_number=1                                     
    flag=0
    variables=[]
    D={}
    for i in range(0,len(L1)):#i is line number
        if flag==0:
            if L1[i][0]=='var':
                if len(L1[i])!=2:
                    f.write("invalid use of variable ")
                    exit()
                if L1[i][1] in variables:
                    f.write("same variable declared multiple times ")
                    exit()
                variables.append(L1[i][1])
                D[L1[i][1]]=variable_number+i
                variable_number=variable_number+1
            if L1[i][0]!='var':
                flag=1
        else:
            if L1[i][0]=='var':
                f.write("variable not declared in beginning")
                exit()
    D1={i:bin(D[i])[2:] for i in D.keys()}
    return variables,D1

def check_label(L,f):
    c=0     #line numbers                                    
    labels=[]
    D={}
    for i in L:
        if i[0]=='var':
            continue
        if i[0].count(":")==1:
            if i[0][:-1] not in labels:
                labels.append(i[0][:-1])
                D[c]=i[0][:-1]
            # else:
            #     print("error in line",c)
            #     raise SyntaxError("multiple definition for same label")
        if (i[0].count(":")>1):
            f.write("invalid label name")
            exit()
        c=c+1
    D_new={D[i]:bin(i)[2:] for i in D.keys()}
    return D_new,labels

def check_hlt(L,f):                                    
    global is_error                                      
    c=0
    l=[]
    for i in range(0,len(L)):
        if (":" not in L[i]):
            if (L[i].strip()=='hlt'):
                if (L[i]!=''):
                    l.append(L[i])
                    c=c+1
        else:
            l=[j for j in L[i].split(":")]
            for j in l:
                if (j.strip()=='hlt'):
                    c=c+1
    if (c>1):
        f.write("hlt used multiple times")
        exit()
    if (c==0):
        f.write("hlt not used")
        exit()
    if (l[-1].strip()=='hlt'):
        return None
    else:
        f.write("hlt not used as last instruction")
        exit()
