
Welcome to ASMLevel6
==================================================

To interact with any level you will send raw bytes over stdin to this program.
To efficiently solve these problems, first run it to see the challenge instructions.
Then craft, assemble, and pipe your bytes to this program.

For instance, if you write your assembly code in the file asm.S, you can assemble that to an object file:
  as -o asm.o asm.S

Note that if you want to use Intel syntax for x86 (which, of course, you do), you'll need to add the following to the start of asm.S:
  .intel_syntax noprefix

Then, you can copy the .text section (your code) to the file asm.bin:
  objcopy -O binary --only-section=.text asm.o asm.bin

And finally, send that to the challenge:
  cat ./asm.bin | /challenge/run

You can even run this as one command:
  as -o asm.o asm.S && objcopy -O binary --only-section=.text ./asm.o ./asm.bin && cat ./asm.bin | /challenge/run

In this level you will be working with registers. You will be asked to modify
or read from registers.

We will now set some values in memory dynamically before each run. On each run
the values will change. This means you will need to do some type of formulaic
operation with registers. We will tell you which registers are set beforehand
and where you should put the result. In most cases, its rax.



Modulo in assembly is another interesting concept!

x86 allows you to get the remainder after a div operation.

For instance: 10 / 3 -> remainder = 1

The remainder is the same as modulo, which is also called the "mod" operator.

In most programming languages we refer to mod with the symbol '%'.

Please compute the following:
  rdi % rsi

Place the value in rax.

We will now set the following in preparation for your code:
  rdi = 0x15e710b8
  rsi = 0x3fff

Please give me your assembly in bytes (up to 0x1000 bytes): 
^[[A
Executing your code...
---------------- CODE ----------------
0x400000:	sbb   	ebx, dword ptr [rbx + 0x41]
--------------------------------------

Your program has crashed!
Invalid memory read (UC_ERR_READ_UNMAPPED)
This was the state of your program on crash:
+--------------------------------------------------------------------------------+
| Registers                                                                      |
+-------+----------------------+-------+----------------------+------------------+
|  rax  |  0xffffffffffffffff  |  rbx  |  0x0000000000000000  |                  |
|  rcx  |  0x0000000000000000  |  rdx  |  0x0000000000000000  |                  |
|  rsi  |  0x0000000000003fff  |  rdi  |  0x0000000015e710b8  |                  |
|  rbp  |  0x0000000000000000  |  rsp  |  0x00007fffff200000  |                  |
|  r8   |  0x0000000000000000  |  r9   |  0x0000000000000000  |                  |
|  r10  |  0x0000000000000000  |  r11  |  0x0000000000000000  |                  |
|  r12  |  0x0000000000000000  |  r13  |  0x0000000000000000  |                  |
|  r14  |  0x0000000000000000  |  r15  |  0x0000000000000000  |                  |
|  rip  |  0x0000000000400000  |       |                      |                  |
+---------------------------------+-------------------------+--------------------+
| Stack location                  | Data (bytes)            | Data (LE int)      |
+---------------------------------+-------------------------+--------------------+
+---------------------------------+-------------------------+--------------------+
| Memory location                 | Data (bytes)            | Data (LE int)      |
+---------------------------------+-------------------------+--------------------+
|    0x0000000000404000 (+0x0000) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
|    0x0000000000404008 (+0x0008) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
