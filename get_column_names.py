#Define function,Get coloumn names from a csv file
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    l=data.split("\n")
 
    
    
    
    
    
    return list(l[0].split(","))

# Read the csv file
file=open("data.csv", "r")
data=file.read()
print(get_column_names(data))