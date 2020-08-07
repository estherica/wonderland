#Dictionary

my_dict={"www.google.com":"8.8.8.8","www.facebook.com":"7.7.7.7","www.youtube.com":["5.5.5.5","4.4.4.4"],"www.google2.com":"www.estherica2.com"}
my_dict.update({"www.net4u.com":"13.13.13.13","www.estherica.com":"26.26.26.26"})
print(my_dict)

my_dict2={"www.instagram.com":"66.66.66.66"}
my_dict.update(my_dict2)
print(my_dict)

print("Number of Entries: " + str(len(my_dict)))

print(my_dict["www.estherica.com"])
my_dict["www.estherica.com"]="77.77.77.77"
print(my_dict["www.estherica.com"])
print(my_dict)

print("www.estherica.com" in my_dict)
print("www.estherica2.com" in my_dict)
print("www.estherica2.com" in my_dict.values())
