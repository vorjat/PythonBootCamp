import sys

if len(sys.argv) == 3:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
else:
    print("Nieprawidlowa ilosc parametrow!")

mails = []

with open(input_file) as f:
    for line in f:
        cleaned_line = line.strip().lower()
        if cleaned_line not in mails and line.count('@') == 1:
            mails.append(cleaned_line)

mails.sort()

with open(output_file, 'w') as f:
    for m in mails:
        f.write(m+"\n")
