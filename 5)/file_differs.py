#takes two .json files and outputs where they differ in a .json file
import json

with open("persons_Convert.json", 'r') as fi:
	wat = json.load(fi)
fi.close()
arr1 = wat
with open("genderize_gender_mapping.json", 'r') as fi:
	wat = json.load(fi)
fi.close()
arr2 = wat
arr3 = {}

default = None
i = 0
for ay in arr2:
	nam = ay.split()[0] + " "+ ay.split()[1]
	if (arr1.get(nam, default)):
		del arr1[nam]
	elif (arr1.get(ay, default)):
		del arr1[ay]
	else:
		arr3[ay] = arr2[ay]
		print(nam)

with open("verified_gender_mapping_final.json", mode="w", encoding='utf-8') as f:
		json.dump(arr1, f, indent=4, sort_keys=True)
with open("failed.json", mode="w", encoding='utf-8') as f:
		json.dump(arr3, f, indent=4, sort_keys=True)		