import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
MOV rax, [0x404000]
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())