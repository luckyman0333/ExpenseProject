import openpyxl

def read_excel(file_path):
    try:
        # Download the Excel file
        workbook = openpyxl.load_workbook(file_path)
        # Select the active sheet
        sheet = workbook.active

        print(f"Outputting data from a file: {file_path}\n")

        # Row iteration and data output
        for row in sheet.iter_rows(values_only=True):
            print(row)

    except Exception as e:
        print(f"Failed to open file. Error: {str(e)}")


if __name__ == "__main__":
    
    file_path = input("Enter the path to the Excel file: ")
    
    read_excel(file_path)
