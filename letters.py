# Given
list_of_words = ['abc','cfe','eaf']

dict_of_organization = {}
for i, v in enumerate(list_of_words):
    dict_of_organization[v[0]] = []
    for d, l in enumerate(v):
        if v[0] != l:
            dict_of_organization[v[0]].append(l)

print(dict_of_organization)