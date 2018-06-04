from shapes import shapes as s

def test_heptagon():
    """Test heptagon"""
    
    expected = 'heptagon'
    result = s.shape(7)
    
    assert expected == result