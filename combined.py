#this is a python program
#program reads numbers from 'numbers1.txt' and 'numbers2.txt'
#numbers are then sorted and printed into 'all_numbers.txt'

def load_numbers(filepath):
    with open(filepath,'r') as file:
        return[(n) for n in file.readlines()]

if __name__ == '__main__':
    first_numbers = load_numbers('numbers1.txt')
    second_numbers = load_numbers('numbers2.txt')
    sort = first_numbers + second_numbers

    print(sort)

    sorted_numbers = sorted(sort)

    print(sorted_numbers)

    with open('all_numbers.txt','w') as file:
        file.writelines(sorted_numbers)

print("Check out the results on ""all_numbers.txt"" ")
