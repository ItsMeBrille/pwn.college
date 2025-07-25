
Welcome to ASMLevel21
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

In this level you will be working with the stack, the memory region that dynamically expands
and shrinks. You will be required to read and write to the stack, which may require you to use
the pop and push instructions. You may also need to use the stack pointer register (rsp) to know
where the stack is pointing.



In the previous levels you used push and pop to store and load data from the stack.

However you can also access the stack directly using the stack pointer.

On x86, the stack pointer is stored in the special register, rsp.
rsp always stores the memory address of the top of the stack,
i.e. the memory address of the last value pushed.

Similar to the memory levels, we can use [rsp] to access the value at the memory address in rsp.

Without using pop, please calculate the average of 4 consecutive quad words stored on the stack.

Push the average on the stack.

Hint:
  RSP+0x?? Quad Word A
  RSP+0x?? Quad Word B
  RSP+0x?? Quad Word C
  RSP      Quad Word D

We will now set the following in preparation for your code:
  (stack) [0x7fffff200000:0x7fffff1fffe0] = ['0x1d1efa75', '0xaea312f', '0xb0dff9c', '0x1577c722'] (list of things)

Please give me your assembly in bytes (up to 0x1000 bytes): 

