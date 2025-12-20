# Counting and printing the email domains in a file.

domains_count= {}
fh= open("mbox-short.txt", "r")
for line in fh:
    line= line.strip()
    if line.startswith("From "):
        words= line.split()
        email= words[1]
        domain= email.split("@")[1]
        if domain in domains_count:
            domains_count[domain] += 1
        else:
            domains_count[domain] = 1

domain_tuple= []
for key in domains_count:
    domain_tuple.append((domains_count[key], key))

domain_tuple.sort(reverse= True)
print("Domains in this email list: ")
for d in domain_tuple:
    print(d[1], ":", d[0])