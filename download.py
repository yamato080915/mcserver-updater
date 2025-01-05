import requests
url = "https://api.purpurmc.org/v2/purpur/1.16.5/1170/download"
filename = "./purpur1165.jar"

urlData = requests.get(url).content
with open(filename, "wb") as f:
    f.write(urlData)