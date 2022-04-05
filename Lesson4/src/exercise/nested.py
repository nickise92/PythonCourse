def nested_sum(l):
    integer_sum = 0
    for i in l:
        for j in i:
            integer_sum += j

    print(integer_sum)
    return integer_sum

def nested_compact(l):
    set = []
    for i in l:
        for k in i:
            if k not in set:
                set.append(k)

    print(set)
    return set




nested_sum(([[1,2,3], [5], [-1 , -1, -1]]))
nested_compact([[1, 2, 3], [-1, 3], [-2, -2]])