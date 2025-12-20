#Finding outgoing emails in a company's log.

outgoing_email_list= []

fh= open("mbox-short.txt", "r")
for line in fh:
    line= line.strip()
    if line.startswith("From: "):
        outgoing_email_list.append(line)
fh.close

print("Out going emails list: ", outgoing_email_list)
print("Total Out going emails: ", len(outgoing_email_list))