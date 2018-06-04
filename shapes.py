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