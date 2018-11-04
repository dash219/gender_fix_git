#sets genders where p<0.8 to null
import json

with open("genderize_results_noconf.json", 'r') as fi:
	wat = json.load(fi)
fi.close()
arr1 = wat

z = 0
while z < len(arr1):
	print(arr1[z])
	currname = arr1[z]['first_name']
	g1 = arr1[z]['gender']
	if (arr1[z]['gender'] != None):
		if (arr1[z]['probability'] < 0.8):
			arr1[z]['gender'] = None
	z += 1
print(arr1)
with open("genderize_results_less8.json", mode="w", encoding='utf-8') as f:
		json.dump(arr1, f, indent=4, sort_keys=True)
