def get_integer(phrase):
    inp = input(phrase)
    while not inp.isnumeric():
        inp = input(f'(Apenas números) {phrase}')
    inp = int(inp)
    return inp
