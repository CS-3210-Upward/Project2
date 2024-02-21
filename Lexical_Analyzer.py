class LexicalAnalyzer:
    """Given a string, this class will return a syntatically correct program"""
    
    def __init__(self, file): #initializer function
        self.file = file
    
    def check_identation( file):
        """This function checks for correct indentation"""
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.strip() != "":
                    if len(line) % 4 != 0:
                        line = "    " + line
        with open("updated_file.txt", "w") as f:
            f.writelines(lines)
        return "updated_file.txt"
    
    def verify_function_headers(file):
        """This function verifies the syntactic correctness of all function headers"""
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if "def" in line:
                    if line[-1] != ":":
                        line = line[:-1] + ":"
        with open("updated_file.txt", "w") as f:
            f.writelines(lines)
        return "updated_file.txt"
    
    def count_print(file):
        """This function counts the occurrences of the keyword "print" """
        with open(file, 'r') as f:
            lines = f.readlines()
            count = 0
            for line in lines:
                count += line.count("print")
        with open("count.txt", "w") as f:
            f.write(str(count))
        return "count.txt"
    
    def output_to_file(file, updated_file, count):
        """This function outputs to a text file the original input program, the updated input program, and the count of occurrences of the keyword "print." """
        with open(file, 'r') as f:
            original = f.read()
        with open(updated_file, 'r') as f:
            updated = f.read()
        with open(count, 'r') as f:
            count = f.read()
        with open("output.txt", "w") as f:
            f.write("Original input program:\n" + original + "\n\nUpdated input program:\n" + updated + "\n\nCount of occurrences of the keyword 'print': " + count)
        return "output.txt"
    
    