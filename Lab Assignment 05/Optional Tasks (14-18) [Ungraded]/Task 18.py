tup_list = [(20, 80), (31, 80), (1, 22), (88, 11), (27, 11)]

grouped_dict = {}

for tup in tup_list:
    group_key = tup[1]
    if group_key in grouped_dict:
        grouped_dict[group_key].append(tup)
    else:
        grouped_dict[group_key] = [tup]
        
print(grouped_dict)