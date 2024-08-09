d = {"Alice": 3, "Bob": 5, "Dave": 4, "Victor": 10}

sorted_dict = sorted(d.items(), key=lambda x: x[0], reverse=True)

for k, v in sorted_dict:
    print(k, "->", v)
