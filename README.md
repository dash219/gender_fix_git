gender_fix_git
Continued work on Summer 2018 employment; graphing data for gender distributions in CS academia.


------------------------------------------------------------------------------------------------
1) create "genderize_results_less8.json"
	-> set all genders w/ p<0.8 in genderize_results_noconf.json to null
	...DONE

2) create "genderize_gender_mapping.json"
	-> the difference between genderize_results_less8.json and verified_gender_mapping.json
	...DONE, had to fix duplicates in verified_gender_mapping.json

3) create "persons_post_genderize.csv" (optional step, useful for graphing)
	-> combine data from genderize_results_less8.json with persons.csv

4) create "persons_final.json"
	-> hand-verify remaining null names in genderize_results_less8.json as best as possible
	-> useful to use university data from persons.csv
	...need time

5) create "verified_gender_mapping_final.json"
	-> the difference between persons_final.json and genderize_gender_mapping.json
	...NEED "persons_final.json" FROM 4)

6) create "persons_final.csv"
	-> combine data from persons_final.json with persons.csv
	...NEED "persons_final.json" FROM 4)

7) re-run the R file that creates the graphs using persons_final.csv
