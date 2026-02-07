import requests
import time

def test_server():
    url = "http://127.0.0.1:5000/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("✅ Server is reachable and serving index.html")
        else:
            print(f"❌ Server returned status code: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server. Is it running?")

if __name__ == "__main__":
    time.sleep(2) # Wait for server to start
    test_server()
