import pytest
from pytest_bdd import given, when, then


@pytest.mark.input
@given("A user inputs a string from the terminal")
def test_get_input():
    t_input = input("Please enter the string to be reversed: ")
    # t_input = "This is a simple test of reversing a string"
    assert len(t_input) > 0, "get_input function failed"
    return t_input


@pytest.mark.split
@when("an input string is given, split them in to words")
def test_split_word(input_string):
    words = input_string.split(" ")
    assert len(words) > 0, "Split words function failed"
    return words


@pytest.mark.reverse
@when("split words are input, reverse them using list slicing method")
def test_reverse_word(input_split_word):
    reversed_words = input_split_word[::-1]
    assert len(reversed_words) > 0, "reversed words function failed"
    return reversed_words


@pytest.mark.join
@when("the reversed words are input, join them up as one single word using join method")
def test_do_join(input_join_word):
    joined_words = ''.join(input_join_word)
    assert len(joined_words) > 0, "joined words function failed"
    return joined_words


@pytest.mark.traverse
@then("finally traverse the reversed word and list the reversed words in order")
def test_traverse_list(input_traverse_list):

    print("the contents of traverse list are:  ")
    for i in input_traverse_list:
        print(i)


terminal_input = test_get_input()

split_words = test_split_word(terminal_input)
print("The split words are  "+str(split_words))


reverse_words = test_reverse_word(split_words)
print("The reversed words are  "+str(reverse_words))


joined_up_words = test_do_join(reverse_words)
print("The joined up words are  "+str(joined_up_words))

test_traverse_list(reverse_words)

get_count_of_words = len(reverse_words)
print("The total length of the list is: ", get_count_of_words)
