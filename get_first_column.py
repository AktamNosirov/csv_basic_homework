def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    
    l=data.split("\n")  
    list=[]
    for x in l:
        list.append(x.split(",")[0])
    return list
    

        
    
    # return [x.split(",")[0] for x in l]
    
    
    
  

# Read the csv file
file=open("data.csv", "r")
data=file.read()
print(get_first_column(data))