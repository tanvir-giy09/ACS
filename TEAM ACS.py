import os
import time
import requests

os.system("clear")

print("===================================")
print("🔰 Bangla SMS Bomber [0.1]")
print("🧑‍💻 ACS TEAM TANVIR")
print("📛 SMS BOMBER")
print("===================================")

# User Input
number = input("📱 নাম্বার দিন (e.g. 017XXXXXXX): ")
amount = int(input("💣 কয়টা SMS পাঠাবো?: "))

print("\n🚀 বোমিং শুরু...\n")

# Fake/Testing API (textbelt demo)
for i in range(amount):
    try:
        response = requests.post("https://textbelt.com/text", {
            'phone': number,
            'message': '🔐 This is a test SMS from Termux!',
            'key': 'textbelt',
        })

        if response.json()['success']:
            print(f"[{i+1}] ✔️ পাঠানো হয়েছে ✅")
        else:
            print(f"[{i+1}] ❌ ব্লক করেছে (Rate Limit?)")

        time.sleep(1)  # Control পাঠানোর গতি

    except:
        print(f"[{i+1}] ❌ কোথাও ত্রুটি!")

print("\n✅ বোমিং শেষ! ধন্যবাদ 🫡")
