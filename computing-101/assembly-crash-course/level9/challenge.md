
Welcome to ASMLevel9
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



Shifting bits around in assembly is another interesting concept!

x86 allows you to 'shift' bits around in a register.

Take, for instance, al, the lowest 8 bits of rax.

The value in al (in bits) is:
  rax = 10001010

If we shift once to the left using the shl instruction:
  shl al, 1

The new value is:
  al = 00010100

Everything shifted to the left and the highest bit fell off
while a new 0 was added to the right side.

You can use this to do special things to the bits you care about.

Shifting has the nice side affect of doing quick multiplication (by 2)
or division (by 2), and can also be used to compute modulo.

Here are the important instructions:
  shl reg1, reg2       <=>     Shift reg1 left by the amount in reg2
  shr reg1, reg2       <=>     Shift reg1 right by the amount in reg2
  Note: 'reg2' can be replaced by a constant or memory location

Using only the following instructions:
  mov, shr, shl

Please perform the following:
  Set rax to the 5th least significant byte of rdi.

For example:
  rdi = | B7 | B6 | B5 | B4 | B3 | B2 | B1 | B0 |
  Set rax to the value of B4

We will now set the following in preparation for your code:
  rdi = 0x83173aeada992096

Please give me your assembly in bytes (up to 0x1000 bytes): 

