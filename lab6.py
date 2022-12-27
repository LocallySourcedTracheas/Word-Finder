#Vanessa Junco
#Lab 6 Challenge 3
#COP2500 002
#10/15/22

def knight_check(word):
    song = "UCF charge onto the field. With our spirit, we’ll never yield. Black and gold, Charge right through the line. Victory is our cry, V-I-C-T-O-R-Y. Tonight our Knights will shine!"
    lyrics = song.split()

    if word in lyrics:
        print(word)
        print("word found in lyrics")
        return True
    else:
        print(word)
        print("word not found in lyrics")
        return False
          
def main():
    word = input("Insert word that is in \"Charge On\" song\n")
    knight_check(word)
main()
