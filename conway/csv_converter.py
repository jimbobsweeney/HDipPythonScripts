import csv

def main():
	toad = [(1,1),(2,1),(3,1),(0,2),(1,2),(2,2)]
	convert(toad)

def convert(coming_in):
	csvfile = open("output.csv", "wb")

	csv_writer = csv.writer(csvfile)
	
	for line in coming_in:
		writing = csv_writer.writerow(line)

	csvfile.close()

if __name__ == '__main__':
	main()