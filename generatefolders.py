from os import makedirs

if __name__ == '__main__':
    for i in range(1, 26):
        day = f'day{i:02d}'
        try:
            makedirs(day)
        except FileExistsError:
            pass
        open(f'{day}/{day}.py', 'a').close()