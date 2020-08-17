my_dict={"sarah":50500,"bella":30254,"tehila":40450,"shifra":10000,"esther":80700}
print("Two major donations: " + str(my_dict["sarah"]+my_dict["esther"]))

my_dict.update({"yehudit":my_dict["sarah"]+my_dict["esther"]})
print(my_dict)

print("\nThe number of entries is: " + str(len(my_dict)))
print("idan" in my_dict)
print("shifra" in my_dict)