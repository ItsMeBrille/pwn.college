import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
shr rdi, 0x20
mov al, dil
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())