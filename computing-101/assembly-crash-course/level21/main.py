import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
MOV rax, [rsp]
ADD rax, [rsp+0x8]
ADD rax, [rsp+0x10]
ADD rax, [rsp+0x18]
MOV rsi, 0x04
DIV rsi
PUSH rax
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())