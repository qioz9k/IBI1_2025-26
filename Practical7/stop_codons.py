import re

infile = open("../Practical7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r")
outfile = open("../Practical7/stop_genes.fa", "w")

current_header = ""
current_seq = ""


for line in infile:
    line = line.rstrip()

    if line.startswith(">"):
      
        if current_header and current_seq:
            
            atg_pos = current_seq.find("ATG")
            if atg_pos != -1:
              
                found = False
                stop_codon = ""
                for i in range(atg_pos, len(current_seq)-2, 3):
                    c = current_seq[i:i+3]
                    if c in ["TAA", "TAG", "TGA"]:
                        stop_codon = c
                        found = True
                        break
                
                if found:
                    gene = current_header.split()[0][1:]
                    outfile.write(f">{gene} {stop_codon}\n")
                    outfile.write(current_seq + "\n")

     
        current_header = line
        current_seq = ""

    else:
        current_seq += line

if current_header and current_seq:
    atg_pos = current_seq.find("ATG")
    if atg_pos != -1:
        found = False
        stop_codon = ""
        for i in range(atg_pos, len(current_seq)-2, 3):
            c = current_seq[i:i+3]
            if c in ["TAA", "TAG", "TGA"]:
                stop_codon = c
                found = True
                break
        if found:
            gene = current_header.split()[0][1:]
            outfile.write(f">{gene} {stop_codon}\n")
            outfile.write(current_seq + "\n")

infile.close()
outfile.close()

  