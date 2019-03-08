
import random

a_list = ["Here we go", None, None, None]

d_dictionary = {
    "a_list[0]": True,
    "a_list[1]": False,
    "a_list[2]": "true",
    "a_list[3]": "false",
}

_name_ = "_main_"
start_integer = 1
random_integer = random.randint(3, 20)


def concatenate_with_limit(phrase, condition, num, num_limit):
    if condition is True or condition == "true":
        while num <= num_limit:
            print(phrase + str(num))
            num += 1
        print("\nConcatenation done with limit " + "\" " + str(num_limit) + " \"")
    elif condition == "Not_valid_Key":
        print("\nNot a valid condition Key!")
    else:
        print("\nNo right condition for concatenation!")


if _name_ == "_main_":
    concatenate_with_limit((a_list[0]),
                           (d_dictionary.get("a_list[2]", "Not_valid_Key")),
                           start_integer, random_integer)
else:
    print("\n\"FOR Loop\" sample:")
    print("\nList of the values, excluding first:")
    for a_index in range(1, (len(a_list))):
        print(a_list[a_index])
    print("\nDictionary index:")
    for d_index in range(len(d_dictionary)):
        print(d_index)
    print("\nEnd")
