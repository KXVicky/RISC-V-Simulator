#Assuming MuxB, RA, RB, IR, RZ, PC, PC_temp, imme are global variables.
#decode fills MuxB, RA, RB, imme
#MuxB = 0 for value from RB to ALU. MuxB = 1 for imme to ALU
#Decodes outputs the name (string, lowercase) of instruction in variable operation:-
#add, and, or, sll, slt, sra, srl, sub, xor, mul, div, rem
#addi, andi, ori, lb, ld, lh, lw, jalr
#sb, sw, sd, sh
#beq, bne, bge, blt
#auipc, lui
#jal

#Output of alu will be in register(global variable) RZ

#Global variables (Same as diagram)
#RA
#RB
#RZ
#PC
#PC_temp
#MuxB
#imme
#IR
#RD
#RY

from bitstring import BitArray

def alu(operation):
	print("OPERATION Preforming : ", operation)
	
	if operation == "add":
		RZ = RA + RB
	elif operation == "addi":
		RZ = RA + imme
	elif operation == "sub":
		RZ = RA - RB
	elif operation == "mul":
		RZ = RA * RB
	elif operation == "div":
		RZ = int(RA / RB)
	elif operation == "rem":
		RZ = RA % RB
	elif operation == "xor":
		RZ = RA ^ RB
	elif operation == "and":
		RZ = RA & RB
	elif operation == "andi":
		RZ = RA & imme
	elif operation == "or":
		RZ = RA | RB
	elif operation == "ori":
		RZ = RA | imme
	elif operation == "sll":
		RZ = BitArray(int = RA, length = 32) << RB		#Restricting size to 32 bits
		RZ = RZ.int 	#Converting back to int
	elif operation == "srl":
		RZ = BitArray(int = RA, length = 32) >> RB
		RZ = RZ.int
	elif operation == "sra":
		RZ = RA >> RB
	elif operation == "slt":
		if RA < RB:
			RZ = 1
		else:
			RZ = 0
	elif operation == "beq":
		if RA == RB:
			RZ = (PC - 4) + imme
			PC = RZ
		else:
			RZ = PC
	elif operation == "bne":
		if RA != RB:
			RZ = (PC - 4) + imme
			PC = RZ
		else:
			RZ = PC
	elif operation == "bge":
		if RA >= RB:
			RZ = (PC - 4) + imme
			PC = RZ
		else:
			RZ = PC
	elif operation == "blt":
		if RA < RB:
			RZ = (PC - 4) + imme
			PC = RZ
		else:
			RZ = PC
	elif operation == "auipc":
		RZ = (PC - 4) + imme
	elif operation == "jal":
		RZ = (PC - 4) + imme
		PC_temp = PC
		PC = RZ
	elif operation == "jalr":
		RZ = RA + imme
		PC_temp = PC
		PC = RZ
	elif operation == "lui":
		RZ = RA + imme
	elif operation == "sb":
		RZ = RA + imme
	elif operation == "sw":
		RZ = RA + imme
	elif operation == "sd":
		RZ = RA + imme
	elif operation == "sh":
		RZ = RA + imme
	elif operation == "lb":
		RZ = RA + imme
	elif operation == "ld":
		RZ = RA + imme
	elif operation == "lh":
		RZ = RA + imme
	elif operation == "lw":
		RZ = RA + imme


