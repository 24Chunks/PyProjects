#lambda function examples
#functiom(params):
# return           =                           lambda params: return



f = lambda x : x*5 #


print(f(4))


old_list = [0, 1,2,3,4]

new_list = list(map(lambda x: x*5, old_list)) # THIS IS THE USE OF LAMBDA IT WILL MULTIPLY EACH VALUE OF olf_list*5

print(new_list)


new_l = list(filter(lambda x: x % 2 == 0, old_list))

print(new_l)
