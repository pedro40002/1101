

def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        numbers = [int(num) for line in lines for num in line.split()]
    return numbers

def find_missing_numbers(numbers):
    all_numbers = set(range(1, 101))
    present_numbers = set(numbers)
    missing_numbers = sorted(list(all_numbers - present_numbers))
    return missing_numbers

def write_sorted_numbers_to_file(sorted_numbers, output_filename):
    with open(output_filename, 'w') as file:
        file.write('\n'.join(map(str, sorted_numbers)))

if __name__ == "__main__":
    
    filename = "one_hundred.txt"
    numbers = read_numbers_from_file(filename)

    # Step 2: Determine missing numbers and write sorted numbers to a new file
    missing_numbers = find_missing_numbers(numbers)
    sorted_filename = "one_hundred_sorted.txt"
    write_sorted_numbers_to_file(missing_numbers, sorted_filename)
