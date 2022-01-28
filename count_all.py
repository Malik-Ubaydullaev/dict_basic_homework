def count_all(txt):
    """
    Given a function that takes a string and calculates the number of letters and digits within it.
    Return the result in a dictionary.
    Args:
        txt(str): count letters and digits
    Returns:
        dict: dictionary with letters and digits
    """
    count_letters = 0
    count_digits = 0
    idx = 0
    while idx < len(txt):
        if txt[idx].isdigit():
            count_digits += 1
        if txt[idx].isalpha():
            count_letters += 1
        idx += 1
    answer = {'LETTERS': count_letters, 'DIGITS': count_digits}
    return answer

txt = "python foundations 2022"
print(count_all(txt))