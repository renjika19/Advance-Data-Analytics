filename = input('Enter file name')
if len(filename) < 1 : filename = "WordExercise.txt"
filehandle = open(filename)


words = {}


for line in filehandle:
    words = line.split()

    print(len(words))