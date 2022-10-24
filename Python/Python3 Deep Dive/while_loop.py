def while_else():
    l = [1, 2, 3]
    val = 10
    idx = 0

    while idx < len(l):
        if l[idx] == val:
            break
        idx += 1
    else:
        # This code gets executed if the loop does not break
        l.append(val)

    print(l)


def while_finally():
    a = 0
    b = 2

    while a < 4:
        print('-------------------')
        a += 1
        b -= 1

        try:
            a / b
        except ZeroDivisionError:
            print("{0}, {1} - division by 0".format(a, b))
            continue  # "continue" statement - ensures that the loop will go on
            #  Break would terminate the execution, and the "finally" block
            # will not be executed
            # break
        finally:
            # Gets executed even though there is a "continue" statement
            print("{0}, {1} - always executes". format(a, b))

        print ("{0}, {1} - main loop". format(a, b))


while_finally()
