import urllib.request

TOKEN = "8554379476:AAHZf4qPgmiCQ5rOQCgovwJX88hSjJPf3iQ"
url = f"https://api.telegram.org/bot{TOKEN}/getMe"
resp = urllib.request.urlopen(url)
print(resp.read().decode())
