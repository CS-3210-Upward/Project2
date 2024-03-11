"""
Upward
CS 3210
"""
import re
import keyword
import builtins
import textwrap

builtin_functions = [func for func in dir(builtins) if callable(getattr(builtins, func))]
keywords = keyword.kwlist
words = builtin_functions + keywords


class LexicalAnalyzer:
    def __init__(self, file):
        self.file = file

    def check_indentation(self, lines):
        """This function checks for correct indentation"""
        updated_lines = []

        current_indentation = 0
        for line in lines:
            if line.strip() != "":
                leading_spaces = len(line) - len(line.lstrip())
                target_indentation = current_indentation

                # Check for the presence of ":" and adjust the indentation only if there is a mismatch
                if ":" in line and leading_spaces != target_indentation:
                    target_indentation = leading_spaces

                    # Remove excess indents if the number of spaces does not match the number of ":"
                    if leading_spaces > target_indentation:
                        line = line[target_indentation:]

                    line = textwrap.indent(line.lstrip(), " " * target_indentation)
                    current_indentation = target_indentation

            updated_lines.append(line)

        return updated_lines

    def verify_function_headers(self, lines):
        """This function verifies the syntactic correctness of all function headers"""
        inside_function = False
        updated_lines = []

        for i, line in enumerate(lines):
            components = line.split()

            if components and components[0] == 'def':
                inside_function = True
                test = True
                while test:
                    # Check for parentheses
                    if "(" in line and ")" in line:
                        # Split the line into function name and arguments
                        func_name, args_part = line.split("(", 1)

                        # Detect multiple arguments even if there is no comma
                        args_count = args_part.count(",")
                        if args_count == 0:
                            # If there is no comma, assume one argument
                            args_part = args_part.strip()
                            func_line = f"{func_name.strip()}({args_part}"
                            if func_line[-1] != ':':
                                func_line += ':'
                            updated_lines.append(func_line + '\n')
                            test = False
                        else:
                            # If there is a comma, split arguments and add commas if needed
                            args = args_part.split(",")
                            args = [arg.strip() for arg in args]
                            args_part = ", ".join(args)
                            func_line = f"{func_name.strip()}({args_part}"
                            if func_line[-1] != ':':
                                func_line += ':'
                            test = False
                            updated_lines.append(func_line + '\n')
                    elif ")" in line:
                        components[2] = f"({components[2]}"
                        line = ' '.join(components)
                    else:
                        line = line.strip()
                        if line and line[-1] == ':':
                            line = line.replace(":", "")
                        line = f"{line})"
            else:
                line_one = components[0] if components else ''
                line_two = line_one.split("(")
                line_three = line_two[0]
                line_four = line_three.split(":")
                line_string = line_four[0]
                if all(line_string not in i for i in words):
                    # Add 'def' keyword before the entire line
                    line = f"def {line}\n"
                updated_lines.append(line)

        return updated_lines

    def count_print(self, lines):
        """This function counts the occurrences of the keyword 'print' """
        count = 0
        for line in lines:
            count += line.count("print")

        return count

    def output(self):
        """Outputs when the process is complete"""
        with open(self.file, 'r') as f:
            lines = f.readlines()

        updated_indentation = self.check_indentation(lines)
        updated_functions = self.verify_function_headers(updated_indentation)
        print_count = self.count_print(updated_functions)

        with open("output.py", "w") as f:
            f.write("'''\n")
            f.write("Original input program:\n")
            f.writelines(lines)
            f.write("'''\n")
            f.write("\n\n# Updated output program:\n")
            f.writelines(updated_functions)
            f.write(f"\n# Count of occurrences of the keyword 'print': {print_count}\n")

        return "Process completed. Output written to: output.py"


if __name__ == "__main__":
    file_path = "testfile2.py"

    # Create an instance of LexicalAnalyzer
    lexical_analyzer = LexicalAnalyzer(file_path)

    # Run the analysis
    result = lexical_analyzer.output()

    # Print the result
    print(result)
