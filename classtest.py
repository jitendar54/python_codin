li = [{"name": "jitendra", "age": 14}, {"name": "barun", "age": 24}, {"name": "arpita", "age": 21}]




def sort_by_name(item):
    return item["name"]

def sort_by_age(item):
    return item["age"]


print("Sorted by name:", sorted(li, key=sort_by_name))
print("Sorted by age:", sorted(li, key=sort_by_age))
