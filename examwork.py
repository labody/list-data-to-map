
"""
 This module converts data from a list into a Dictionary
"""

# Here is the data we are to convert into
# a dictionary currently in a List
data = [
    ["Seyram", "seyram@gmail.com", ["024566543", "054342323"]],
    ["Caleb", "caleb@gmail.com", ["020234543", "020234532"]],
    ["Kingsley", "kingsley@gmail.com", ["0503452323", "0234532344"]],
    ["Philia", "philia@gmail.com", ["0245644543", "054889323"]],
    ["Kimkay", "kimkay@gmail.com", ["0207774543", "030234532"]],
    ["Gertrude", "gertrude@gmail.com", ["0511152323", "024444344"]],
    ["Kwesi", "kay@gmail.com", ["4533434343", "2345632345"]]
]

# Let's create an empty dictionary to hold the data
info_dict = {}

# Let's loop through each element in data and populate them into the dictionary
for item in data:
    name, email, phone_numbers = item
    info_dict[name] = {"Email": email, "Phone Numbers": phone_numbers}    

# Output the resulting dictionary
print(info_dict)

# Accessing individual info

print(info_dict["Caleb"]["Email"])
























