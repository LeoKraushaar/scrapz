query = ["1", " tIMe and MEATr  ", "", " ", "6 ", "", "9  8"]
items = []
for q in query:
    if q.strip() == "":
        continue
    
    items.append("-".join(q.strip().lower().split()))
    

print(items)