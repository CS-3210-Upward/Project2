"""
Upward
CS 3210
"""

import re  # unused but maybe useful for alternative use


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
                if "def" in line:
                    inside_function = True
                    # Check for parentheses
                    if "(" in line and ")" in line:
                        # Split the line into function name and arguments
                        func_name, args_part = line.split("(", 1)

                        # Detect multiple arguments even if there is no comma
                        args_count = args_part.count(",")
                        if args_count == 0:
                            # If there is no comma, assume one argument
                            args_part = args_part.strip()
                        else:
                            # If there is a comma, split arguments and add commas if needed
                            args = args_part.split(",")
                            args = [arg.strip() for arg in args]
                            args_part = ", ".join(args)

                        # Replace specific strings before the name of the function with 'def'
                        if 'fed' in func_name or 'dfe' in func_name or 'efd' in func_name or 'fde' in func_name:
                            func_name = 'def'

                        # Replace any string before the name of the function with 'def'
                        func_line = f"{func_name.strip()}({args_part}):"

                        # Ensure there's a colon at the end
                        if not func_line.endswith(':'):
                            func_line += ':'

                        # Remove unnecessary closing parenthesis after the last argument
                        func_line = func_line.replace(")", "")

                        updated_lines.append(func_line + '\n')
                    elif "(" in line:
                        # Handle the case where there is an open parenthesis but no closing parenthesis
                        updated_lines.append(line.rstrip() + "):\n")
                    elif ")" in line:
                        # Handle the case where there is a closing parenthesis but no open parenthesis
                        updated_lines.append("(" + line.lstrip())
                    else:
                        # If there are no parentheses, just add parentheses and colon
                        updated_lines.append(line.rstrip() + "():\n")
                elif inside_function and line.strip() == "":
                    inside_function = False
                else:
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
