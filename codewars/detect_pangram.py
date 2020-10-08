def is_pangram(s):
    low_string = s.lower()
    s_set = set(c for c in low_string if c.isalpha())
    print(s_set, len(s_set))
    if len(s_set) == 26:
        return True
    else:
        return False


# Top solution:
# def is_pangram(s):
#     return set(string.lowercase) <= set(s.lower())
