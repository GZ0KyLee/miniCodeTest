import itertools


def convert_digits_into_letters(int_list):
    res_letters = []
    # "null" for no matching letters
    phone_number = {1: "null", 2: ("a", "b", "c"), 3: ("d", "e", "f"),
                    4: ("g", "h", 'i'), 5: ("j", "k", "l"), 6: ("m", "n", "o"),
                    7: ("p", "q", "r", "s"), 8: ("t", "u", "v"), 9: ("w", "x", "y", "z"),
                    0: "null"}

    # Situation: input 1 number
    if len(int_list) == 1:
        print('The result of {numberA} is'.format(numberA=int_list[0]))
        print(phone_number[int_list[0]])
        return
    #
    # if phone_number[int_list[0]] == "null" and phone_number[int_list[1]] == "null":
    #     print('No combination of these two numbers')
    #     return

    # Situation: the first number is not matching letters
    if phone_number[int_list[0]] == "null":
        print('The result of {numberA} and {numberB} is'.format(numberA=int_list[0], numberB=int_list[1]))
        print(phone_number[int_list[1]])
        return

    # Situation: the second number is not matching letters
    if phone_number[int_list[1]] == "null":
        print('The result of {numberA} and {numberB} is'.format(numberA=int_list[0], numberB=int_list[1]))
        print(phone_number[int_list[0]])
        return

    # Put all possible letter combinations that the numbers could represent
    for i in itertools.product(phone_number[int_list[0]], phone_number[int_list[1]]):
        res_letters.append(i)

    print('The result of {numberA} and {numberB} is'.format(numberA=int_list[0], numberB=int_list[1]))
    print(res_letters)


if __name__ == '__main__':

    # Stage 1
    # input_int_list = [0, 5]
    # convert_digits_into_letters(int_list=input_int_list)

    # Stage 2
    for i in range(100):  # convert the digits from 0 to 99 into letters
        input_int_list = list(str(i))  # convert int to list, for example: 99 convert to [9, 9]
        for j in range(len(input_int_list)):
            input_int_list[j] = int(input_int_list[j])

        convert_digits_into_letters(int_list=input_int_list)
