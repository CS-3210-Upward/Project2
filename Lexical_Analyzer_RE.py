import re

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
                if re.search(r'\bdef\b', line):
                    inside_function = True
                    match = re.match(r'\s*def\s*([a-zA-Z_]\w*)\s*\((.*?)\)\s*:', line)
                    if match:
                        func_name = match.group(1)
                        args_part = match.group(2)
                        
                        args = [arg.strip() for arg in args_part.split(',')]
                        args_part = ", ".join(args)

                        # Replace specific strings before the name of the function with 'def'
                        if 'fed' in func_name or 'dfe' in func_name or 'efd' in func_name or 'fde' in func_name:
                            func_name = 'def'

                        func_line = f"{func_name}({args_part}):"

                        updated_lines.append(func_line + '\n')
                    else:
                        # Handle the case where the def line does not follow the expected format
                        updated_lines.append(line.rstrip() + ":\n")
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
                count += len(re.findall(r'\bprint\b', line))
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
