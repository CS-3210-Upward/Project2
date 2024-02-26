def correct_indentation(filename):
    """
    Corrects indentation to a 4-space standard for non-empty lines.
    """
    updated_lines = []
    with open(filename, 'r') as file:
        for line in file:
            stripped_line = line.lstrip()
            # Calculate required indentation based on the stripped line's leading spaces
            indentation_level = len(line) - len(stripped_line)
            corrected_indentation = ' ' * (indentation_level // 4 * 4)
            updated_lines.append(corrected_indentation + stripped_line)
    
    updated_filename = 'updated_' + filename
    with open(updated_filename, 'w') as file:
        file.writelines(updated_lines)
    
    return updated_filename

def count_print_statements(filename):
    """
    Counts the occurrences of 'print' in the file.
    """
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            # Simple check for 'print' in the line
            count += line.count('print')
    return count

def output_results(original_filename, updated_filename, print_count):
    """
    Outputs the original and updated file contents, along with the count of 'print' statements.
    """
    with open('final_output.txt', 'w') as file:
        file.write("Original File Content:\n")
        with open(original_filename, 'r') as orig_file:
            file.write(orig_file.read())
        
        file.write("\n\nUpdated File Content (Corrected Indentation):\n")
        with open(updated_filename, 'r') as upd_file:
            file.write(upd_file.read())
        
        file.write(f"\n\nCount of 'print' statements: {print_count}\n")
    
    return 'final_output.txt'

def main():
    original_filename = 'fake.py'
    updated_filename = correct_indentation(original_filename)
    print_count = count_print_statements(updated_filename)
    final_output = output_results(original_filename, updated_filename, print_count)
    print(f"Analysis completed. Results are in {final_output}")

if __name__ == "__main__":
    main()