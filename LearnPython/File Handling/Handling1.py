# f = open("jokes.txt", "r")
# for line in f:
#     print(line)
# f.close()

# with open("jokes.txt", "r") as f:
#     for line in f:
#         print(line)

# with open("add.txt", "w") as f2:
#     f2.write("Adding to the file\n")
#     f2.write("Adding more to the file")

with open("add.txt", "w") as f2: #for overwriting the content of the file
    f2.write("Adding some content to the file\n")
    f2.write("Adding more magic to the file")

    #or

    f2.writelines([
        "\nEverything is awesome\n",
        "Everything is cool when you're part of a team\n",
    ])

with open("scores.csv", "r") as f3:
    for line in f3:
        print(line)