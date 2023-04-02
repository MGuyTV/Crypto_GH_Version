from pathlib import Path
#source https://stackoverflow.com/questions/6142689/initialising-an-array-of-fixed-size-in-python

#I'm suspecting "gnz" == "and", because of thie text's frequency, and the
#fact that "n" is currently deciphered, maybe "g" == "a", and "z" == "d"?

#Assuming "s" == "n", because of an "ose" if found where "o" and "e"
#are currently deciphered.

#I am now assuming that "t" is the period, becuase it is the last letter
#in the cipher text, and it appears to match in the deciphered text made
#so far

#We are assuming d = o just from looking at the current texti
#"d" was the only letter in more than one two letter word and that
#coincides with "o"

#We are assuming m = a space, and r = e space, because of letter frequencies
#Statically spaces occur almost twice as often as e's do.

def swap_letter(a, b, file_path):
    txt = Path(file_path).read_text()
    new_txt = [None] * len(txt)
    for i in range(len(txt)):
        if txt[i] == a:
            new_txt[i] = b
        else:
            new_txt[i] = txt[i]

    f = open("deciphered.txt", "w")
    f.write("".join(new_txt))
    f.close()


    return "".join(new_txt)
#abcdefghijklmnopqrstuvwxy "',-.;
if __name__ == "__main__":
    my_file = './cipher.txt'

    swap_letter(" ", "G", my_file)

    swap_letter("m", " ", "./deciphered.txt")
    
    swap_letter("r", "E", "./deciphered.txt")
    
    swap_letter("d", "O", "./deciphered.txt")

    swap_letter(".", "K", "./deciphered.txt")
    
    swap_letter("t", ".", "./deciphered.txt")
    
    swap_letter("s", "N", "./deciphered.txt")
    
    swap_letter("g", "A", "./deciphered.txt")
    
    swap_letter("z", "D", "./deciphered.txt")
    
    #I think "," == "v", because of the word "de,epow" I found
    #from the partially decipered text, other letters can also be
    #inferred by this.
    swap_letter(",", "V", "./deciphered.txt")

    #THOUSANDS OF YEARS AGOi FIVE AFRICAN TRIBES
    swap_letter("i", ",", "./deciphered.txt")
    
    swap_letter("p", "L", "./deciphered.txt")

    swap_letter("w", "P", "./deciphered.txt")
    
    #advanked, k likely equals c
    swap_letter("k", "C", "./deciphered.txt")
    
    #qo develop advanced, so q likely equals t
    swap_letter("q", "T", "./deciphered.txt")

    #to develop advanced tec'nolo+x, ' == h, + == g, x == y
    swap_letter("\'", "H", "./deciphered.txt")
    
    #ToCHAKA, so o == '
    swap_letter("o", "\'", "deciphered.txt")

    swap_letter("x", "Y", "./deciphered.txt")
   

    swap_letter("l", "R", "./deciphered.txt")
    
    #-ETEORITE
    swap_letter("-", "M", "./deciphered.txt")
    
    #EXaLOVER, so a == -
    swap_letter("a", "-", "./deciphered.txt")

    #AhRuCAN
    swap_letter("h", "F", "./deciphered.txt")

    swap_letter("u", "I", "./deciphered.txt")
    
    #eTEALING VIcRANIjM FROM "A.ANDA.
    swap_letter("e", "S", "./deciphered.txt")

    swap_letter("c", "B", "./deciphered.txt")

    swap_letter("j", "U", "./deciphered.txt")

    swap_letter("\"", "W", "./deciphered.txt")

    #bBLACK PANTHERb, b == "
    swap_letter("b", "\"", "./deciphered.txt")

    #E;TRACT T'CHALLA'S E;aLOVER, so ; == x
    swap_letter(";", "X", "./deciphered.txt")
    
    #THAN BE INCARCERATEDv T'CHALLA, so v == ;
    swap_letter("v", ";", "./deciphered.txt")

    #fABARI, so f == j, At this point, I realized that
    #this text is the exact synopsis of the movie from
    #the wikipedia article after trying to figure out
    #what name fABARI matched to, so I used that synopsis
    #to solve the rest, even though I had already found
    #most of the cipher on my own.
    swap_letter("f", "J", "./deciphered.txt")
   
    #yURI, there's a character named Zuri in the movie
    #, so y == z
    
    #AROUND THE WORLD TO HELP THEM CONnUER THEIR OPPRESSORS,
    # so n == q
    swap_letter("n", "Q", "./deciphered.txt")
    
    swap_letter("y", "Z", "./deciphered.txt")
    print(Path("./deciphered.txt").read_text())
