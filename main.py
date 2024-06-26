def main():
    numbers = []
    """
    ########################################
    Code Your Program here
    ########################################
    """
    prevnum = None
    while True:
        currentnum = int(input("enter an integer: "))
        if prevnum is None or prevnum <= currentnum:
            numbers.append(currentnum)
            prevnum = currentnum
        else:
            break

    ########################################
    # Do not delete the return statement
    ########################################
    print(*numbers)
    return numbers


if __name__ == '__main__':
    main()
