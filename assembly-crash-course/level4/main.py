import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
mov rax, rdi
imul rax, rsi
add rax, rdx
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())