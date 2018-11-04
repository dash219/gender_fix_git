#takes two .json files and outputs where they differ in a .json file
import json

with open("genderize_results_less8.json", 'r') as fi:
	wat = json.load(fi)
fi.close()
arr1 = wat
arr2 = {}

i = 0
default = "Noodle"
z = 0
while z < len(arr1):
	r = len(arr2)
	name = arr1[z]["last_name"] + ", " + arr1[z]["first_name"]
	while(arr2.get(name, default) != default):
		name += "0"
	arr2[name] = arr1[z]["gender"]
	if(len(arr2) == r):
		print(name)
		print("WHAT")
		z = len(arr1)
	z += 1

with open("map_Convert.json", mode="w", encoding='utf-8') as f:
		json.dump(arr2, f, indent=4, sort_keys=True)