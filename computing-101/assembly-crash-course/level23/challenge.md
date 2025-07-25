
Welcome to ASMLevel23
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

We will now set some values in memory dynamically before each run. On each run
the values will change. This means you will need to do some type of formulaic
operation with registers. We will tell you which registers are set beforehand
and where you should put the result. In most cases, its rax.

In this level you will be working with control flow manipulation. This involves using instructions
to both indirectly and directly control the special register `rip`, the instruction pointer.
You will use instructions such as: jmp, call, cmp, and their alternatives to implement the requested behavior.



Recall that for all jumps, there are three types:
  Relative jumps
  Absolute jumps
  Indirect jumps

In this level we will ask you to do a relative jump.

You will need to fill space in your code with something to make this relative jump possible.

We suggest using the `nop` instruction. It's 1 byte long and very predictable.

In fact, the as assembler that we're using has a handy .rept directive that you can use to
repeat assembly instructions some number of times:
  https://ftp.gnu.org/old-gnu/Manuals/gas-2.9.1/html_chapter/as_7.html

Useful instructions for this level:
  jmp (reg1 | addr | offset) ; nop

Hint: for the relative jump, lookup how to use `labels` in x86.

Using the above knowledge, perform the following:
  Make the first instruction in your code a jmp
  Make that jmp a relative jump to 0x51 bytes from the current position
  At the code location where the relative jump will redirect control flow set rax to 0x1

We will now set the following in preparation for your code:
  Loading your given code at: 0x4000db

Please give me your assembly in bytes (up to 0x1000 bytes): 

