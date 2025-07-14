import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
MOV rax, 0x00
MOV al, [0x404000]
MOV rbx, 0x00
MOV bx, [0x404000]
MOV rcx, 0x00
MOV ecx, [0x404000]
MOV rdx, [0x404000]
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())