import collections


# ATTEMPT 2:

def associate(input, output, go=0):
    memory_file = open("learning_memory.txt", "r+")
    memory = memory_file.read()

    input_locater = "#IN:" + input + "#"
    if input_locater in memory:
        memory_location = memory.index(input_locater)
        new_memory = memory[:memory_location + 6] + str(output) + memory[memory_location + 6:]

        print("\n" + new_memory + "\n")

        memory_file.close()

    else:
        memory_file.write("\n#IN:" + input + "#")
        memory_file.close()
        associate(input, output, 1)
        return

    memory_file_overwrite = open("learning_memory.txt", "w")
    memory_file_overwrite.write(new_memory)
    memory_file_overwrite.close()

    if go == 1:
        memory_file_addend = open("learning_memory.txt", "a")
        memory_file_addend.write("-" + input + "-")
        memory_file_addend.close


def learning():
    new_input = -1
    new_output = -1
    while 1:
        new_input = input("Input (letter): \n").upper()
        # shuts down if you enter "."
        if (new_input == "."):
            break
        new_output = input("Output (number): \n")
        if (new_output == "."):
            break
        associate(new_input, new_output)


def predict(input):
    memory_file = open("learning_memory.txt", "r")
    memory = memory_file.read()

    input_locater = "#IN:" + input + "#"
    if input_locater in memory:
        start = memory.index(input_locater) + 6
        end = memory.index("-" + input + "-")
        data = memory[start:end]
        predicted_output = int((collections.Counter(data).most_common(1)[0])[0])
        occurences = (collections.Counter(data).most_common(1)[0])[1]
        strength = occurences / len(data)

        print("Predicted Output of Input '" + input + "': " + str(predicted_output) + "\nOccurences: " + str(occurences) + "\nStrength: " + str((strength*100))[:5] + "%")

        return predicted_output

        memory_file.close()
    else:
        print("No data for input '" + input + "' was found in memory.")
        return
        memory_file.close()


# Run Functions:

#learning()
predict("A")


# make class for result, make predicted output an object










'''
def learning():
    memory_file = open("learning_memory.txt", "r+")
    memory = memory_file.read()

    new_input = "A"
    new_output = 1


    def associate(input, output):
        input_locater = "#IN:" + input + "#"
        if input_locater in memory:

            print("check")

            memory_location = memory.index(input_locater)

            temp = open("temp.txt", "wb")
            for line in memory_file:
                if line.startswith(input_locater):

                    print("check")

                    addition = line.strip() + (output + ",")
                    temp.write(addition)
                    temp.close()
                    shutils.move("temp", "learning_memory.txt")


            temp.close()


    associate(new_input, new_output)

    memory_file.close()
'''


