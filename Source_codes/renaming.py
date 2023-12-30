import os
import csv
from tkinter import Tk, filedialog

def select_csv_file():
    # Create a Tkinter root window (it will not be shown)
    root = Tk()
    root.withdraw()  # Hide the root window

    # Ask the user to select the CSV file
    csv_file_path = filedialog.askopenfilename(
        title="Select CSV File",
        filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
    )

    return csv_file_path

def rename_files(csv_file_path):
    # Open the CSV file and read its content
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            old_name = row['Name']
            folder_path = row['Folder Path']
            new_name = row['New Name']

            # Construct the full paths for the old and new files
            old_file_path = os.path.join(folder_path, old_name)
            new_file_path = os.path.join(folder_path, new_name)

            try:
                # Rename the file
                os.rename(old_file_path, new_file_path)
                #print(f"File renamed: {old_file_path} -> {new_file_path}")
            except FileNotFoundError:
                #print(f"File not found: {old_file_path}")
                pass

# Example usage
csv_file_path = select_csv_file()

if csv_file_path:
    rename_files(csv_file_path)
    print("Done")
else:
    print("No CSV file selected")
