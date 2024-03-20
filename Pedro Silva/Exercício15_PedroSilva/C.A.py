#fput = input('Select the file>>>')
fopen = open('mbox-short.txt')

email_count = {}
unique_emails = []

for line in fopen:
    line = line.strip()
    if line.startswith('From') and '@' in line:
        words = line.split()
        email = words[1]
        pieces = email.split('@')
        formatted_email = pieces[0] + '@' + pieces[1]

    #remove the space in text / checks the line if starts with 'From' or have '@' in the line / organize the pieces

        if formatted_email not in unique_emails:
            unique_emails.append(formatted_email)
            email_count[formatted_email] = 1
        else:
            email_count[formatted_email] += 1

print(email_count)

tup = email_count.items()
list = list()
for key, value in tup:
    list.append((value, key))

slist = (sorted(list, reverse = True))
for k, v in slist:
    print(v, k)





    