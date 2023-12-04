import ast

def write_to_file(algo, problemList, outputFile):
    total = algo(problemList)
    outputFile.write("{}\n".format(total))

def run_problems(algo):
    inputFile = open("input.txt", "r")
    outputFile = open("output_" + algo.__name__ + ".txt" , "w")

    lines = inputFile.readlines()
    inputFile.close()

    problemInstance = []
    for line in lines:
        if line is not "\n":
            problemInstance.append(ast.literal_eval(line))
        else:
            write_to_file(algo, problemInstance, outputFile)
            outputFile.write("\n")

            problemInstance.clear()

    write_to_file(algo, problemInstance, outputFile)  
    outputFile.close()