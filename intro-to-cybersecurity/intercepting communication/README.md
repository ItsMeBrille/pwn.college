# Intercepting Communication

##  Connect

```bash
nc 10.0.0.1 31337
```

pwn.college{g-L8M5I6wMivtEztAGCUxQoRiI5.dlTNzMDL5ETN1QzW}


## Send

```bash
nc 10.0.0.1 31337
Hello, World!
```
pwn.college{YL62zwXvS4WbgFs_kNdKvAz5ZsD.QX1IDM2EDL5ETN1QzW}


## Shutdown

`-N` sends a EOF through nc to say its finished sending.

```bash
nc -N 10.0.0.1 31337
```
pwn.college{Y_nYnr9mKB0j7BKXz7As1jztNsi.QX2IDM2EDL5ETN1QzW}


## Listen

Listen for incoming connections using `-l`

```bash
nc -l 10.0.0.1 31337
```
pwn.college{sCdl7KwQZt1-hwD4TsdYCUE-JEu.dBjNzMDL5ETN1QzW}


## Scan 1

Grep for successful ping:

```bash
for i in {10..254};
    do ping -c 1 -W 1 10.0.0.$i &
done | grep "1 rec" -B 1
```

Send all output to null, then at success echo the ip:

```bash
for i in {10..254}; do
    ping -c 1 -W 1 10.0.0.$i > /dev/null && echo "10.0.0.$i is alive" &
done
```

Then nc that ip:

```bash
nc 10.0.0.$i
```

pwn.college{sCdl7KwQZt1-hwD4TsdYCUE-JEu.dBjNzMDL5ETN1QzW}


## Scan 2

Listen for incoming connections using `-l`


```bash
nmap -Pn -p 31337 --open -T5 -n 10.0.0.0/16
```

pwn.college{AcZmAmcG4AVuFNdSScqLyqsZzi8.dJjNzMDL5ETN1QzW}