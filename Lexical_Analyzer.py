import re

class LexicalAnalyzer:
    def __init__(self, file):
        self.file = file

    def check_identation(self):
        """This function checks for correct indentation"""
        with open(self.file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.strip() != "":
                    if len(line) % 4 != 0:
                        line = "    " + line
        with open("updated_file.txt", "w") as f:
            f.writelines(lines)
        return "updated_file.txt"

    def verify_function_headers(self):
        """This function verifies the syntactic correctness of all function headers"""
        with open(self.file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if "def" in line:
                    if line[-1] != ":":
                        line = line[:-1] + ":"
        with open("updated_file.txt", "w") as f:
            f.writelines(lines)
        return "updated_file.txt"

    def count_print(self):
        """This function counts the occurrences of the keyword 'print' """
        with open(self.file, 'r') as f:
            lines = f.readlines()
            count = 0
            for line in lines:
                count += line.count("print")
        with open("count.txt", "w") as f:
            f.write(str(count))
        return "count.txt"

    def output_to_file(self, updated_file, count):
        """This function outputs to a text file the original input program, the updated input program, and the count of occurrences of the keyword 'print.' """
        with open(self.file, 'r') as f:
            original = f.read()
        with open(updated_file, 'r') as f:
            updated = f.read()
        with open(count, 'r') as f:
            count = f.read()
        with open("output.txt", "w") as f:
            f.write("Original input program:\n" + original + "\n\nUpdated input program:\n" + updated + "\n\nCount of occurrences of the keyword 'print': " + count)
        return "output.txt"

    def run_analysis(self):
        """Run the entire analysis process"""
        updated_file_indentation = self.check_identation()
        updated_file_headers = self.verify_function_headers()
        count_file = self.count_print()
        output_file = self.output_to_file(updated_file_headers, count_file)

        return f"Analysis completed. Output written to: {output_file}"

if __name__ == "__main__":
    file_path = "testfile1.py"  

    # Create an instance of LexicalAnalyzer
    lexical_analyzer = LexicalAnalyzer(file_path)

    # Run the analysis
    result = lexical_analyzer.run_analysis()

    # Print the result
    print(result)
