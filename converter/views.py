from django.shortcuts import render
from converter.helper_methods import process_xmls, create_dictionarys, write_csv
import lxml.etree as etree
import csv
import os

def home(request):
	if request.method == 'GET':
		return render(request, 'converter/home.html')
	else:
		try:
			directory = request.POST['directory']
			studio = request.POST['studio']
		except:
			directory = ''
			studio = ''
		
		file_list = []
		studio_error = ''
		studio_name = ''
		
		list_data = process_xmls.process_directory(directory, studio)

		# EXTRACT COLUMN HEADERS TO SEND TO TEMPLATE:
		columns = write_csv.extract_columns(list_data)

		# EXTRACT COLUMN ROWS
		rows = []
		row_data = write_csv.extract_row_data(list_data)

	
		filename = "C:\\Users\\nhunter\\Desktop\\code\\sandbox\\_TEST2.csv"
		# filename = directory + '\\' + "_TEST2.csv"

		# if not request.POST['export']:
		# 	print("EXPORT")
		
		write_csv.write_to_csv(filename, list_data)

		return render(request, 'converter/home.html', {
			'path': directory,
			'file_list': list_data,
			'studio': studio.upper(),
			'columns': columns,
			'rows': row_data,
			'filename': filename
			}
		)


def about(request):
    return render(request, 'converter/about.html')
