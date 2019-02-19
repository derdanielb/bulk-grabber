# coding=utf-8
import os
import urllib.request
import urllib.error
import sys

if len(sys.argv) == 3:
	filename = sys.argv[1]
	directory = sys.argv[2]
	skippedfiles = []

	print("Start downloading files from list: " + filename)
	print("Target directory: " + directory)
	print("___________________________________")
	if not os.path.exists(directory):
		os.makedirs(directory)

	f = open(filename, "r", encoding="utf-8")
	linecount = 0
	for line2 in f:
		if not (line2 == "" or line2 == "\n"):
			linecount += 1
	f.close()
	# f.seek(0)
	f = open(filename, "r", encoding="utf-8")
	currentline = 0
	for line in f:
		if not (line == "" or line == "\n"):
			currentline += 1
			print("\n")
			print("file " + str(currentline) + "/" + str(linecount))
			url = line.split("\n")[0]
			file = line.split("/")
			file = (file[len(file)-1].split("\n"))[0].split("?")[0]

			print("Downloading... '" + file + "' from '" + url + "'")
			try:
				response = urllib.request.urlopen(url)
				if not (os.path.isfile(directory + "/" + file)):
					f = open(directory+"/"+file, 'wb')

					f.write(response.read())
					f.close()
					print("Completed: " + file)
				else:
					print("Skipping: " + file)
					skippedfiles.append(file)
			except:
				print("Skipping: " + file)
				skippedfiles.append(file)
	print("\n\n**********************************\n")
	print(str(len(skippedfiles)) + " SKIPPED FILES:")
	if len(skippedfiles) > 0:
		for ele in skippedfiles:
			print(ele)
else:
	print("Invalid arguments")
