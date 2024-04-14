my_dict = {
    "brand" : "WV",
    "model" : "Polo",
    "year"  :2018,
    "year"  :2017,
}

print(my_dict["model"])
x=my_dict.get("model")

print(my_dict)

#to check if value/key is present

#if "model" in my_dict:
 #   print("yes, "model"is one of this in dictionary")
  #  my_dict.update({"year":1999})
  #  print(my_dict)
    
 #   del my_dict ["year"]
 #   print(my_dict)
    
   # car_dictionary = my_dict.copy
   # car_dictionary =dict(my_dict)
   
   child1 = dict(name= "Adam ", age =8)
   child2 = dict(name="ben", Age=10)
   child3 = {"name": "charlie", age:7}
   class_list={child1:child1 , "child2":child2,"child3":child3 }
   print(class_list)
   print(class_list["child2"]["name"])
   
    
    