
Welcome to ASMLevel10
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

In this level you will be working with bit logic and operations. This will involve heavy use of
directly interacting with bits stored in a register or memory location. You will also likely
need to make use of the logic instructions in x86: and, or, not, xor.



Bitwise logic in assembly is yet another interesting concept!
x86 allows you to perform logic operations bit by bit on registers.

For the sake of this example say registers only store 8 bits.

The values in rax and rbx are:
  rax = 10101010
  rbx = 00110011

If we were to perform a bitwise AND of rax and rbx using the
"and rax, rbx" instruction, the result would be calculated by
ANDing each bit pair 1 by 1 hence why it's called a bitwise
logic.

So from left to right:
  1 AND 0 = 0
  0 AND 0 = 0
  1 AND 1 = 1
  0 AND 1 = 0
  ...

Finally we combine the results together to get:
  rax = 00100010

Here are some truth tables for reference:
      AND          OR           XOR
   A | B | X    A | B | X    A | B | X
  ---+---+---  ---+---+---  ---+---+---
   0 | 0 | 0    0 | 0 | 0    0 | 0 | 0
   0 | 1 | 0    0 | 1 | 1    0 | 1 | 1
   1 | 0 | 0    1 | 0 | 1    1 | 0 | 1
   1 | 1 | 1    1 | 1 | 1    1 | 1 | 0

Without using the following instructions:
  mov, xchg

Please perform the following:
  rax = rdi AND rsi

i.e. Set rax to the value of (rdi AND rsi)

We will now set the following in preparation for your code:
  rdi = 0x9223251b3fa272be
  rsi = 0x95f1e5a681a90cab

Please give me your assembly in bytes (up to 0x1000 bytes): 

