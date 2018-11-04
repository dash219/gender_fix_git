#takes two .json files and outputs where they differ in a .json file
import json

with open("persons_final.json", 'r') as fi:
	wat = json.load(fi)
fi.close()
arr1 = wat
arr2 = {}

i = 0
default = None
z = 0
while z < len(arr1):
	name = arr1[z]["last_name"] + ", " + arr1[z]["first_name"]
	while(arr2.get(name, default)):
		name += "0"
	arr2[name] = arr1[z]["gender"]
	z += 1

with open("persons_Convert.json", mode="w", encoding='utf-8') as f:
		json.dump(arr2, f, indent=4, sort_keys=True)