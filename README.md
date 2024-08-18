# LinkedIn-High-School-Scraper

## **Project Overview**

This project involves a Python script designed to scrape high school names from LinkedIn profile HTML files. The script processes a CSV file containing paths to local HTML files, extracts high school information, and outputs the results to a new CSV file.

## **Files Included**

- **`main.py`**: The main Python script that performs the scraping.
- **`input_linkedin_profiles.csv`**: Example CSV file with paths to local HTML files.
- **`output_high_schools.csv`**: The output CSV file containing extracted high school information (this file will be generated after running the script).

## **How It Works**

1. **Input**: The script reads from `input_linkedin_profiles.csv`, which contains paths to local HTML files representing LinkedIn profiles.
2. **Processing**: It opens each HTML file, parses the content to find the high school name under the "Education" section, and extracts it.
3. **Output**: The script writes the extracted high school names and their corresponding LinkedIn profile paths to `output_high_schools.csv`.

## **Example**
**This is an example of how the simulated LinkedIn HTML file looks like, taken from profile number 5**
<img width="400" alt="LinkedIn HTML ss" src="https://github.com/user-attachments/assets/51266e57-900d-4071-aa71-d73b0554c55d">


## **Usage**

1. **Install Dependencies**:
   Ensure you have the required Python libraries installed. You can install them using pip:
   ```bash
   pip install beautifulsoup4

