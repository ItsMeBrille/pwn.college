import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
MOV [0x404000], rax
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())