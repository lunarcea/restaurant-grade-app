from ratings_app import *

####################################################################################
####################################################################################

def test_get_data():
	file_path = open("mock/test_orig.json")
	data_file = get_data(file_path) 
	
	# PASS TEST
	# LENGTH OF FIRST LEVEL OF JSON FILE 
	assert len(data_file) == 2
	
	# FAIL TEST
	# assert len(data_file) == 3

####################################################################################
####################################################################################

def test_get_critical():
	file_path = open("mock/test_orig.json")
	data_file = get_data(file_path) 
	content = get_critical(data_file)

	# PASS TEST
	# LENGTH OF CRITICAL RESULTS
	assert len(content) == 93315
	
	# FAIL TEST
	# assert len(content) == 2

####################################################################################
####################################################################################

def test_final_results():
	processed_data = [[330708812, 'E44CFF15-C846-4B35-9615-B4DD0878210F', 330708812, 1529260870, '399231', 1529260870, '399231', None, 'CASA MEZCAL', 'MANHATTAN', '86', 'ORCHARD STREET', '10002', 'Mexican', 'Filth flies or food/refuse/sewage-associated (FRSA) flies present in facility\x1as food and/or non-food areas. Filth flies include house flies, little house flies, blow flies, bottle flies and flesh flies. Food/refuse/sewage-associated flies include fruit flies, drain flies and Phorid flies.', 'Critical', '17', 'B', '2017-09-18T00:00:00', '2018-06-17T06:01:06'], [330729186, '655A4822-7867-4957-9EA5-CF4DDC63AF4B', 330729186, 1529260880, '399231', 1529260880, '399231', None, 'CASA MEZCAL', 'MANHATTAN', '86', 'ORCHARD STREET', '10002', 'Mexican', 'Raw, cooked or prepared food is adulterated, contaminated, cross-contaminated, or not discarded in accordance with HACCP plan.', 'Critical', '17', 'B', '2017-09-18T00:00:00', '2018-06-17T06:01:06']]
	new_results = []
	for b in processed_data:
		restaurant_address = str(b[10]) + " " + str(b[11]) + ", " + str(b[9]) + ", New York, " + str(b[12])
		new_results.append([b[8], restaurant_address, b[13], b[15], b[14], b[17], b[18], b[19]])
	
	# PASS TEST
	# LENGTH OF FINAL RESULTS
	assert len(new_results) == 2

	# PASS TEST
	for b in new_results:
		assert b[1] == "86 ORCHARD STREET, MANHATTAN, New York, 10002"
