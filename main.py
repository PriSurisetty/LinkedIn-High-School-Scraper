from bs4 import BeautifulSoup
import csv

# ------------------------------Opening and extracting High Schools with BeautifulSoup-------------------------------- #

with open('/Users/priyankaasurisetty/WebDevProjects/input_linkedin_profiles.csv', mode='r') as file:
    reader = csv.reader(file)
    urls = list(reader)

# Create an output list to store results
output_data = []

# Processing each URL
for url in urls:
    file_path = url[0].replace("file://", "")

    try:
        # Open and parsing the HTML files
        with open(file_path, 'r', encoding='utf-8') as html_file:
            soup = BeautifulSoup(html_file, 'html.parser')

            # Find the Education section
            education_section = soup.find('h2', string='Education')
            if education_section:
                high_school = None

                # Search for the High School entry under <strong> tag within <li> element
                for li in soup.find_all('li'):
                    strong_tag = li.find('strong')
                    if strong_tag and 'High School' in strong_tag.text:
                        # Extracting just the school name, correcting the outputting format
                        high_school_name = li.text.split(',')[0].replace('High School', '').strip()
                        # Storing each High School in the output list
                        output_data.append([url[0], f'{high_school_name} High School'])
                        break
                else:
                    output_data.append([url[0], "High School not found"])
            else:
                output_data.append([url[0], "Education section not found"])

# ------------------------------Exception Handling & writing to the output file-------------------------------- #

    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        output_data.append([url[0], "Error processing file"])

# Write the results to an output CSV file
with open('/Users/priyankaasurisetty/WebDevProjects/output_high_schools.csv', mode='w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(["LinkedIn URL", "High School"])
    writer.writerows(output_data)

print("Output saved to output_high_schools.csv")
