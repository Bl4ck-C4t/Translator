import re
import random

def setup_translator(file="1337.txt"):
    f = open(file, "r")
    al = {}
    for line in f:
        regex = re.search(r"(?P<key>\w+|\w,\w) - (?P<value>.+)", line)
        if regex is None:
            continue
        key = regex.group("key")[0]
        value = regex.group("value").split(" ")
        al[key] = value
    rev_al = {}
    for k,v in al.items():
        for x in v:
            rev_al[x] = k

    def leetify(word):
        word = word.lower()
        translated = ""
        for x in word:
            if x not in al.keys():
                translated += x
                continue
            ls = al[x]
            translated += random.choice(ls)
        return translated

    def unleetify(word):
        translated = ""
        part = ""
        for x in word:
            part += x
            if part not in rev_al.keys():
                continue
            translated += rev_al[part]
            part = ""
        return translated

    return (leetify, unleetify)

def main():
    leet, unleet = setup_translator()
    mode = "l"
    while True:
        print("1. Load custom rules\n2. Change mode\n3. Translate\n4. Exit")
        ent = input("Enter option: ")
        if ent == "1":
            path = input("Enter file path: ")
            path = path if path != "" else "1337.txt"
            leet, unleet = setup_translator(path)
        elif ent == "2":
            print("'l' - for text to leet\n't' for leet to text")
            mode = input("Select mode: ")
            if mode not in ["l", "t"]:
                print("Wrong mode!")
                print("Defaulting to 'l'...")
                mode = "l"
            else:
                print("Mode successfully changed to '{}'".format(mode))

        elif ent == "3":
            if mode == "l":
                fn = leet
            elif mode == "t":
                fn = unleet
            word = input("Enter word to translate: ")
            word = fn(word)
            print("Translated: " + word)

        elif ent == "4":
            print("Goodbye")
            exit()



if __name__ == '__main__':
    main()