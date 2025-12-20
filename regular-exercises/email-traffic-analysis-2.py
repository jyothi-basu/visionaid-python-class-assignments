#Analyzing emails log and finding it's spam accuracy.

email_list= []
fh= open("mbox-short.txt", "r")
for line in fh:
    line= line.strip()
    if line.startswith("X-DSPAM-Confidence: "):
        spam_code= line[19:]
        spam_code= float(spam_code)
        email_list.append(spam_code)
fh.close()

print("detected Spam Email list: ", email_list)
print("Total number of spam emails detected: ", len(email_list))
print("Sum of all the spam values in this log: ", sum(email_list))