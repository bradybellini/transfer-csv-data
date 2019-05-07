import csv

def open_files():
	with open('testing.csv', 'r') as csv_file, open('bad_score.csv', 'w', newline='') as bad_score:
		csv_reader = csv.reader(csv_file, dialect='excel')
		csv_writer = csv.writer(bad_score, dialect='excel')
		next(csv_reader)
		find_1(csv_reader, csv_writer)
			
def find_1(reader, writer):			
	for row in reader:
		if any(field.strip() for field in row):
			if '1' in row[30]:
				writer.writerow(row)

if __name__ == '__main__':
	open_files()
