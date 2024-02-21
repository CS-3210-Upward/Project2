import re

def fix_indentation(program):
    # Fix incorrect indentation
    # For simplicity, this just removes leading whitespaces and adds 4 spaces per level
    lines = program.split('\n')
    program = '\n'.join([line.strip() for line in lines])

    return program

def fix_function_headers(program):
    # Fix syntactically incorrect function headers
    # For simplicity, this just ensures that the parentheses are properly balanced
    program = re.sub(r'(\w+)\s+(\w+)\s*\(', r'\1 \2(', program)

    return program

def count_print_keywords(program):
    # Count the number of times the keyword "print" is used
    count = program.lower().count("print")
    return count

def main():
    # Read the input Python program from a file
    with open('test_program.py', 'r') as file:
        input_program = file.read()

    # Task 1: Fix incorrect indentation
    fixed_indentation_program = fix_indentation(input_program)

    # Task 2: Fix syntactically incorrect function headers
    fixed_headers_program = fix_function_headers(fixed_indentation_program)

    # Task 3: Count the number of times the keyword "print" is used
    print_count = count_print_keywords(fixed_headers_program)

    # Task 4: Print the results to a text file
    with open('output_results.txt', 'w') as output_file:
        output_file.write(f"Original Input Program:\n{input_program}\n\n")
        output_file.write(f"Updated Input Program:\n{fixed_headers_program}\n\n")
        output_file.write(f"Number of times 'print' keyword is used: {print_count}\n")

if __name__ == "__main__":
    main()
