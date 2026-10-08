# getting the string from the text file
the_string = 0
with open("rosalind_ini6.txt" , "r") as f :
    the_string = f.read()

# splitting words in to a list 
the_string_divided = the_string.split()

# word counter company
word_counter = {}
for word in the_string_divided :
    if word in word_counter.keys():
        word_counter[word] += 1
    else :
        word_counter[word] = 1

# printing out the result
# for word , number in word_counter.items() :
#    print (f"{word} {number}")

imp_list = []
for word , number in word_counter.items() :
    imp_list.append(f"{word} {number}\n")
with open("result.txt" , "w") as t :
    t.writelines(imp_list)