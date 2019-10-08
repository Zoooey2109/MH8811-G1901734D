################################################################
#                                                              #
#                              Classwork                       #
#                                                              #
################################################################

# Program C1_Finding Smallest Value
lst = [9, 41, 12, 3, 74, 15]
smallest_so_far = None
print("Program C1\n\nBefore", smallest_so_far)
for the_num in lst :
    if smallest_so_far is None:
        smallest_so_far = the_num
    elif the_num < smallest_so_far:
        smallest_so_far = the_num
    print(smallest_so_far, the_num)
print("Smallest number in the list:", smallest_so_far)


# Program C2_Basic Descriptive Statistics

# Define function min()
def my_min(lst):
    smallest_so_far = None
    for the_num in lst :
        if len(lst)==0:
            print("None")
        elif smallest_so_far is None:
            smallest_so_far = the_num
        elif the_num < smallest_so_far:
            smallest_so_far = the_num
    return smallest_so_far

# Define function max()
def my_max(lst):
    largest_so_far = None
    for the_num in lst :
        if len(lst)==0:
            print("None")
        elif largest_so_far is None:
            largest_so_far = the_num
        elif the_num > largest_so_far:
            largest_so_far = the_num
    return largest_so_far

# Define function average()
def my_average(lst):
    count_1 = 0
    sum = 0
    for value in lst :
        if len(lst)==0:
            print("None")
        else:
            count_1 = count_1 + 1
            sum = sum + value
    return sum/count_1

#Define function median()
def my_median(lst):
    lst.sort()
    r = int(len(lst)/2)
    if len(lst) % 2 is 1:
        median = lst[r]
    else:
        median = (lst[r-1] + lst[r])/2
    return median

# Define function range()
def my_range(lst):
    if len(lst)==0:
            print("None")
    else:
        range = my_max(lst) - my_min(lst)
    return range

print("\n\nProgram C2\n")
print(lst)
print("min:", my_min(lst))
print("max:", my_max(lst))
print("average:", my_average(lst))
print("median:", my_median(lst))
print("range:", my_range(lst))

# Program C3_ run C2 against a file
def getFileLines(fname):
    fhandle = open(fname)
    lines = []
    for line in fhandle:
        line = line.rstrip()
        if line :
            lines.append(line)
    return lines

my_list = getFileLines("MH8811-04-Data.csv")

print(my_list)

# Convert all the str in the dataset into float
my_list= list(map(float, my_list))

print("\n\nProgram C3\n")
print("min of my_list:", my_min(my_list))
print("max of my_list:", my_max(my_list))
print("average of my_list:", my_average(my_list))
print("median of my_list:", my_median(my_list))
print("range of my_list:", my_range(my_list))



################################################################
#                                                              #
#    Homework: Program H1 Advanced Descriptive Statistics      #
#                                                              #
################################################################

def my_variance(my_list):
    average = my_average(my_list)
    count = 0
    sum = 0
    for number in my_list :
        sum = sum + (number - average)**2
        count = count +1
    return sum/(count-1)

print("\n\nProgram H1\n")
print("variance:",my_variance(my_list) )
        
