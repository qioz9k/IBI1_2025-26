import matplotlib.pyplot as plt
# ask user for stop codon
target_stop = input("Enter stop codon (TAA/TAG/TGA): ").upper()

while target_stop not in ["TAA", "TAG", "TGA"]:
    target_stop = input("Invalid input. Enter TAA, TAG or TGA: ").upper()


# dictionary for codon counts
codon_counts = {}

# open fasta file
infile = open("D:/IBI/IBI1_2025-26-master/Practical7/stop_genes.fa", "r")
current_header = ""
current_seq = ""

# read fasta file
for line in infile:

    line = line.rstrip()

    if line.startswith(">"):
        # process previous gene
        if current_header and current_seq:
            # only process genes containing chosen stop codon
            if target_stop in current_header:
                longest_orf = ""
                # find all ATG codons
                for start in range(len(current_seq)-2):
                    if current_seq[start:start+3] == "ATG":
                        # move in frame
                        for i in range(start, len(current_seq)-2, 3):
                            codon = current_seq[i:i+3]
                            # chosen stop codon found
                            if codon == target_stop:
                                # ORF without stop codon
                                orf = current_seq[start:i]
                                # keep longest ORF
                                if len(orf) > len(longest_orf):
                                    longest_orf = orf
                                break

                # count codons
                if longest_orf:
                    for i in range(0, len(longest_orf), 3):
                        codon = longest_orf[i:i+3]
                        if len(codon) == 3:
                            if codon in codon_counts:
                                codon_counts[codon] += 1
                            else:
                                codon_counts[codon] = 1

        # start next gene
        current_header = line
        current_seq = ""

    else:
        current_seq += line

# process last gene
if current_header and current_seq:
    if target_stop in current_header:
        longest_orf = ""
        for start in range(len(current_seq)-2):
            if current_seq[start:start+3] == "ATG":
                for i in range(start, len(current_seq)-2, 3):
                    codon = current_seq[i:i+3]
                    if codon == target_stop:
                        orf = current_seq[start:i]
                        if len(orf) > len(longest_orf):
                            longest_orf = orf
                        break

        if longest_orf:
            for i in range(0, len(longest_orf), 3):
                codon = longest_orf[i:i+3]
                if len(codon) == 3:
                    if codon in codon_counts:
                        codon_counts[codon] += 1
                    else:
                        codon_counts[codon] = 1

infile.close()


# print codon counts
print("\nCodon counts:\n")

for codon in sorted(codon_counts):
    print(codon, codon_counts[codon])


# pie chart
labels = list(codon_counts.keys())
sizes = list(codon_counts.values())

plt.figure(figsize=(17, 15))
plt.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",
    pctdistance=1.03,
    labeldistance=1.1,
    textprops={'fontsize': 5}
)
plt.title(f"Codon usage upstream of {target_stop}",pad=20)
plt.savefig(f"{target_stop}_codon_usage.png", dpi=150, bbox_inches='tight')

plt.show()

print(f"\nPie chart saved as {target_stop}_codon_usage.png")
