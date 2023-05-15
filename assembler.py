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
