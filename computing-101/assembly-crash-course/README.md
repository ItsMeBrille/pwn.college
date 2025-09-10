# Assembly Crash Course

Python code to run the assembly:

```py
import pwn
pwn.context.update(arch="amd64")

code = pwn.asm("""
add rdi, 0x331337
""" )

io = pwn.process("/challenge/run")
io.write(code)
print(io.readall())
```


## Level 3
```asm
add rdi, 0x331337
```

## Level 4
```asm
mov rax, rdi
imul rax, rsi
add rax, rdx
```

## Level 5
```asm
mov rax, rdi
div rsi
```

## Level 6
```asm
mov rax, rdi
div rsi
mov rax, rdx
```

## Level 7
```asm
mov ah, 0x42
```

## Level 8
```asm
mov al, dil
mov bx, si
```

## Level 9
```asm
shr rdi, 0x20
mov al, dil
```

## Level 10
```asm
AND rax, rdi
AND rax, rsi
```

## Level 11
```asm
AND rax, rdi
AND rax, 0x01
XOR rax, 0x01
```

## Level 12
```asm
MOV rax, [0x404000]
```

## Level 13
```asm
MOV [0x404000], rax
```

## Level 14
```asm
MOV rax, [0x404000]
ADD DWORD PTR [0x404000], 0x1337
```

## Level 15
```asm
MOV rax, 0x00
MOV axl, [0x404000]
```

## Level 16
```asm
MOV rax, 0x00
MOV al, [0x404000]
MOV rbx, 0x00
MOV bx, [0x404000]
MOV rcx, 0x00
MOV ecx, [0x404000]
MOV rdx, [0x404000]
```

## Level 17
```asm
MOV rax, 0xdeadbeef00001337
MOV [rdi], rax
MOV rax, 0xc0ffee0000
MOV [rsi], rax
```

## Level 18
```asm
MOV rax, [rdi]
MOV rbx, [rdi+8]
ADD rax, rbx
MOV [rsi], rax
```

## Level 19
```asm
POP rax
SUB rax, rdi
PUSH rax
```

## Level 20
```asm
PUSH rdi
PUSH rsi
POP rdi
POP rsi
```

## Level 21
```asm
MOV rax, [rsp]
ADD rax, [rsp+0x8]
ADD rax, [rsp+0x10]
ADD rax, [rsp+0x18]
MOV rsi, 0x04
DIV rsi
PUSH rax
```

## Level 22
```asm
MOV rax, 0x403000
JMP rax
```

## Level 23
```asm
JMP .+0x53
{"nop;"*int("51", 16)}
MOV rax, 0x01
```

## Level 24
```asm
JMP .+0x53
{"nop;"*int("51", 16)}
POP rdi
MOV rax, 0x403000
JMP rax
```

## level 25
```asm
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
```
