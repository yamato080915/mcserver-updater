import sys, requests, json
arg = sys.argv[1:]

with open(f"{arg[0]}.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def get(url, header=None):
    return json.loads(requests.get(url=url, headers=header).text)

url ={"purpur": "https://api.purpurmc.org/v2/purpur"}

def update():
    global data
    latest = get(f"{url[data["software"]]}/{data["mcversion"]}")["builds"]["latest"]
    if data["build"] == latest:
        print("running the latest version")
    else:
        print("downloading the latest version")
        latData = requests.get(f"{url[data["software"]]}/{data["mcversion"]}/{latest}/download").content
        with open(arg[0], "wb") as f:
            f.write(latData)
        data["build"] = latest
        with open(f"{arg[0]}.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print("updated to the latest version")

if data["mcversion"] in get(url[data["software"]])["versions"]:
    if data["build"] in get(f"{url[data["software"]]}/{data["mcversion"]}")["builds"]["all"]:
        update()
    else:
        sys.exit()
else:
    sys.exit()