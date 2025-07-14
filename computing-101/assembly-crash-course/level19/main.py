import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
POP rax
SUB rax, rdi
PUSH rax
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())