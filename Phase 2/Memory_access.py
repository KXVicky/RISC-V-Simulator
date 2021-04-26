

# Assume rd global variable
# TextMemory, and Datamemory are global
# RZ is global, output of ALU
# rd is detected in decode stage
# .


TextMemory = dict.fromkeys(range(0, 0x00000194, 4), 0)
DataMemory = dict.fromkeys(range(0x0FFFFFE8, 0x10000178, 4), 0)



StoreInst = ["beq", "bne", "bge", "blt", "auipc", "jal", "jalr", "lui", "sb", "sw", "sh", "sd", "lb", "lw", "ld", "lh"]
def Memory_access(operation, lines):
    global TextMemory, DataMemory
    array = []
    if operation in StoreInst:
        TextMemory[rd] = RZ
    if (lines):
        for i in range(len(lines)):
            if lines[i]!='\n':
                array.append(lines[i].split())
        print(array)
        for j in array:
            DataMemory[int(j[1], 16)] = int(j[0], 16)


Memory_access("Ok", ['0x10101010 0x10000178', '\n'])
print(DataMemory)
'''
    if operation == "beq":
		TextMemory[rd]=RZ
		
	elif operation == "bne":
		TextMemory[rd]=RZ
		
	elif operation == "bge":
		TextMemory[rd]=RZ
		
	elif operation == "blt":
		TextMemory[rd]=RZ
		
	elif operation == "auipc":
		TextMemory[rd]=RZ
		
	elif operation == "jal":
		TextMemory[rd]=RZ
		
	elif operation == "jalr":
		TextMemory[rd]=RZ
		
	elif operation == "lui":
		TextMemory[rd]=RZ
		
	elif operation == "sb":
		TextMemory[rd]=RZ
		
	elif operation == "sw":
		TextMemory[rd]=RZ
		
	elif operation == "sd":
		TextMemory[rd]=RZ
		
	elif operation == "sh":
		TextMemory[rd]=RZ
		
	elif operation == "lb":
		TextMemory[rd]=RZ
		
	elif operation == "ld":
		TextMemory[rd]=RZ
		
	elif operation == "lh":
		TextMemory[rd]=RZ
	elif operation == "lw":
		TextMemory[rd]=RZ
'''

