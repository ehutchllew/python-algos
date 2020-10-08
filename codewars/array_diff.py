# def array_diff(a, b):
#     diff_list = []
#     for i in a:
#         try:
#             if b.index(i):
#                 pass
#         except ValueError:
#             diff_list.append(i)
#     print(diff_list)


def array_diff(a, b):
    diff_list = [i for i in a if i not in b]
    return diff_list


# test

