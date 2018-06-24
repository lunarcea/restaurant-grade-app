import json
import texttable
from texttable import Texttable

####################################################################################
####################################################################################

def get_data(data_url):
	content = json.load(data_url) 
	return content

####################################################################################
####################################################################################

def search_start(content):
	original_length = len(content)
	header = "Find restaurants with critical health code violations"
	t = Texttable()
	t.header(['NAME', 'ADDRESS', "CATEGORY", "LEVEL", "DESCRIPTION", "GRADE", "DATE_ISSUED", "DATE_EXPIRED"])
	t.set_cols_width([20, 40, 20, 15, 50, 5, 20, 20])
	print("")
	print("-" * len(header))
	print(header.upper())
	print("-" * len(header))
	content = get_critical(content)
	content = search_name(content)
	print("-" * 50)
	content = search_zip(content)
	print("-" * 50)
	content = search_category(content)
	print("-" * 50)
	content = search_grade(content)
	print("-" * 50)
	for b in content:
		restaurant_address = str(b[10]) + " " + str(b[11]) + ", " + str(b[9]) + ", New York, " + str(b[12])
		t.add_row([b[8], restaurant_address, b[13], b[15], b[14], b[17], b[18], b[19]])
	print("")
	print("*" * 50)
	print("******  RESULTS  ******")
	print("*" * 50)
	print("")
	print(t.draw())

####################################################################################
####################################################################################

def get_critical(content):
	new_results = []
	for a in content["data"]:
		if a[15] == "Critical":
			new_results.append(a)
	return new_results

####################################################################################
####################################################################################

def search_name(content):
	new_results = []
	print("(1.) Please enter a restaurant name to filter by. If you wish to skip filtering by restaurant name, please leave the following line blank.")
	prompt_text = "Restaurant Name: "
	print("-" * (len(prompt_text)-1))
	name_search = input(prompt_text)
	print("-" * (len(name_search) + len(prompt_text)))
	if len(str(name_search)) > 0:
		for a in content:
			if (name_search in a[8] or name_search.title() in a[8] or name_search.capitalize() in a[8] or name_search.upper() in a[8] or name_search.lower() in a[8]) and (a[15] == "Critical"):
				new_results.append(a)
		if len(new_results) == 0:
			print("There were no results for your search. Would you like to try another name?")
			redo_name_search = input("Yes/No: ")
			if redo_name_search == "Yes" or redo_name_search == "yes" or redo_name_search == "y" or redo_name_search == "Y":
				return search_name(content)
			elif redo_name_search == "No" or redo_name_search == "no" or redo_name_search == "n" or redo_name_search == "N":
				return content
		else:
			matching = "*** " + str(len(new_results)) + " restaurants with a matching name ***".upper()
			print("")
			print("*" * len(matching))
			print(matching)
			print("*" * len(matching))
			print("")
		return new_results

	else:
		return content

####################################################################################
####################################################################################

def search_zip(content):
	content = content
	print("(2.) Please enter a zipcode to filter by. If you wish to skip filtering by zipcode, please leave the following line blank.")
	zip_search = input("Zipcode: ")
	
	if len(str(zip_search)) > 0:
		if len(str(zip_search)) > 5:
			print("Error, too many numbers!")
			print("")
			print("Please enter a valid zip code: ")
			print("")
			search_zip(content)
		elif len(str(zip_search)) < 5:
			print("Error, too few numbers!")
			print("")
			print("Please enter a valid zip code: ")
			search_zip(content)
		elif len(str(zip_search)) == 5:
			return zip_in_data(content, zip_search)

	return content

####################################################################################
####################################################################################

def search_category(content):
	new_results = []
	print("(3.) Please enter a restaurant category to filter by. If you wish to skip filtering by restaurant category, please leave the following line blank.")
	prompt_text = "Restaurant Category: "
	print("-" * (len(prompt_text)-1))
	category_search = input(prompt_text)
	print("-" * (len(category_search) + len(prompt_text)))

	for a in content:
		if str(category_search) in str(a[13]) or str(category_search).lower() in str(a[13]) or str(category_search).upper() in str(a[13]) or str(category_search).title() in str(a[13]) or  str(category_search).capitalize() in str(a[13]): 
			new_results.append(a)

	if len(new_results) == 0:
		print("There were no results for your search. Would you like to try another Category?")
		redo_category_search = input("Yes/No: ")
		if redo_category_search == "Yes" or redo_category_search == "yes" or redo_category_search == "y" or redo_category_search == "Y":
			return search_category(content)
		elif redo_category_search == "No" or redo_category_search == "no" or redo_category_search == "n" or redo_category_search == "N":
			return content
		return content
	else:
		return new_results

####################################################################################
####################################################################################

def zip_in_data(content, entered_zip):
	new_results = []
	for a in content:
		if a[12] == str(entered_zip):
			new_results.append(a)

	if len(new_results) == 0:
		print("There were no results for your search. Would you like to try another zipcode?")
		redo_zip_search = input("Yes/No: ")
		if redo_zip_search == "Yes" or redo_zip_search == "yes" or redo_zip_search == "y" or redo_zip_search == "Y":
			return search_zip(content)
		elif redo_zip_search == "No" or redo_zip_search == "no" or redo_zip_search == "n" or redo_zip_search == "N":
			return content
	else:
		return new_results

####################################################################################
####################################################################################

def search_grade(content):
	new_results = []
	print("(4.) Please enter a restaurant grade to filter by. If you wish to skip filtering by restaurant grade, please leave the following line blank.")
	prompt_text = "Restaurant Grade (A, B, C, or Z): "
	print("-" * (len(prompt_text)-1))
	grade_search = input(prompt_text)
	print("-" * (len(grade_search) + len(prompt_text)))

	for a in content:
		if a[17] == str(grade_search) or a[17] == str(grade_search).lower() or a[17] == str(grade_search).upper() or a[17] == str(grade_search).capitalize() or a[17] == str(grade_search).title():
			new_results.append(a)

	if len(new_results) == 0:
		print("There were no results for your search. Would you like to try another Grade?")
		redo_grade_search = input("Yes/No: ")
		if redo_grade_search == "Yes" or redo_grade_search == "yes" or redo_grade_search == "y" or redo_grade_search == "Y":
			return search_grade(content)
		elif redo_grade_search == "No" or redo_grade_search == "no" or redo_grade_search == "n" or redo_grade_search == "N":
			return content
		return content
	else:
		return new_results


####################################################################################
####################################################################################


if __name__ == '__main__':
	file_path = open("rows.json")
	search_start(get_data(file_path))
