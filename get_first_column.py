def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    
    l=data.split("\n")
    for i in l:
        return i.split(",")[0]
    
    # return [x.split(",")[0] for x in l]
    
    
    
  

# Read the csv file
file=open("data.csv", "r")
data=file.read()
print(get_first_column(data))