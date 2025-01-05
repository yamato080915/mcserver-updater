import requests
url = [
    "https://api.papermc.io/v2/projects/paper/versions/1.16.5/builds/793/downloads/paper-1.16.5-793.jar",
    "https://api.purpurmc.org/v2/purpur/1.16.5/1170/download"
]
filename = ["./paper1165.jar","purpur1165.jar"]
for i in range(2):
    urlData = requests.get(url[i]).content
    with open(filename[i], "wb") as f:
        f.write(urlData)