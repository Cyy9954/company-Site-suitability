
def multiply_raster(raster, weight):
    """
    Multiplies each element of the raster data by the given factor and stores the result in a two-dimensional list.
    ----------
    raster : list
        A 2D grid representing the raster data.
    weight : int or float
        A factor to multiply each element of the raster.
    -------
    weighted_raster : list
        A 2D grid representing the raster data after multiplication by the given factor.

    """
    weighted_raster = [[weight * value for value in row] for row in raster]
    return weighted_raster


def add_rasters(raster1, raster2, raster3):
    """
    Add the three raster data element by element and store the result in a two-dimensional list.
    ----------
    raster1, raster2, raster3 : list
        Three 2D grids representing the raster data.
    -------
    added_raster : list
        A 2D grid representing the sum of the three rasters.

    """
    n_row=len(raster1)
    n_cols=len(raster1[0])
    added_raster=[]
    for i in range(n_row):
        added_row=[]
        for j in range(n_cols):
            addraster = raster1[i][j] + raster2[i][j] + raster3[i][j]
            added_row.append(addraster)
        added_raster.append(added_row)
    return added_raster


def rescale_raster(raster, new_min, new_max):
    """
    Rescales the raster data to the specified range and stores the result in a two-dimensional list.
    ----------
    raster: list
        A two-dimensional list of the raster data to be rescaled.
    new_min: int
        The minimum value of the rescaled raster data.
    new_max: int
        The maximum value of the rescaled raster data.
    rescaled_raster: list
        A two-dimensional list of the rescaled raster data.
    ------
    Rescales the raster data according to the minimum and maximum values of the raster data, as well as the new minimum and maximum values specified.
    """
     # Find the minimum and maximum values of the raster data
    min_value = min([min(row) for row in raster])
    max_value = max([max(row) for row in raster])
    # If the maximum and minimum values are equal, the original data is returned directly without scaling
    if max_value - min_value == 0:
        rescaled_raster =raster
    # Otherwise, scaling of raster data
    else:
        rescaled_raster = [[int((value - min_value) / (max_value - min_value) * (new_max - new_min) + new_min) for value in row] for row in raster]
    return rescaled_raster