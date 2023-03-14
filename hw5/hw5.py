#Q1
# Python program to write in file text
def my_file(my_id):
    with open(my_id,"w") as file:
        file.write("My name is aya\n")
        file.write(" Last name is kaabyia\n")
        file.write("I'm 27 years old\n")
        file.write("my phone number: 0584772017\n")
        file.close()
my_file("my_id.txt")


# #Q2
# from collections import Counter
def word_count(file_path):
    with open(file_path, "r") as file:
        txt= file.read().split()
        # count =0
        sample_dictionary={}
        for word in txt:
            count = sample_dictionary.get(word, 0)
            count += 1
            sample_dictionary[word] = count
    print(sample_dictionary)
    return sample_dictionary
word_count("../my_id.txt")





# #Q3

def file_read_from_head(my_file, nlines):
    from itertools import islice
    with open(my_file) as file:
        for line in islice(file, nlines):
            print(line)

file_read_from_head("../my_id.txt", 2)



#Q4
def longest_world(my_filee):
    my_filee = open(my_filee, "r")
    txt = my_filee.read().split()
    longest_w = len(max(txt, key=len))
    l_word = [textword for textword in txt if len(textword) == longest_w]
    print("The longest words from a text file:")
    print(l_word)

longest_world("my_id.txt")




#Q5
class revers_sentence:
    def reverse(self, sentence):
        return ' '.join(reversed(sentence.split()))


print(revers_sentence().reverse('aya mutlak'))





#Q6
class IOString():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = "aya"

    def print_String(self):
        print(self.str1.upper())

str1 = IOString()
str1.get_String()
str1.print_String()






#Q7
class Rectangle():
    def __init__(self, height, width):
        self.height = height
        self.width  = width

    def rectangle_area(self):
        return self.height*self.width

newRectangle = Rectangle(9, 7)
print(newRectangle.rectangle_area())





#Q8 chalenge
class find_validity:
   def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

print(find_validity().is_valid_parenthese("{}[]"))
print(find_validity().is_valid_parenthese("()[{"))





#Q9
class py_solution:
    def sub_sets(self, ssgitet):
        return self.subsetsRecur([], sorted(sset))

    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]

print(py_solution().sub_sets([4,5,6]))