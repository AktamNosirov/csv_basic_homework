def get_first_row(data):   
    """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
    """
   
    l=data.split("\n")
    return list(l[1].split(","))

file=open("data.csv", "r")
data=file.read()
print(get_first_row(data))