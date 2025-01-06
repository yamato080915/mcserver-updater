import sys, requests, json, os

arg = sys.argv[1:]
if arg == []:sys.exit()

jarFile = arg[0]
configFile = f"{arg[0]}.json"

if len(arg) >= 2:
    configFile = arg[1]
elif arg[0][-5:] == ".json":
    configFile = os.path.abspath(arg[0])
    os.chdir(os.path.dirname(configFile))
#---------------------------------------------------
supportedSoftware = ["purpur", "paper", "velocity"]
#---------------------------------------------------
proxy = ["velocity"]

with open(configFile, "r", encoding="utf-8") as f:
    data = json.load(f)
    software = data["software"]
    ver = data["version"]
    if arg[0][-5:]==".json" and len(arg)==1:
        jarFile = data["file"]

if not software in supportedSoftware:sys.exit()

def get(url, header=None):
    return json.loads(requests.get(url=url, headers=header).text)

url ={
    "purpur": "https://api.purpurmc.org/v2/purpur", 
    "paper": "https://api.papermc.io/v2/projects/paper", 
    "velocity": "https://api.papermc.io/v2/projects/velocity"
    }

def update():
    global data
    latest = get(f"{url[software]}{"" if software=="purpur" else "/versions"}/{ver}")["builds"]
    if software == "purpur":latest = latest["latest"]
    else:latest = latest[-1]
    if data["build"] == latest:
        print("running the latest version")
    else:
        print("downloading the latest version")
        latData = requests.get(f"{url[software]}{"" if software=="purpur" else "/versions"}/{ver}{"" if software=="purpur" else "/builds"}/{latest}/download{"" if software=="purpur" else f"s/{software}-{ver}-{latest}.jar"}").content
        with open(jarFile, "wb") as f:
            f.write(latData)
        data["build"] = latest
        with open(configFile, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print("updated to the latest version")

if software in proxy:
    ver = get(url[software])["versions"][-1]
    data["version"] = ver
if ver in get(url[software])["versions"]:
    update()
else:
    sys.exit()