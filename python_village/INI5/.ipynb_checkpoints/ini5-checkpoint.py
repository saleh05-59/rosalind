modified_line_list = 0
with open("rosalind_ini5.txt" , "r") as f :
    first_line_list = f.readlines()

    modified_line_list = first_line_list[1::2]

with open("asnwer.txt" , "w") as t :
    t.writelines(modified_line_list)