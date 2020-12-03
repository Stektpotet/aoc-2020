if __name__ == '__main__':

    # min, max, char, test
    valid = 0
    with open("input") as reader:
        line = reader.readline()
        while line != '':
            min_max, char, test = line.split(' ')
            lower_limit, higher_limit, char = *map(int, min_max.split('-')), char[0]

            if lower_limit <= test.count(char) <= higher_limit:
                valid += 1
            line = reader.readline()

    print(valid)

    valid = 0
    with open("input") as reader:
        line = reader.readline()
        while line != '':
            min_max, char, test = line.split(' ')
            lim1, lim2, char = *map(int, min_max.split('-')), char[0]

            if (test[lim1-1] == char) + (test[lim2-1] == char) == 1:
                valid += 1
            line = reader.readline()
    print(valid)