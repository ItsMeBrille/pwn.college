# Cryptography

## XORing ASCII

```py
chr(ord("@") ^ 0x13)
```

## XORing ASCII Strings

```py
from Crypto.Util.strxor import strxor
strxor(num1, num2)
```

## One-time Pad

```py
import pwn
from Crypto.Util.strxor import strxor

io = pwn.process('/challenge/run')

io.recvuntil(b":")
num1 = bytes.fromhex(io.recvuntil(b"\n").decode().strip())
io.recvuntil(b":")
num2 = bytes.fromhex(io.recvuntil(b"\n").decode().strip())

print(strxor(num1, num2))    
```

## One-time Pad Tampering

```py
strxor(bytes.fromhex("f200c780c6"), strxor(b"flag!", b"sleep")).hex()
```


## Many-time Pad

Decrypt one to learn key. Then find flag.

```py
import pwn
from Crypto.Util.strxor import strxor

io = pwn.process('/challenge/run')

# Flag
io.recvuntil(b"Flag Ciphertext (hex): ")
flag = bytes.fromhex(io.recvuntil(b"\n", drop=True).decode())

# Plaintext
pt = b"A" * 256
io.sendlineafter(b"Plaintext (hex):", pt)
pt = bytes.fromhex(pt.decode())

# Ciphertext
io.recvuntil(b"Ciphertext (hex): ")
ct = bytes.fromhex(io.recvuntil(b"\n", drop=True).decode())

# Key
key = strxor(pt, ct)

# Solve flag with key
result = strxor(flag, key[:len(flag)])

print(result)    

io.close()
```