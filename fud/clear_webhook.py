import urllib.request, json

TOKEN = "8554379476:AAHZf4qPgmiCQ5rOQCgovwJX88hSjJPf3iQ"

# Delete webhook
url = f"https://api.telegram.org/bot{TOKEN}/deleteWebhook"
req = urllib.request.Request(url, method="POST")
resp = urllib.request.urlopen(req)
print("deleteWebhook:", resp.read().decode())

# Get webhook info
url2 = f"https://api.telegram.org/bot{TOKEN}/getWebhookInfo"
resp2 = urllib.request.urlopen(url2)
print("getWebhookInfo:", resp2.read().decode())
