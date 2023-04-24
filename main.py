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

            
    def trainer():
        import random
        oldnum = random.randint(1, 10000) # select random number
        zeroes = len(str(oldnum))+len(str(oldnum))%2 # do the same zero calculation thing for the zeroes preview
        num = str(oldnum).zfill(zeroes)
        if input(f"WHAT NUMBER IS {num} IN LETTERS?\nANSWER --> ") == convert(num): # check if user responds correctly
            print("MASTERMIND")
        else:
            print(f'ABSOLUTE BUFFOON --- IT WAS {convert(num)}')
    while True:
        trainer()



if __name__ == '__main__': # checks if the code is ran as a file
    main() # starts the main function
