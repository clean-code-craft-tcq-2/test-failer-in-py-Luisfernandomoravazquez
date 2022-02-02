from turtle import color
from misaligned_support_functions import resize_array_to_biggest_element
from misaligned_support_functions import get_color_index
from misaligned_support_functions import get_columns_from_color_map_array
from misaligned_support_functions import get_color_map_array_from_columns

major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]

def get_color_map_array():
    colorMap_array = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            colorIndex = get_color_index(i,j)
            colorMap_array.append([colorIndex,major,minor])
    return colorMap_array

def color_map_array_align_elements(color_map_arrayMapArray):
    
    index_array, major_array, minor_array = get_columns_from_color_map_array(color_map_arrayMapArray)
    
    index_array = resize_array_to_biggest_element(index_array)
    major_array = resize_array_to_biggest_element(major_array)
    minor_array = resize_array_to_biggest_element(minor_array)
    
    return get_color_map_array_from_columns(index_array,major_array,minor_array)

def color_map_array2text(colorMapArray, separator="|"):
    color_map_to_Print = ""
    for possibleCombination in colorMapArray:
        for column in possibleCombination:
            color_map_to_Print += str( column ) + separator
        color_map_to_Print = color_map_to_Print[:-1] # Remove last separator
        color_map_to_Print += '\n'
    color_map_to_Print = color_map_to_Print[:-1] # Remove last '\n'
    return color_map_to_Print

def print_color_map(colorMapText):
    print(colorMapText)
    return len(major_colors) * len(minor_colors), colorMapText

# Test resize_array_to_biggest_element()
inputArray = ["a","abc","123456","25"]
expectedOutput = ["a     ","abc   ","123456","25    "]
output = resize_array_to_biggest_element(inputArray)
assert(output == expectedOutput)

# Test get_color_index()
output = get_color_index(2,2)
expectedOutput = 13
assert(output == expectedOutput)

# Test get_columns_from_color_map_array()
output1,output2,output3 = get_columns_from_color_map_array([["he","good","my"],["llo","bye","friend"]])
expectedOutput1 = ["he","llo"]
expectedOutput2 = ["good","bye"]
expectedOutput3 = ["my","friend"]
assert(output1==expectedOutput1)
assert(output2==expectedOutput2)
assert(output3==expectedOutput3)

# Test get_color_map_array_from_columns()
output = get_color_map_array_from_columns(["he","llo"],["good","bye"],["my","friend"])
expectedOutput = [["he","good","my"],["llo","bye","friend"]]
assert(output == expectedOutput)

# Main funcionality
colorMap = get_color_map_array()
colorMap_aligned = color_map_array_align_elements(colorMap)
colorMap_text = color_map_array2text(colorMap_aligned)
result, printedText = print_color_map(colorMap_text)

# Main Testing
printedText_array = printedText.split("\n")
assert(result == len(printedText_array))
index_divisor1_prev = printedText_array[0].find("|")
index_divisor2_prev = printedText_array[0].rfind("|")
for zeroBased_row,line in enumerate(printedText_array):
    index_divisor1 = line.find("|")
    index_divisor2 = line.rfind("|")
    assert(str(zeroBased_row+1) == line[:index_divisor1].strip())
    assert(index_divisor1 == index_divisor1_prev)
    assert(index_divisor2 == index_divisor2_prev)

print("All is well\n")
