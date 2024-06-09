with open("my_text.txt", mode="a") as file:
    file.write("\nI am th best")
    contacts=file.read()

    print(contacts)