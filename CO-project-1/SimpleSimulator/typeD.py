import Globals
def store_in_memory_from_register(register:str,memory_address:str)->None:
    Globals.memory[memory_address]=Globals.registers[register][9:].zfill(16)
def load_in_register_from_memory(register:str,memory_address:str)->None:
    Globals.registers[register]=Globals.memory[memory_address].zfill(16)
def type_D(instruction:str)->None:
    if (instruction[0:5]=="00100"):
        load_in_register_from_memory(instruction[6:9],instruction[9:])
    if (instruction[0:5]=="00101"):#store
        store_in_memory_from_register(instruction[6:9],instruction[9:])#6,7,8