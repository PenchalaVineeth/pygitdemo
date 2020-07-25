def sort(list):

    for i in range(len(list)-1):
        minpos = i
        for j in range(i, len(list)):
            if list[j] < list[minpos]:
                minpos = j
            # else:
            #     print("Nothing")

        temp = list[i]
        list[i] = list[minpos]
        list[minpos] = temp

##################### OR #########################

        # list[i], list[minpos] = list[minpos], list[i]
        # print(list)

nums = [9, 5, 6, 12, 14, 1, 2]

# Ascending order
sort(nums)


print(nums)
