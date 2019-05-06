import csv

with open('testing.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file, dialect='excel')
	with open('bad_score.csv', 'w') as bad_score:
		csv_writer = csv.writer(bad_score)
		next(csv_reader)
		csv_writer.writerow(bad_score.row[0])
		for row in csv_reader:
			if not '1' in row[30]:
				csv_writer.writerow(row)
			
f.close()
