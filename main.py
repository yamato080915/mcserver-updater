import sys, requests, json
arg = sys.argv[1:]

with open(f"{arg[0]}.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def get(url, header=None):
    return json.loads(requests.get(url=url, headers=header).text)

url ={"purpur": "https://api.purpurmc.org/v2/purpur"}

def update():
    latest = get(f"{url[data["software"]]}/{data["mcversion"]}")["builds"]["latest"]
    if data["build"] == latest:
        print("running latest version")
    else:
        print("downloading latest version")
        latData = requests.get(f"{url[data["software"]]}/{data["mcversion"]}/{latest}/download").content
        with open("./aho.zip", "wb") as f:
            f.write(latData)

if data["mcversion"] in get(url[data["software"]])["versions"]:
    if data["build"] in get(f"{url[data["software"]]}/{data["mcversion"]}")["builds"]["all"]:
        update()
    else:
        sys.exit()
else:
    sys.exit()