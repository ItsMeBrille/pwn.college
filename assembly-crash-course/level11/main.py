import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
AND rax, rdi
AND rax, 0x01
XOR rax, 0x01
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())