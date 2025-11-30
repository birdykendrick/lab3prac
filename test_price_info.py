import price_info

def test_total_cost_shipping():
    #arrange
    expected_result = 46.75
    #act
    result = price_info.total_cost_shopping()

    #assert
    assert result == expected_result

def test_cost_of_fruits():
    #arrange
    fruit_name = "apple"
    quantity = 10
    expected_result = 12.0

    #act
    result = price_info.cost_of_fruits(fruit_name, quantity)

    #assert
    assert result == expected_result