import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])

def test_bubble_sort_10ormore():
    #Act
    input_arr = [10,10,10,1,1,1,2,3,4,5,6,7]

    #arrange
    result = Lab3.bubble_sort(input_arr, test_bubble_sort_descending)

    #assert
    assert result == 1

def test_non_integervalues():
    #act
    input_array = [1,2,3,4,5,6,8,"hello",5]

    #arrange
    result = Lab3.bubble_sort(input_array, test_bubble_sort_descending)

    #assert
    assert result == 2