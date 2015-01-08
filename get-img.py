import json, requests

def updateperson(person):
	token = "a5e92af24222b2218d6b6a2c073ef017bf67123c"
	userdata = requests.get("https://api.github.com/users/"+person["github"], auth=(token, "")).json()

	person["image"] = userdata["avatar_url"]
	person["githuburl"] = "www.github.com/"+person["github"]

	return person

##

with open("./jade/index.json") as jsonfile:
	index = json.load(jsonfile)

index["teachers"] = map(updateperson, index["teachers"])
index["ninjas"] = map(updateperson, index["ninjas"])

with open("./jade/index.json", "w") as jsonfile:
	json.dump(index, jsonfile, indent=4, separators=(',', ': '))