def find_longest_al_word(filename):
    longest_word = ""
    special_chars = ".,'?!/"

    with open(filename, 'r', encoding='utf-8') as f: # the file is opened, to which I add encoding='utf-8' to make python able to read certain special characters normally
        for line in f:
            line = line.lower()
            for c in special_chars:
                line = line.replace(c, " ")

            words = line.split()
            for word in words:
                if word.endswith("al"): # now that the lines have been broken into words, we look for those ending in "al"
                    if len(word) > len(longest_word): # here we specify that if the word ends in al, we want the longest al ending word
                        longest_word = word
    return longest_word

path = "Frankenstein.txt"
result = find_longest_al_word(path)

if result:
    print(f"The longest word ending in 'al' is: {result}")
else:
    print("No words ending in 'al' were found.") # in these last lines of code, we say to python thst, after having specified from which text it is going to retrive the words
    # that if he finds the longest word ending with al he should print it, and to print that none were found if that was the case