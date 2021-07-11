def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    list_of_nums = []
    list_of_words = []
    for i in words:
        if i.isdigit() or i[0].isdigit():
            list_of_nums.append(i)
        else:
            list_of_words.append(i)

    sorted_words = sorted(list_of_words, key=str.casefold)
    sorted_nums = sorted(list_of_nums)

    return sorted_words + sorted_nums
