import lab2practice.bmi as bmi

# The AAA pattern in testing

#arrange
#set up test conditions
# prepare the input data
def test_calculate_bmi():
    #Arrange
    weight = 60
    height = 1.57

    #Act
    result = bmi.calculate_bmi(weight, height)

    #Assert
    assert result == -1

def test_bmi_underweight():
    #arrange
    weight = 50
    height = 1.8

    #Act
    result = bmi.calculate_bmi(weight, height)

    #assert
    assert result == -1

def test_calculate_min_max():
    #arrange
    minmax = [60, 90, 61, 99]

    #Act
    result = bmi.find_min_max(minmax)
    #assert
    assert result == [60, 99]

def test_calc_median_temperature():
    #arrange
    vallist = [10,20,30,40,50]

    #act
    result = bmi.calc_median_temperature(vallist)

    #assert
    assert result == 30