def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    l=data.split("\n")
 
    
    
    
    
    
    return len(l)-1

# Read the csv file
file=open("data.csv", "r")
data=file.read()
print(find_number_of_rows(data))