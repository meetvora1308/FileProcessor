import os
import csv 
import pandas as pd

previous_data = []
unique_ids = []

all_uniques_data = []
names = {}

def process_file_data(file_path):
    # reading records as frame
    read_csv = pd.read_csv(file_path,"\t")
    
    # convert it into dict
    converted_dict = read_csv.to_dict("records")
    for data in converted_dict:
        
        # check whether that id is already present in list
        if data["id"] in unique_ids:
            continue
        
        elif data["email"] in names.keys():
            if data["firstname"] == names[data["email"]["firstname"]] and data["last_name"] == names[data["email"]["last_name"]]:
                # First name already exists, remove this data from all_unique_data
                continue
        
        else:
            unique_ids.append(data["id"])
            names[data["email"]] = data
            data["Gross Salary"] = data["basic_salary"] + data["allowances"]
            all_uniques_data.append(data)

                        

if __name__ == "__main__":
    
    file_list = os.listdir("inputfiles")
    output_file_path = "outputfiles/output.csv"
    output_dict = []
    for file_name in file_list:
        file_path = os.path.join("inputfiles", file_name)
        
        # convert the file into dict format 
        process_file_data(file_path)
    print("file execution done")
        
    fieldnames = list(all_uniques_data[0].keys())
    
    # sorting data based on ids 
    sorted_data = sorted(all_uniques_data, key=lambda x: int(x['id']))

    # sorting all gross salary 
    all_gross_salary = list(set([x["Gross Salary"] for x in all_uniques_data]))
    all_gross_salary.sort()
    second_highest_salary = "Second Highest Salary = {0}".format(all_gross_salary[-2])
    
    # Calculate the average salary
    total_salary = sum([d["Gross Salary"] for d in all_uniques_data])
    average_salary = total_salary / len(all_uniques_data)
    average_salary ="average salary = {}".format(round(average_salary,2))
    
    # Write the list of dictionaries to the CSV file
    with open(output_file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        # Write the header row
        writer.writeheader()
        
        # Write the data rows
        writer.writerows(sorted_data)
        
        writer.writerow({"id":second_highest_salary, "first_name":average_salary})
