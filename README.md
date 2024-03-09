# week2_notebook2script

Data Summarization and Visualization Script

This Python script provides a utility for summarizing CSV data by group and visualizing the total word counts associated with each group. It is designed to process a CSV file containing at least 'GroupName' and 'Text' columns, performing aggregations to count paragraphs and total word counts, then generating a horizontal bar chart to visually represent this data.

Features
•	Summarizes CSV data by 'GroupName', counting paragraphs and total words.
•	Visualizes the word counts in a horizontal bar chart, saving the plot as a PNG file.
•	Allows customization of the plot through command-line arguments.

Prerequisites
Before you begin, ensure you have met the following requirements:
•	Python 3.x installed on your machine.
•	Pandas and Matplotlib libraries installed. You can install these with pip install pandas matplotlib.

Installation
To use this script, follow these steps:
1.	Clone the repository or download the script to your local machine.
2.	Ensure that the required Python libraries are installed by running pip install -r requirements.txt (assuming a requirements.txt file exists with the entries pandas and matplotlib; if not, install these packages manually as mentioned above).

Usage
To run this script from the command line, navigate to the directory containing the script and execute the following command:
python nb_to_script.py <input_csv_file_path> <output_png_file_path> [--max_words MAX_WORDS] 
•	<input_csv_file_path> is the path to the CSV file you wish to process. Necessary columns are 'GroupName' and 'Text'.
•	<output_png_file_path> is the path where the generated plot image will be saved.
•	--max_words is an optional argument that specifies the maximum number of words to display from each group name in the plot. The default value is 8.

Contributing
For those who would like to contribute to the script, please follow the standard process of forking the repository, making your changes, and submitting a pull request for review. Your contributions are greatly appreciated!

Authors
•	gschaumb

License
This project is licensed under the [License Name]. See the LICENSE file for more details.

Acknowledgments
Acknowledgments, if applicable, such as references to external resources, data sources, or inspiration for the project.
