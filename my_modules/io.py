def read_raster_data(file_path):
   
    """
    Reads the raster data from the file and stores it in a 2D list.
    ----------
    file_path : str
        The path to the file containing the raster data.
    -------
    list of lists
        A two-dimensional list of lists representing the raster data.

    """
    with open(file_path, "r") as f:
        lines = f.readlines()  # Read all rows of data from a file
    raster_data = []
    for line in lines:
        row_data = line.strip().split(',')  # split into a set of numbers using the split(',') method
        row_data = [int(x) for x in row_data]  # Convert each numeric string to an integer
        raster_data.append(row_data) # Add each row of data as a one-dimensional list to the raster data list
    return raster_data

def write_raster(file,rescaled_raster):
       # Write raster data to file
    with open(file, 'w') as f:
        for i in rescaled_raster:
            line=','.join([str(int(value)) for value in i])
            f.write(line+'\n')