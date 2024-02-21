class LexicalAnalyzer:
    """Given a string, this class will return a syntatically correct program"""
    
    def __init__(self, file): #initializer function
        self.file = file
    
    def check_identation( file):
        """This function checks for correct indentation"""
        with open(file, 'r') as f: #open the file and read the lines
            lines = f.readlines() 
            for line in lines: #iterate through the lines
                if line.strip() != "": #strip the line of any white space
                    if len(line) % 4 != 0: #if the number of spaces is not a multiple of 4, or a tab
                        line = "    " + line #fix the indentation
        with open("updated_file.txt", "w") as f: #write the updated lines to a new file
            f.writelines(lines) 
        return "updated_file.txt" #return the name of the new file
    
    def verify_function_headers(file): 
        """This function verifies the syntactic correctness of all function headers"""
        with open(file, 'r') as f: #open the file and read the lines
            lines = f.readlines() 
            for line in lines: #iterate through the lines
                if "def" in line: #if the line is a function header
                    if line[-1] != ":": #if the function header is not correct
                        line = line[:-1] + ":" #remove last character
        with open("updated_file.txt", "w") as f:
            f.writelines(lines)
        return "updated_file.txt"
    
    def count_print(file):
        """This function counts the occurrences of the keyword "print" """
        with open(file, 'r') as f:
            lines = f.readlines() #open the file and read the lines
            count = 0 #initialize count to 0
            for line in lines:
                count += line.count("print")#count the occurrences of the keyword "print"
        with open("count.txt", "w") as f:
            f.write(str(count))
        return "count.txt"
    
    def output_to_file(file, updated_file, count):
        """This function outputs to a text file the original input program, the updated input program, and the count of occurrences of the keyword "print." """
        with open(file, 'r') as f: #write the original input program to a new file
            original = f.read() 
        with open(updated_file, 'r') as f: #write the updated input program to a new file
            updated = f.read()
        with open(count, 'r') as f:#write the count of occurrences of the keyword "print" to a new file
            count = f.read()
        with open("output.txt", "w") as f:
            f.write("Original input program:\n" + original + "\n\nUpdated input program:\n" + updated + "\n\nCount of occurrences of the keyword 'print': " + count)
        return "output.txt" #return the names of the new files
    
    