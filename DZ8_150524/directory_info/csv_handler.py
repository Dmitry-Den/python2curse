import csv

def save_as_csv(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for key, value in data.items():
            writer.writerow([key, value['type'], value['size']])
