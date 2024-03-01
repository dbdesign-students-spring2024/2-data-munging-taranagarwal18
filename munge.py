# Place code below to do the munging part of this assignment.
def clean_and_convert_data(input_file_path, output_file_path):
    # We first read the file
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    # Now we identify the starting and ending index of the data
    start_index = None
    end_index = None

    for i, line in enumerate(lines):
        if line.strip().startswith('Year'):
            if start_index is None:
                start_index = i
            else:
                end_index = i
                break

    # Next we extract the relevant data
    data_lines = lines[start_index:end_index]

    # We go ahead and remove blank lines and lines with repeated headers
    data_lines = [line for line in data_lines if line.strip() and not line.strip().startswith('Year')]

    # We prepare it for CSV conversion
    csv_lines = []
    for line in data_lines:
        line_data = line.split()
        year = line_data[0]
        monthly_data = line_data[1:13]  # Excluding yearly and seasonal summaries for simplicity

        # Converting temperature anomalies from Celsius to Fahrenheit and handling missing data
        for i, value in enumerate(monthly_data):
            if value == '****':  # Handling missing data
                fahrenheit_value = 'NaN'
            else:
                celsius = int(value) / 100.0
                fahrenheit = celsius * 1.8
                fahrenheit_value = f"{fahrenheit:.1f}"
            monthly_data[i] = fahrenheit_value

        csv_line = f"{year}," + ",".join(monthly_data)
        csv_lines.append(csv_line)

    # Write the cleaned and converted data to a new CSV file
    with open(output_file_path, 'w') as file:
        # Headers
        headers = 'Year,Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec\n'
        file.write(headers)

        # Writing the data
        for line in csv_lines:
            file.write(line + '\n')

# We now define input and output file paths
input_file_path = '/Users/taranagarwal/Desktop/database & design/2-data-munging-taranagarwal18/data/GLB.Ts+dSST.txt'
output_file_path = '/Users/taranagarwal/Desktop/database & design/2-data-munging-taranagarwal18/data/clean_data.csv'

# Finally we call the function to clean and convert the data
clean_and_convert_data(input_file_path, output_file_path)