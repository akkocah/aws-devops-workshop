majority_vote = ["A", "B", "B", "B", "C", "A"]

setlist1 = set(majority_vote)
setlist = list(setlist1)
counter = []
count = 0
for i in setlist:
    count = 0
    for j in majority_vote:
        if j == i:
            count = count + 1
    counter.append(count)

largest = counter[0]
for i in counter:
    if i > largest:
        largest = i

c = 0
for i in counter:
    if i != largest:
        c = c + 1
    else:
        c = c
        break

mostvoted = setlist[c]
print("Most voted one is", mostvoted, "with", largest, "votes.")


        

