#takes two .json files and outputs where they differ in a .json file
#reads from "verified_gender_mapping.json" and deletes its duplicates
#puts names not found in map_Convert.json into failed.json
import json

with open("map_Convert.json", 'r') as fi:
	wat = json.load(fi)
fi.close()
arr1 = wat
with open("verified_gender_mapping.json", 'r') as fi:
	wat = json.load(fi)
fi.close()
arr2 = wat
arr3 = {}

default = "Noodle"
i = 0
for ay in arr2:
	nam = ay.split()[0] + " "+ ay.split()[1]
	revnam = ay.split()[1] + ", " + ay.split()[0]
	revnam = revnam[:-1]
	if (arr1.get(nam, default) != default):
		del arr1[nam]
	elif (arr1.get(ay, default) != default):
		del arr1[ay]
	elif (arr1.get(revnam, default) != default):
		del arr1[revnam]
	else:
		r = 0
		ay2 = ay
		nam2 = nam
		revnam2 = revnam
		while(r < 4):
			ay2 += "0"
			nam2 += "0"
			revnam2 += "0"
			r += 1
			if(arr1.get(ay2,default) != default):
				del arr1[ay2]
				r = 5
			elif(arr1.get(nam2,default) != default):
				del arr1[nam2]
				r = 5
			elif(arr1.get(revnam2,default) != default):
				del arr1[revnam2]
				r = 5
		if(r == 4):
			arr3[ay] = arr2[ay]
			print(nam)

with open("genderize_gender_mapping.json", mode="w", encoding='utf-8') as f:
		json.dump(arr1, f, indent=4, sort_keys=True)
with open("failed.json", mode="w", encoding='utf-8') as f:
		json.dump(arr3, f, indent=4, sort_keys=True)		