# madeleine varner
# january 29 2015

import os, sys, string

def parse_line(line):
	categ_index = 9
	exemp_index = 8
	response_index = 4
	sf_index = 2
	line_info = line.split()

	if len(line_info) != 8: 
		if (line_info[3] == 'stream'):
			categ_index = 9
			exemp_index = 8
			response_index = 4
			sf_index = 2
		elif (line_info[3] == 'PHOTO'):
			categ_index = 9
			exemp_index = 8
			response_index = 4
			sf_index = 2
	filename_info = string.split(line_info[2], "_")

	#print line_info
	if not "gray_500x_CHURCHES_Google_Images_Inside-Our-Lady-of-Light-Church.jpg" in line_info[2]:
		# category shit
		category = filename_info[9]
		categ_num = ''
		if (category == 'BEDROOMS'):    categ_num = '1'
		elif (category == 'CHURCHES'):  categ_num = '2'
		elif (category == 'MOUNTAINS'): categ_num = '3'
		elif (category == 'SKYLINE'):   categ_num = '4'
		elif (category == 'STREAM'):    categ_num = '5'
		elif (category == 'WOODS'):     categ_num = '6'
		# correctness
		correctness = '\t0'
		#print categ_num, line_info[4]
		if (categ_num == line_info[4]): 
			correctness = '\t1'
		categ = '\t' + categ_num
		exemp = '\t' + filename_info[8]
		sf = '\t' + filename_info[2]
		fixed_line = ''
		fixed_line = line.rstrip()
		fixed_line += categ + exemp + sf + correctness + '\n'
		return fixed_line
	else:
		return line

def parse_document(document):
	count = 0
	with open(document, 'r') as f:
		lines = f.readlines()

		# dumb and for testing
		# print lines[5]
		# print lines[7]
		# print parse_line(lines[7])


	with open(document + "_new", 'w') as f:
		print lines[5]
		for i in xrange(6, len(lines)):
			lines[i] = parse_line(lines[i])
			print lines[i]
		f.writelines(lines)

def list_documents(directory):
	folder = os.listdir(directory)
	documents = []
	for item in folder:
		if not "." in item:
			documents.append(item)
	return documents

def clean_data():
	directory = os.getcwd()
	documents = list_documents(directory)
	for document in documents:
		parse_document(document)
	return

def test():
	parse_line()

if __name__ == '__main__':
	clean_data()
	