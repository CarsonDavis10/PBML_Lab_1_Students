from START_Lab_1 import lab1Question1, lab1Question2, lab1Question3, lab1Question4, lab1Question5, lab1Question6
import pytest

def test_lab1Question1():
    # Test case 1
    input_gb = 10
    expected_bytes = 10 * 1024 * 1024 * 1024
    assert lab1Question1(input_gb) == expected_bytes

    # Test case 2
    input_gb = 0
    expected_bytes = 0
    assert lab1Question1(input_gb) == expected_bytes

    # Test case 3
    input_gb = 1
    expected_bytes = 1 * 1024 * 1024 * 1024
    assert lab1Question1(input_gb) == expected_bytes

    # Test case 4
    input_gb = 100
    expected_bytes = 100 * 1024 * 1024 * 1024
    assert lab1Question1(input_gb) == expected_bytes

    # Test case 5
    input_gb = -5
    expected_bytes = -5 * 1024 * 1024 * 1024
    assert lab1Question1(input_gb) == expected_bytes

def test_lab1Question2():
    # Test case 1
    name = "John"
    assert lab1Question2(name) == False

    # Test case 2
    name = "Jane"
    assert lab1Question2(name) == False

    # Test case 3
    name = "Alice"
    assert lab1Question2(name) == True

    # Test case 4
    name = "Bob"
    assert lab1Question2(name) == True

    # Test case 5
    name = ""
    assert lab1Question2(name) == False

def test_lab1Question3():
    # Test case 1
    input_string = "Hello"
    input_number = 0
    assert lab1Question3(input_string, input_number) == "H"

    # Test case 2
    input_string = "World"
    input_number = 2
    assert lab1Question3(input_string, input_number) == "r"

    # Test case 3
    input_string = "Python"
    input_number = 10
    assert lab1Question3(input_string, input_number) == -1

    # Test case 4
    input_string = "AI"
    input_number = 1
    assert lab1Question3(input_string, input_number) == "I"

    # Test case 5
    input_string = "Programming"
    input_number = 5
    assert lab1Question3(input_string, input_number) == "a"

def test_lab1Question4():
    # Test case 1
    file_name = "test_file1.txt"
    expected_list = [1, 2, 3, 4, 5]
    assert lab1Question4(file_name) == expected_list

    # Test case 2
    file_name = "test_file2.txt"
    expected_list = [10, 20, 30, 40, 50]
    assert lab1Question4(file_name) == expected_list

def test_lab1Question5():
    # Test case 1
    list_numbers = [1, 2, 3, 4, 5, 1]
    assert lab1Question5(list_numbers) == 1

    # Test case 2
    list_numbers = [10, 20, 30, 40, 50, 10, 20, 20]
    assert lab1Question5(list_numbers) == 20

    # Test case 3
    list_numbers = [1, 1, 2, 2, 3, 3, 3]
    assert lab1Question5(list_numbers) == 3

    # Test case 4
    list_numbers = [100, 200, 300, 400, 500, 400]
    assert lab1Question5(list_numbers) == 400

    # Test case 5
    list_numbers = [1, 1, 1, 1, 1]
    assert lab1Question5(list_numbers) == 1

def test_lab1Question6():
    # Test case 1
    quarters = 4
    dimes = 3
    nickels = 2
    pennies = 1
    assert lab1Question6(quarters, dimes, nickels, pennies) == 1.41

    # Test case 2
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    assert lab1Question6(quarters, dimes, nickels, pennies) == 0

    # Test case 3
    quarters = 10
    dimes = 5
    nickels = 2
    pennies = 1
    assert lab1Question6(quarters, dimes, nickels, pennies) == 3.15

    # Test case 4
    quarters = 1
    dimes = 1
    nickels = 1
    pennies = 1
    assert lab1Question6(quarters, dimes, nickels, pennies) == 0.41

    # Test case 5
    quarters = 2
    dimes = 0
    nickels = 0
    pennies = 5
    assert lab1Question6(quarters, dimes, nickels, pennies) == 0.55