"""
Upward
CS 3210
"""
import re  # unused but maybe useful for alternative use
import keyword
import builtins

builtin_functions = [func for func in dir(builtins) if callable(getattr(builtins, func))]
keywords = keyword.kwlist
words = builtin_functions + keywords


class LexicalAnalyzer:
    def __init__(self, file):
        self.file = file

    def check_indentation(self):
        """This function checks for correct indentation"""
        with open(self.file, 'r') as f:
            lines = f.readlines()
            updated_lines = []

            current_indentation = 0
            for i, line in enumerate(lines):
                if line.strip() != "":
                    leading_spaces = len(line) - len(line.lstrip())
                    target_indentation = current_indentation

                    if leading_spaces % 4 == 0:
                        # The line has correct indentation
                        current_indentation = leading_spaces
                    else:
                        # Fix indentation based on the previous line
                        target_indentation = (leading_spaces // 4) * 4
                        line = " " * target_indentation + line.lstrip()

                    updated_lines.append(line)

            with open("output.txt", "w") as f:
                f.write("Original input program:\n")
                f.writelines(lines)
                f.write("\n\nUpdated input program:\n")
                f.writelines(updated_lines)

    def verify_function_headers(self):
        """This function verifies the syntactic correctness of all function headers"""
        with open(self.file, 'r') as f:
            lines = f.readlines()
            inside_function = False
            updated_lines = []

            for i, line in enumerate(lines):
                components = line.split()
                
                if components[0] == 'def':
                    inside_function = True
                    test = True
                    while test:
                        # Check for parentheses
                        if "(" in line and ")" in line:
                            # Split the line into function name and arguments
                            func_name, args_part = line.split("(", 1)
                            print(func_name, args_part)
                            # Detect multiple arguments even if there is no comma
                            args_count = args_part.count(",")
                            print(args_count)
                            if args_count == 0:
                                # If there is no comma, assume one argument
                                args_part = args_part.strip()
                                print(args_part)
                                func_line = f"{func_name.strip()}({args_part}"
                                print(func_line)
                                if func_line[-1] != ':':
                                        func_line += ':'
                                print(func_line)
                                updated_lines.append(func_line + '\n')
                                test = False
                            else:
                                # If there is a comma, split arguments and add commas if needed
                                args = args_part.split(",")
                                print(args)
                                args = [arg.strip() for arg in args]
                                args_part = ", ".join(args)
                                print(args_part)
                                func_line = f"{func_name.strip()}({args_part}"
                                print(func_line)
                                if func_line[-1] != ':':
                                        func_line += ':'
                                print(func_line)
                                test = False
                                updated_lines.append(func_line + '\n')
                        elif ")" in line: 
                            print(components[2])
                            components[2] = f"({components[2]}"
                            line = ' '.join(components)
                            print(line)
                        else:
                            print(line)
                            line = line.strip()
                            if line[-1] == ':':
                                line = line.replace(":", "")
                            line = f"{line})"
                            
                else:
                    line_one = components[0]
                    line_two = line_one.split("(")
                    line_three = line_two[0]
                    line_four = line_three.split(":")
                    line_string = line_four[0]
                    if all(line_string not in i for i in words):
                        # Add 'def' keyword before the entire line
                        print(line)
                        line = f"def {line}\n"
                        print(line)
                    updated_lines.append(line)

        with open("output.txt", "a") as f:
                    f.write("\n\nUpdated function headers:\n")
                    f.writelines(updated_lines)


    def count_print(self):
        """This function counts the occurrences of the keyword 'print' """
        with open(self.file, 'r') as f:
            lines = f.readlines()
            count = 0
            for line in lines:
                count += line.count("print")
        with open("output.txt", "a") as f:
            f.write(f"\nCount of occurrences of the keyword 'print': {count}\n")

    def run_analysis(self):
        """Run the entire analysis process"""
        self.check_indentation()
        self.verify_function_headers()
        self.count_print()

        return "Analysis completed. Output written to: output.txt"


if __name__ == "__main__":
    file_path = "testfile2.py"

    # Create an instance of LexicalAnalyzer
    lexical_analyzer = LexicalAnalyzer(file_path)

    # Run the analysis
    result = lexical_analyzer.run_analysis()

    # Print the result
    print(result)
