import json

# Ask user for a path to the json file and load the data
fh = open(input("please input your path of json"))
data = json.load(fh)
fh.close()
print(data)

# Serialization:convert the original data struture into a string
print("\nSerialization: convert the original data structure into a string ")
print("\nThe type of data structure before serialization:",type(data))

# Serialization
orig_str = json.dumps(data)
print("\nAfter serialization, the data is: {0}, its type is :{1}".format(orig_str,type(orig_str)))

#Write the string to a file (ask user for a file name for that too).
#Don't forget to close the file.
def newFile():
    filename = input("\nPlease enter 'filename.txt' here >>>")
    with open(filename, "w") as f:
        userinput = orig_str
        f.write(userinput)
        f.write("\n")
    return filename
fh.close()

# Read the string back from the file. Close the file afterwards.
fh = open(newFile())
for i in fh:
    print(i)
fh.close()

print("\nRead the string from the file above and deserialize it")

# Deserialization
str_orig = json.loads(orig_str)
print("\nAfter deserialization, the data is:{0}, its type is :{1}".format(str_orig,type(str_orig)))

# Comparison
ds1 = data
ds2 = str_orig
def my_compare(ds1, ds2):
    if type(ds1) == type(ds2):
        return "The Same"
    else:
        return "Not the same"

print("\nCompare the two data structures:{}".format(my_compare(ds1, ds2)))
