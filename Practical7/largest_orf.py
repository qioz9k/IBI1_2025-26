import re
seq = 'AAGAUCACUGCAAUGUGUGUGUCUGUUCUGAGAGGCUAAAAG'
pattern = r'(?=(AUG(?:.{3})*?(?:UAA|UAG|UGA)))'

matches = re.findall(pattern, seq)

longest_orf = ""
longest_orf_length = 0

for orf in matches:
    if len(orf) > longest_orf_length:
        longest_orf = orf
        longest_orf_length = len(orf)

result = re.search(pattern, seq)

if result:
    longest_orf = result.group(1) + result.group(0)[3:-3]

longest_orf = longest_orf[:-3]
longest_orf_length = len(longest_orf)

print("Longest ORF:", longest_orf)
print("Length:", longest_orf_length)