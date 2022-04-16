def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    l=data.split("\n")
 
    
    
    
    
    
    return len(l)-1

# Read the csv file
file=open("data.csv", "r")
data=file.read()
print(find_number_of_columns(data))


