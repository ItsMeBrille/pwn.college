import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
PUSH rdi
PUSH rsi
POP rdi
POP rsi
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())