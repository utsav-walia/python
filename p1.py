dict1 = {"brand":"Maruti", "model":"Ciaz", "year":2021}
print(dict1["brand"])

print(len(dict1))
print(type(dict1))

print(dict1.keys())
print(dict1.values())

dict1["year"] = 2025
print(dict1)

dict1.update({"year":2015})
print(dict1)

dict1["color"] = "red"
print(dict1)

dict1.pop("model")
print(dict1)

newdict = dict1.copy()
print(newdict)



	
