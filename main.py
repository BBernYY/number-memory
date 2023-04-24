def main():
    import data
    def convert(num):
        zeroes = len(str(num))+len(str(num))%2 # calculate zeroes before number
        num = str(num).zfill(zeroes) # add said zeroes
        newnum = []
        for i in range(len(num)):
            for k in range(10):
                if num[i] == str(k): # check if the number is same as the expected
                    if i % 2 == 0: # if even
                        v = data.consonants[k] # add the correct consonant
                    else: # if uneven
                        v = data.vowels[k] # add the correct vowel
                    newnum.append(v)
                    break
        return ''.join(newnum) # combine everything
    def anti_convert(text):
        part_of_double = False
        import data
        outnum = "" # a string, so I can append numbers to it digit by digit.
        for i in range(len(text)):
            if part_of_double:
                part_of_double = False
                continue
            if text[i] in data.consonants or text[i] in data.vowels or ((text[i] + text[i+1] in data.consonants or text[i]+text[i+1] in data.vowels) if i != len(text)-1 else False):
                if ((text[i] + text[i+1] in data.consonants or text[i]+text[i+1] in data.vowels) if i != len(text)-1 else False):
                    part_of_double = True
                    outnum += str(data.consonants.index(text[i]+text[i+1])) if text[i]+text[i+1] in data.consonants else str(data.vowels.index(text[i]+text[i+1])) # if its a consonant, revert it to the correct number, and same with vowel
                else:
                    outnum += str(data.consonants.index(text[i])) if text[i] in data.consonants else str(data.vowels.index(text[i])) # if its a consonant, revert it to the correct number, and same with vowel
        return int(outnum)

            
    def trainer(text_to_num=True, num_to_text=True):
        import random
        oldnum = random.randint(1, 10000) # select random number
        zeroes = len(str(oldnum))+len(str(oldnum))%2 # do the same zero calculation thing for the zeroes preview
        num = str(oldnum).zfill(zeroes)
        con = convert(num)
        option = random.random() # get a random number for the option
        if (option < 0.5 and num_to_text) or not text_to_num:
            ans = input(f"WHAT NUMBER IS {num} IN LETTERS?\nANSWER --> ")
            if ans == con: # check if user responds correctly
                print("MASTERMIND")
            else:
                print(f'ABSOLUTE BUFFOON --- IT WAS {con}, AND YOU SAID {ans} WHICH WOULD BE {anti_convert(ans)}')
        elif (option > 0.5 and num_to_text) or (not text_to_num):
            ans = input(f"WHAT IS {con} IN NUMBERS?\nANSWER --> ")
            if ans == num: # check if user responds correctly
                print("MASTERMIND")
            else:
                print(f'ABSOLUTE BUFFOON --- IT WAS {num}, AND YOU SAID {ans} WHICH TRANSLATES TO {convert(ans)}')
    while True:
        trainer()



if __name__ == '__main__': # checks if the code is ran as a file
    main() # starts the main function
