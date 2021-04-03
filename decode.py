# code by ashish sulania
# decode function returns 5 values (mnemonic,rs1,rs2,rd,immediate_value) to generalise things if instruction don't have any one such as rs1,rs2,rd,immediate_value then it returns -1 for each register 
# and for immediate_value it returns  0xffffff(24 bits) number that is out of range of immediate field

def opc(inst):    # returns opcode
    return (inst&0x7f)

def fun3(inst):   # returns fun3
    return ((inst >> 12)&0x7)

def fun_7(inst):  # returns fun7
    return ((inst>>25)&0x7f)

def r_d(inst):    # returns rd
    return ((inst>>7)&0x1f)

def rs_1(inst):   # returns rs1
    return ((inst>>15)&0x1f)

def rs_2(inst):   # returns rs2
    return ((inst>>20)&0x1f)

def imm_12(inst): # returns imm12 of i format
    return ((inst>>20)&0xfff)

def imm_20(inst): # returns imm20 of u format
    return ((inst>>12)&0xfffff)

def sign_extend(value, bits):  # compare sign extended number and returns appropriate integer
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

def cals(a,b):    # calculates 12 bits of s format  imm[11:0]=imm[11:5]imm[4:0]
    a=a<<5
    a=a|b
    return a

def calsb(imm7,imm5):  # calculates 12 bits of sb format imm[12:1]=imm[12]imm[11]imm[10:5]imm[4:1]
    imm11=imm5&0x1     #imm[11] 1 bit
    imm4=imm5>>1       # imm[4:1] 4 bits
    imm6=imm7&0x6f     # imm[10:5] 6 bits
    imm10=(imm6<<4)|imm4     # imm[10:1] 10 bits
    imm11=(imm11<<10)|imm10  # imm[11:1] 11 bits
    imm12=imm7>>6            # imm[12] 1 bit
    imm12=(imm12<<11)|imm11  # imm[12:1] 12 bits
    return imm12


def decode(inst):
    if(opc(inst)==0x33):  # r format 
        print("instruction is of r format")
        if(fun3(inst)==0x0 and fun_7(inst)==0x00):
            print("instruction is add")
            rs1=rs_1(inst)
            rs2=rs_2(inst)
            rd=r_d(inst)
            return 'add',rs1,rs2,rd,0xffffff
        elif(fun3(inst)==0x0 and fun_7(inst)==0x20):
            print("instruction is sub")
            rs1=rs_1(inst)
            rs2=rs_2(inst)
            rd=r_d(inst)
            return 'sub',rs1,rs2,rd,0xffffff
        elif(fun3(inst)==0x7 and fun_7(inst)==0x00):
            print("instruction is and")
            rs1=rs_1(inst)
            rs2=rs_2(inst)
            rd=r_d(inst)
            return 'and',rs1,rs2,rd,0xffffff
        elif(fun3(inst)==0x6 and fun_7(inst)==0x00):
            print("instruction is or")
            rs1=rs_1(inst)
            rs2=rs_2(inst)
            rd=r_d(inst)
            return 'or',rs1,rs2,rd,0xffffff
        elif(fun3(inst)==0x1 and fun_7(inst)==0x00):
            print("instruction is sll")
            rs1=rs_1(inst)
            rs2=rs_2(inst)
            rd=r_d(inst)
            return 'sll',rs1,rs2,rd,0xffffff  
        elif(fun3(inst)==0x2 and fun_7(inst)==0x00):
            print("instruction is slt")
            rs1=rs_1(inst)
            rs2=rs_2(inst)
            rd=r_d(inst)
            return 'slt',rs1,rs2,rd,0xffffff
        elif(fun3(inst)==0x5 and fun_7(inst)==0x20):
            print("instruction is sra")
            rs1=rs_1(inst)
            rs2=rs_2(inst)
            rd=r_d(inst)
            return 'sra',rs1,rs2,rd,0xffffff
        elif(fun3(inst)==0x5 and fun_7(inst)==0x00):
            print("instruction is srl")
            rs1=rs_1(inst)
            rs2=rs_2(inst)
            rd=r_d(inst)
            return 'srl',rs1,rs2,rd,0xffffff
        elif(fun3(inst)==0x4 and fun_7(inst)==0x00):
            print("instruction is xor")
            rs1=rs_1(inst)
            rs2=rs_2(inst)
            rd=r_d(inst)
            return 'xor',rs1,rs2,rd,0xffffff
        elif(fun3(inst)==0x0 and fun_7(inst)==0x01):
            print("instruction is mul")
            rs1=rs_1(inst)
            rs2=rs_2(inst)
            rd=r_d(inst)
            return 'mul',rs1,rs2,rd,0xffffff
        elif(fun3(inst)==0x4 and fun_7(inst)==0x01):
            print("instruction is div")
            rs1=rs_1(inst)
            rs2=rs_2(inst)
            rd=r_d(inst)
            return 'div',rs1,rs2,rd,0xffffff
        elif(fun3(inst)==0x6 and fun_7(inst)==0x01):
            print("instruction is rem")
            rs1=rs_1(inst)
            rs2=rs_2(inst)
            rd=r_d(inst)
            return 'rem',rs1,rs2,rd,0xffffff

    elif(opc(inst)==0x13):  # i format
        print("instruction is of i format(arithmetic)")
        if(fun3(inst)==0x0):
            print("instruction is addi")
            rs1=rs_1(inst)
            rd=r_d(inst)
            imm12=imm_12(inst)
            return 'addi',rs1,-1,rd,sign_extend(imm12,12)
        elif(fun3(inst)==0x7):
            print("instruction is andi")
            rs1=rs_1(inst)
            rd=r_d(inst)
            imm12=imm_12(inst)
            return 'andi',rs1,-1,rd,sign_extend(imm12,12)
        elif(fun3(inst)==0x6):
            print("instruction is ori")
            rs1=rs_1(inst)
            rd=r_d(inst)
            imm12=imm_12(inst)
            return 'ori',rs1,-1,rd,sign_extend(imm12,12)
    elif(opc(inst)==0x03):
        print("instruction is of i format(load)")
        if(fun3(inst)==0x0):
            print("instruction is lb")
            rs1=rs_1(inst)
            rd=r_d(inst)
            imm12=imm_12(inst)
            return 'lb',rs1,-1,rd,sign_extend(imm12,12)
        elif(fun3(inst)==0x1):
            print("instruction is lh")
            rs1=rs_1(inst)
            rd=r_d(inst)
            imm12=imm_12(inst)
            return 'lh',rs1,-1,rd,sign_extend(imm12,12)
        elif(fun3(inst)==0x2):
            print("instruction is lw")
            rs1=rs_1(inst)
            rd=r_d(inst)
            imm12=imm_12(inst)
            return 'lw',rs1,-1,rd,sign_extend(imm12,12)
    elif(opc(inst)==0x67 and fun3(inst)==0x0):
        print("instruction is of i format")
        print("instruction is jalr")
        rs1=rs_1(inst)
        rd=r_d(inst)
        imm12=imm_12(inst)
        return 'jalr',rs1,-1,rd,sign_extend(imm12,12)

    elif(opc(inst)==0x23):  # s format
        print("instruction is of s format")
        if(fun3(inst)==0x0):
            print("instruction is sb")
            rs1=rs_1(inst)
            rs2=rs_2(inst)
            imm5=r_d(inst) # imm[4:0] 5 bits
            imm7=fun_7(inst) #imm[11:5] 7 bits
            imm12=cals(imm7,imm5)
            return 'sb',rs1,rs2,-1,sign_extend(imm12,12)
        elif(fun3(inst)==0x1):
            print("instruction is sh")
            rs1=rs_1(inst)
            rs2=rs_2(inst)
            imm5=r_d(inst) # imm[4:0] 5 bits
            imm7=fun_7(inst) #imm[11:5] 7 bits
            imm12=cals(imm7,imm5)
            return 'sh',rs1,rs2,-1,sign_extend(imm12,12)
        elif(fun3(inst)==0x2):
            print("instruction is sw")
            rs1=rs_1(inst)
            rs2=rs_2(inst)
            imm5=r_d(inst) # imm[4:0] 5 bits
            imm7=fun_7(inst) #imm[11:5] 7 bits
            imm12=cals(imm7,imm5)
            return 'sw',rs1,rs2,-1,sign_extend(imm12,12)

    elif(opc(inst)==0x63):  # sb format
        print("instruction is of sb format(branch)")
        if(fun3(inst)==0x0):
            print("instruction is beq")
            rs1=rs_1(inst)
            rs2=rs_2(inst)
            imm5=r_d(inst) # imm[4:1]imm[11] 5 bits
            imm7=fun_7(inst) #imm[12]imm[10:5] 7 bits
            imm12=calsb(imm7,imm5)
            return 'beq',rs1,rs2,-1,sign_extend(imm12,12)
        elif(fun3(inst)==0x1):
            print("instruction is bne")
            rs1=rs_1(inst)
            rs2=rs_2(inst)
            imm5=r_d(inst) # imm[4:1]imm[11] 5 bits
            imm7=fun_7(inst) #imm[12]imm[10:5] 7 bits
            imm12=calsb(imm7,imm5)
            return 'bne',rs1,rs2,-1,sign_extend(imm12,12)
        elif(fun3(inst)==0x4):
            print("instruction is blt")
            rs1=rs_1(inst)
            rs2=rs_2(inst)
            imm5=r_d(inst) # imm[4:1]imm[11] 5 bits
            imm7=fun_7(inst) #imm[12]imm[10:5] 7 bits
            imm12=calsb(imm7,imm5)
            return 'blt',rs1,rs2,-1,sign_extend(imm12,12)
        elif(fun3(inst)==0x5):
            print("instruction is bge")
            rs1=rs_1(inst)
            rs2=rs_2(inst)
            imm5=r_d(inst) # imm[4:1]imm[11] 5 bits
            imm7=fun_7(inst) #imm[12]imm[10:5] 7 bits
            imm12=calsb(imm7,imm5)
            return 'bge',rs1,rs2,-1,sign_extend(imm12,12)

    elif(opc(inst)==0x17):   # u format
        print("instruction is of u format")
        print("instruction is auipc")
        rd=r_d(inst)
        imm20=imm_20(inst) #imm[31:12] 20 bits
        return 'auipc',-1,-1,rd,sign_extend(imm20,20)
    elif(opc(inst)==0x37):
        print("instruction is of u format")
        print("instruction is lui")
        rd=r_d(inst)
        imm20=imm_20(inst) #imm[19:0] 20 bits
        return 'lui',-1,-1,rd,sign_extend(imm20,20)

    elif(opc(inst)==0x6f):  # uj format
        print("instruction is of uj format")
        print("instruction is jal")
        rd=r_d(inst)
        imm19=(inst>>12)&0xff   # imm[19:12] 8 bits
        imm11=(inst>>20)&0x1    # imm[11] 1 bit
        imm10=(inst>>21)&0x3ff  # imm[10:1] 10 bits
        imm20=(inst>>31)&0x1    # imm[20] 1 bit
        imm11=(imm11<<10)|imm10 # imm[11:1] 11 bits
        imm19=(imm19<<11)|imm11 # imm[19:1] 19 bits
        imm20=(imm20<<19)|imm19 # imm[20:1] 20 bits
        return 'jal',-1,-1,rd,sign_extend(imm20,20)
    
    
    
