#!/usr/bin/python
"""
hypothetical assembler implementation
Dhruva Sahasrabudhe 111408051 T3 IT

"""

"""
read file, 

initialise mot, pot, pc, flag, symtab

for each line in file, tokenize (according to spaces),

for each token do:
    check if in mot/pot/symtab
        1),if word has ':' definitely keyword, add to symtab along with address
        2)check if in cs or ds, if in cs, check only mot
        3)if in ds, check pot, symtab, add 
    if not in any of them, add name to symtab but no address
    at endp change flag to ds

"""
from collections import namedtuple


MOT_tup = namedtuple("MOT_tup","mnem_op symb_op num_operands len")
POT_tup = namedtuple("POT_tup","mnem_op num_operands")
MOT = [
MOT_tup("add", 1, 1, 2),
MOT_tup("sub", 2, 1, 2),
MOT_tup("mult", 3, 1, 2),
MOT_tup("jmp", 4, 1, 2),
MOT_tup("jpos", 5, 1, 2),
MOT_tup("jneg", 6, 1, 2),
MOT_tup("jz", 7, 1, 2),
MOT_tup("load", 8, 1, 2),
MOT_tup("store", 9, 1, 2),
MOT_tup("read", 10, 1, 2),
MOT_tup("write", 11, 1, 2),
MOT_tup("stop", 12, 0, 1)
]

POT = [
POT_tup("db", 1),
POT_tup("dw", 1),
POT_tup("org", 1),
POT_tup("endp", 0),
POT_tup("end", 0),
POT_tup("const", 1)
]

symtab = dict()
csflag = 0
pc = 0
tokentype = []


"""
for val in MOT:
    print val.mnem_op, val.symb_op, val.num_operands, val.len

"""

def buildsymtab(token):
    global MOT, POT, symtab, csflag, pc
    if token.isdigit() or token == "?":
        return
    if token == "endp" and csflag == 1:
        csflag = 0
        return
    if token.find(":") != -1:
        symtab[token.strip(':')] = pc
        return

    else:
        if csflag == 1: 
            for entry in MOT:
                if entry.mnem_op == token:
                    pc += entry.len
                    return

            if token not in symtab.keys():
                symtab[token] = ''
                return

        elif csflag == 0:
            for entry in POT:
                if entry.mnem_op == token:
                    pc += 1
                    return
            symtab[token] = pc
    
    return

def printsymtab():
    global symtab
    print "Symbol table at the end of pass one:\n"
    print "|Symbol\t|Address|"
    for symbol in symtab:
        print "|",symbol,"\t|",symtab[symbol],"\t|"
    return

def passone():
    global csflag, pc
    as_file = open(raw_input("Enter the source filename\n"))
    target = open(raw_input("Enter the target filename\n"), "w+")
    csflag = 1
    pc = 0
    for line in as_file:
        ltokens = line.strip("\n").split(" ")
        #print ltokens
        for token in ltokens:
            buildsymtab(token)
    printsymtab()     
    pc = 0
    as_file.seek(0)
    target.seek(0)
    passtwo(as_file, target)
    return
    

def passtwo(as_file, target):
    global MOT, POT, pc, symtab, csflag
    csflag = 1
    target.write("%s. "%(pc))
    
    for line in as_file:
        ltokens = line.split(" ")
        for token in ltokens:
            if token.strip("\n").isdigit() or token.strip("\n") == "?":
                target.write("%s "%(token.strip("\n")))
                
                if token.find("\n") != -1:
                    if csflag == 0:
                        pc+=1
                    target.write("\n%s. "%(pc))
                continue

            if token.strip("\n").find(":") != -1:
                continue

            if token.strip("\n") == "endp" and csflag == 1:
                csflag = 0

            if csflag == 1:
                for entry in MOT:
                    if token.strip("\n") == entry.mnem_op:
                        target.write("%s "%(entry.symb_op))
                        pc += entry.len
                        if token.find("\n") != -1:
                            target.write("\n%s. "%(pc))
                        continue
                for entry in symtab:
                    if token.strip("\n") == entry:
                        target.write("%s "%(str(symtab[entry])))
                        if token.find("\n") != -1:
                            target.write("\n%s. "%(pc))
                        continue

    as_file.close()
    target.close()
    return




if __name__=="__main__":
    passone()
