def ecrypted(stri):   #call a function receuve a variable
    dic3={}    # empty dictionary definition
    dic= {}
    # str = str.lower()   #to lower the litter
    for i in stri.lower():     # lope for to count all of the litters
        if i.isalpha():
            count = dic.get(i, 0)
            count += 1
            dic[i] = count

    # to sorted the dict and to but key and value with lambda and revers the dict to begening from the big vale to litel.
    dic2 = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
    print(dic2)
    s=list(dic2)
    # to add and merge two list in dictonary (zip)
    dic3 = dict(zip(s[:5], ['e', 't', 'o', 'r']))
    dic3.update(zip(['e', 't', 'o', 'r'], s[:5]))

    print(dic3)
    return dic3

with open("file.txt", "w+") as file:
    file.write("Puackich, hvhnkrally oaths phufhck. All ymr nhhd is Pykemn.\n")
    file.write("J.U.U.U Kmltin.\n")
    file.write("mmps iks nmk eio; ---> hkmu\n")
    file.seek(0)
    ecrypted(file.read())



#part2
def decrypted_text(txt):
    new_string = ''     # str
    most_common_dict =ecrypted(txt)    #creat to the function in part 1
    keys = list(most_common_dict.keys())       # list of keys dict in part1
    for letter in txt:    # loop for letters if the letter in the list change the liter else no change the letter
        if letter.lower() in keys:
            new_string += most_common_dict[letter.lower()]
        else:
            new_string += letter
    return new_string

print(decrypted_text('''Puackich, hvhnkrally oaths phufhck. All ymr nhhd is Pykemn.'
J.U.U.U Kmltin.
mmps iks nmk eio; ---> hkmu'''))


#part3
# path the file in part 3
def decrypted_file(file_path):
    my_file = open(file_path,"a+") # a+ because we need to apdat in the file, to add text in the file.
    my_file.seek(0)    # to start from the begining
    ecrypted=my_file.read()
    decrypted_txt=decrypted_text(ecrypted)
    my_file.write("\n The encryption for the above text is: \n"+decrypted_txt) # to sdd this sentax
    with open("results.txt","w+") as result_file:    # opine new file results txt and add the decrypted text
        result_file.write(decrypted_txt)
    my_file.close
    result_file.close()

decrypted_file("file.txt")


#part 4

def longest_world(my_filee):
    my_filee = open(my_filee, "r")    #path for results.txt wiht help the function, r for read the file witheuot apdate or write.
    wordsList = my_filee.read().split()    # Getting the list of words of a file
    longest_w = len(max(wordsList, key=len))     # finding the length of the longest word in the above words list.

    # Storing all the words having the maximum length(longest word length)
    # Here, we are checking all the words whose length is equal to that of the longest word
    l_word = [textword for textword in wordsList if len(textword) == longest_w]
    print("The following are the longest words from a text file:")
    print(l_word)

longest_world("results.txt")



def numberline(resultfail):    # function that input the file in part3 and count the number of the line (output)
    my_file_ = open(resultfail,"r")        # the file result
    lines = len(my_file_.readlines())     # len readline in the file metoda readline
    print('Total Number of lines:', lines)
numberline("results.txt")



def main():
# i try but dont sucsess


    if __name__ == "__main__":
        main()