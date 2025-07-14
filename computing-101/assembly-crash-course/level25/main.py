import pwn
pwn.context.update(arch="amd64")
code = pwn.asm(f"""
cmp rdi, 0x7F454C46
jmp addit
cmp rdi, 0x00005A4D
jmp subit

jmp imulit

addit:
MOV rbx, [rdi+4]
ADD rbx, [rdi+8]
ADD rbx, [rdi+12]
jmp done

subit:
MOV rbx, [rdi+4]
SUB rbx, [rdi+8]
SUB rbx, [rdi+12]
jmp done

imulit:
MOV rbx, [rdi+4]
IMUL rbx, [rdi+8]
IMUL rbx, [rdi+12]
jmp done

done:
MOV eax, ebx
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())