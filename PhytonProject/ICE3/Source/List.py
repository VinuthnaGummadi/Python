
def new_list(input_list):
    return [input_list[0], input_list[len(input_list)-1]]

input_string = input("Enter numbers into list with ,:")

input_list = input_string.split(",")

generated_list = new_list(input_list)

print (generated_list)