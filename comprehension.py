my_family = {
    "mother": {"name": "Juanita", "hair color": "blonde"}, 
    "father": {"name": "Mick", "hair color": "red"}, 
    "brother": {"name": "Tom", "hair color": "brown"}, 
    "wife": {"name": "Sophia", "hair color": "brown"}, 
    "son": {"name": "Lee", "hair color": "blonde"}
}

def my_family_list():
    exp = [f'My {m} is {v["name"]} and their hair is {v["hair color"]}.' for (m, v) in my_family.items()]
    for i in exp:
        print(i)

my_family_list()