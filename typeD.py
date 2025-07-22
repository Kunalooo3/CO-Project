def type_D(instruction:str)->None:#isse poora chod dio
    if (instruction[0:5]=="00100"):
        ld(instruction[7:10],instruction[10:])
    if (instruction[0:5]=="00101"):
        st(instruction[7:10],instruction[10:])