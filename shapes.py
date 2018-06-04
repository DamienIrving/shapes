"""Code to work with shapes."""

valid_shapes = [None, None, None, 'triangle', 'square', 'pentagon', 'hexagon']

def shape(sides):
    """Given a number of sides, tell us the shape.
    
    Args:
      sides (int) : Number of sides
      
    Returns:
      str : The name of the shape
    
    """

    return valid_shapes[sides]
    
    
def sides(shape):
    """Given a shape, tell us the number of sides.
    
    Args:
      shape (str) : Name of shape
      
    Returns:
      int : Number of sites
      
    """
    
    assert shape in valid_shapes, "Not a valid shape."
    
    return valid_shapes.index(shape)
    
    
    
if __name__ == '__main__':

    print('I know about the following shapes:')
    
    for valid_shape in valid_shapes:
        if valid_shape is not None:
            num_sides = sides(valid_shape)
            print(' %s (sides=%s)' %(valid_shape, num_sides))
            
            