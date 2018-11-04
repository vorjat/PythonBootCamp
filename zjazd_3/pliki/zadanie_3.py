mails = []

with open("dane/emails.txt") as f:
    for line in f:
        cleaned_line = line.strip().lower()
        if cleaned_line not in mails and line.count('@') == 1:
            mails.append(cleaned_line)

mails.sort()
for m in mails:
    print(m)
