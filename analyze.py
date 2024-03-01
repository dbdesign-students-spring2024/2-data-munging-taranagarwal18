# Place code below to do the analysis part of the assignment.
import csv
from collections import defaultdict

csv_file_path = '/Users/taranagarwal/Desktop/database & design/2-data-munging-taranagarwal18/data/clean_data.csv'

# We reate a dictionary to store sum of anomalies and count of entries for each decade
decade_data = defaultdict(lambda: {'sum': 0, 'count': 0})

# Now we open and read the CSV file
with open(csv_file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # We are skipping the header row

    for row in csvreader:
        year = int(row[0])
        anomalies = [float(val) for val in row[1:] if val != 'NaN']  # Excluding 'NaN' values

        # Determining the decade for the current row
        decade = (year // 10) * 10

        # Adding the sum of anomalies and counting them
        decade_data[decade]['sum'] += sum(anomalies)
        decade_data[decade]['count'] += len(anomalies)

# Finally we calculate the average anomaly for each decade and output the results
for decade in sorted(decade_data.keys()):
    total_anomaly = decade_data[decade]['sum']
    count = decade_data[decade]['count']
    average_anomaly = total_anomaly / count if count else 0
    print(f"Decade {decade}-{decade+9}: Average Temperature Anomaly: {average_anomaly:.2f}°F")