dna_string = ""
with open("rosalind_dna.txt" , "r") as f :
    dna_string = f.read()

a_count = dna_string.count("A")
c_count = dna_string.count("C")
g_count = dna_string.count("G")
t_count = dna_string.count("T")

print(f"{a_count} {c_count} {g_count} {t_count}")