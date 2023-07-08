# File Processor

The File Processor is a Python script designed to read data from multiple files located in a specific folder, process the data, and convert it into a CSV file with the desired output. The script fulfills the requirements specified below:

## Requirements

1. Read data from multiple files located in a folder.
2. Convert the data into a CSV file with the following specifications:
   - No duplicate data should be present in the output file.
   - The output file should include a footer row with the following details:
     - Second highest salary.
     - Average salary.

## How to Use

1. Clone the repository or download the script.
2. Place the input files to be processed in the `inputfiles` folder.
3. Run the `main.py` or `main1.py` script based on below mentioned Assumptions.
4. The processed output will be saved as `output.csv` in the `outputfiles` folder.

## Dependencies

The script requires the following dependencies:

- Python 3.x
- pandas library


## Implementation Details

The code is implemented in Python and uses the pandas library for data processing. Here's an overview of the key components and their functionality:

- `process_file_data(file_path)`: This function reads an individual file using pandas' `read_csv` function. It converts the data into a dictionary using the `to_dict` method. Each record is checked for duplicate IDs and duplicate combinations of `first_name` and `last_name`. If the record is unique, it calculates the gross salary by summing the `basic_salary` and `allowances`. The unique records are stored in the `all_uniques_data` list.

- Execution Logic: The main execution logic is placed under the `if __name__ == "__main__":` block. It iterates over each file in the `inputfiles` folder and calls the `process_file_data` function to process the data. After processing all files, it sorts the unique records based on IDs, calculates the second highest salary and average salary, and writes the processed data to the output CSV file.

## Assumptions

The File Processor script makes the following assumptions:

1. Input Files
   - The input files to be processed should be located in the `inputfiles` folder.
   - Before running the script, ensure that the desired input files are placed in the `inputfiles` folder.

2. main.py Assumptions
   - If the same `ID` occurs more than once, only the first occurrence will be considered, and any subsequent occurrences will be ignored.
   - In addition to the above assumption, if a combination of `firstname` `+` `lastname` and `email` occurs more than once, only the first occurrence will be considered, and subsequent occurrences will be ignored.

3. main1.py Assumptions
   - If the same `ID` occurs more than once, all records with that `ID` will be `removed and ignored`.
   - In addition to the above assumption, if a combination of `firstname` `+` `lastname` and `email` occurs more than once, the entire record `removed and ignored`, and none of the occurrences will be considered.


## Limitations and Future Improvements

- The code assumes that the input files are tab-separated. If the file format varies, the code needs to be modified accordingly.
- The script replaces the existing output file on each run. To preserve previous outputs, consider modifying the code to generate a unique filename for each run or include a timestamp in the output file name.