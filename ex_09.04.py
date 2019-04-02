# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
#  The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fname = input("Enter file name: ")
try:
    fhandle = open(fname)
except:
    print("File not found.")
    quit()

counts = dict()
words = []
for line in fhandle:
    if line.startswith('From '):
        lineSplitted = line.split()
        words.append(lineSplitted[1])

for word in words:
    counts[word] = counts.get(word, 0) + 1

biggestWord = None
biggestValue = 0
for k, v in counts.items():
    if k is None or v > biggestValue:
        biggestWord = k
        biggestValue = v

print(biggestWord,biggestValue)