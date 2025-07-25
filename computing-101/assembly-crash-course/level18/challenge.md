
Welcome to ASMLevel18
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

In this level you will be working with memory. This will require you to read or write
to things stored linearly in memory. If you are confused, go look at the linear
addressing module in 'ike. You may also be asked to dereference things, possibly multiple
times, to things we dynamically put in memory for your use.



Recall that memory is stored linearly.

What does that mean?

Say we access the quad word at 0x1337:
  [0x1337] = 0x00000000deadbeef

The real way memory is layed out is byte by byte, little endian:
  [0x1337] = 0xef
  [0x1337 + 1] = 0xbe
  [0x1337 + 2] = 0xad
  ...
  [0x1337 + 7] = 0x00

What does this do for us?

Well, it means that we can access things next to each other using offsets,
similar to what was shown above.

Say you want the 5th *byte* from an address, you can access it like:
  mov al, [address+4]

Remember, offsets start at 0.

Perform the following:
  Load two consecutive quad words from the address stored in rdi
  Calculate the sum of the previous steps quad words.
  Store the sum at the address in rsi

We will now set the following in preparation for your code:
  [0x4041a0] = 0x348f0
  [0x4041a8] = 0xc32ed
  rdi = 0x4041a0
  rsi = 0x404668

Please give me your assembly in bytes (up to 0x1000 bytes): 

