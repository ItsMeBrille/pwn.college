
Welcome to ASMLevel22
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



Earlier, you learned how to manipulate data in a pseudo-control way, but x86 gives us actual
instructions to manipulate control flow directly.

There are two major ways to manipulate control flow:
 through a jump;
 through a call.

In this level, you will work with jumps.

There are two types of jumps:
  Unconditional jumps
  Conditional jumps

Unconditional jumps always trigger and are not based on the results of earlier instructions.

As you know, memory locations can store data and instructions.

Your code will be stored at 0x4000e1 (this will change each run).

For all jumps, there are three types:
  Relative jumps: jump + or - the next instruction.
  Absolute jumps: jump to a specific address.
  Indirect jumps: jump to the memory address specified in a register.

In x86, absolute jumps (jump to a specific address) are accomplished by first putting the target address in a register reg, then doing jmp reg.

In this level we will ask you to do an absolute jump.

Perform the following:
  Jump to the absolute address 0x403000

We will now set the following in preparation for your code:
  Loading your given code at: 0x4000e1

Please give me your assembly in bytes (up to 0x1000 bytes): 

