import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
MOV rax, [rdi]
MOV rbx, [rdi+8]
ADD rax, rbx
MOV [rsi], rax
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())