# Program Interaction

Below are brief explanations and minimal code snippets for each level from 8 to 54.


## Bash

### Level 8

Run the binary directly.

```bash
/challenge/embryoio_level8
```


### Level 9

Run the binary directly.

```bash
/challenge/embryoio_level9
```


### Level 10

Provide the required argument.

```bash
/challenge/embryoio_level10 wghqomoiep
```


### Level 11

Set the required environment variable.

```bash
env jinbxc=uuzezdplfx /challenge/embryoio_level11
```


### Level 12

Redirect input from a file.

```bash
env /challenge/embryoio_level12 < /tmp/kzgaox
```


### Level 13

Redirect output to a file.

```bash
env /challenge/embryoio_level13 > /tmp/pxfpyh
```


### Level 14

Run with an empty environment.

```bash
env -i /challenge/embryoio_level14
```


## Python

### Level 15

Run the binary directly.

```python
from pwn import *
p = process(['/challenge/embryoio_level15'])
p.interactive()
```


### Level 16

Run the binary directly.

```python
from pwn import *
p = process(['/challenge/embryoio_level16'])
p.interactive()
```


### Level 17

Provide the required argument.

```python
from pwn import *
p = process(['/challenge/embryoio_level17', 'jivlxzhtri'])
p.interactive()
```


### Level 18

Set the required environment variable.

```python
from pwn import *
p = process(['/challenge/embryoio_level18'], env={'zdfuhr': 'rrxxbtnuky'})
p.interactive()
```


### Level 19

Redirect input from a file.

```python
from pwn import *
p = process(['/challenge/embryoio_level19'], stdin=open('/tmp/ajasug', 'r'))
p.interactive()
```


### Level 20

Redirect output to a file, then read it.

```python
from pwn import *
p = process(['/challenge/embryoio_level20'], stdout=open('/tmp/dkihjg', 'w'))
p.interactive()
q = process(['cat', '/tmp/dkihjg'])
q.interactive()
```


### Level 21

Run with an empty environment.

```python
from pwn import *
p = process(['env', '-i', '/challenge/embryoio_level21'])
p.interactive()
```


### Level 22

Run the binary directly.

```python
from pwn import *
p = process(['/challenge/embryoio_level22'])
p.interactive()
```


### Level 23

Run the binary directly.

```python
from pwn import *
p = process(['/challenge/embryoio_level23'])
p.interactive()
```


### Level 24

Provide the required argument.

```python
from pwn import *
p = process(['/challenge/embryoio_level24', 'kfcrhcrdqk'])
p.interactive()
```


### Level 25

Set the required environment variable.

```python
from pwn import *
p = process(['/challenge/embryoio_level25'], env={'fimoun': 'shspjejaxc'})
p.interactive()
```


### Level 26

Pipe output from `echo` to the binary.

```python
from pwn import *
o = process(['echo', 'trjvnbxk'], stdout=open('/tmp/eunodh', 'w'))
p = process(['/challenge/embryoio_level26'], stdin=open('/tmp/eunodh', 'r'))
p.interactive()
```


### Level 27

Redirect output to a file, then read it.

```python
from pwn import *
p = process(['/challenge/embryoio_level27'], stdout=open('/tmp/fnnofu', 'w'))
p.interactive()
q = process(['cat', '/tmp/fnnofu'])
q.interactive()
```


### Level 28

Run with an empty environment.

```python
from pwn import *
p = process(['env', '-i', '/challenge/embryoio_level28'])
p.interactive()
```


## C

### Level 29

Run the binary directly.

```c
pid_t pid = fork();
if (pid == 0) {
    char *args[] = {"/challenge/embryoio_level29", NULL};
    execv(args[0], args);
}
wait(NULL);
```


### Level 30

Run the binary directly.

```c
pid_t pid = fork();
if (pid == 0) {
    char *args[] = {"/challenge/embryoio_level30", NULL};
    execv(args[0], args);
}
wait(NULL);
```


### Level 31

Provide the required argument.

```c
pid_t pid = fork();
if (pid == 0) {
    char *args[] = {"/challenge/embryoio_level31", "ysmmolmblt", NULL};
    execv(args[0], args);
}
wait(NULL);
```


### Level 32

Set the required environment variable.

```c
pid_t pid = fork();
if (pid == 0) {
    char *args[] = {"/challenge/embryoio_level32", NULL};
    char *envp[] = {"cqwqxs=wqodsyxfsq", NULL};
    execve(args[0], args, envp);
}
wait(NULL);
```


### Level 33

Redirect input from a file.

```c
pid_t pid = fork();
if (pid == 0) {
    FILE *file = fopen("/tmp/brxhzr", "r");
    dup2(fileno(file), STDIN_FILENO);
    fclose(file);
    char *args[] = {"/challenge/embryoio_level33", NULL};
    execv(args[0], args);
}
wait(NULL);
```


### Level 34

Redirect output to a file, then read it.

```c
pid_t pid = fork();
if (pid == 0) {
    FILE *file = fopen("/tmp/tfzgke", "w");
    dup2(fileno(file), STDOUT_FILENO);
    fclose(file);
    char *args[] = {"/challenge/embryoio_level34", NULL};
    execv(args[0], args);
}
wait(NULL);
pid_t pid2 = fork();
if (pid2 == 0) {
    char *args[] = {"cat", "/tmp/tfzgke", NULL};
    execv("/bin/cat", args);
}
wait(NULL);
```


### Level 35

Run with an empty environment.

```c
pid_t pid = fork();
if (pid == 0) {
    char *args[] = {"env", "-i", "/challenge/embryoio_level35", NULL};
    execvp(args[0], args);
}
wait(NULL);
```


## Python Subprocess

### Level 48

Pipe output through `cat`.

```python
import subprocess

process1 = subprocess.Popen(['/challenge/embryoio_level48'], stdout=subprocess.PIPE)
process2 = subprocess.Popen(['cat'], stdin=process1.stdout, stdout=subprocess.PIPE)
output, _ = process2.communicate()
print(output.decode())
```


### Level 49

Pipe output through `grep` to filter lines.

```python
import subprocess

process1 = subprocess.Popen(['/challenge/embryoio_level49'], stdout=subprocess.PIPE)
process2 = subprocess.Popen(['grep', '{'], stdin=process1.stdout, stdout=subprocess.PIPE)
output, _ = process2.communicate()
print(output.decode())
```


### Level 50

Pipe output through `sed`.

```python
import subprocess

process1 = subprocess.Popen(['/challenge/embryoio_level50'], stdout=subprocess.PIPE)
process2 = subprocess.Popen(['sed', ''], stdin=process1.stdout, stdout=subprocess.PIPE)
output, _ = process2.communicate()
print(output.decode())
```


### Level 51

Reverse output twice.

```python
import subprocess

process1 = subprocess.Popen(['/challenge/embryoio_level51'], stdout=subprocess.PIPE)
process2 = subprocess.Popen(['rev'], stdin=process1.stdout, stdout=subprocess.PIPE)
process3 = subprocess.Popen(['rev'], stdin=process2.stdout, stdout=subprocess.PIPE)
output, _ = process3.communicate()
print(output.decode())
```


### Level 52

Pipe input from `cat` to the binary.

```python
import subprocess

process1 = subprocess.Popen(['cat'], stdout=subprocess.PIPE)
process2 = subprocess.Popen(['/challenge/embryoio_level52'], stdin=process1.stdout, stdout=subprocess.PIPE)
output, _ = process2.communicate()
print(output.decode())
```


### Level 53

Reverse twice, then pipe to the binary.

```python
import subprocess

x = subprocess.Popen(['rev'], stdout=subprocess.PIPE)
y = subprocess.Popen(['rev'], stdin=x.stdout, stdout=subprocess.PIPE)
out = subprocess.Popen(['/challenge/embryoio_level53'], stdin=y.stdout, stdout=subprocess.PIPE)
r, e = out.communicate()
print(r.decode())
```


### Level 54

Same as Level 53, but for level 54.

```python
import subprocess

x = subprocess.Popen(['rev'], stdout=subprocess.PIPE)
y = subprocess.Popen(['rev'], stdin=x.stdout, stdout=subprocess.PIPE)
out = subprocess.Popen(['/challenge/embryoio_level54'], stdin=y.stdout, stdout=subprocess.PIPE)
r, e = out.communicate()
print(r.decode())
```