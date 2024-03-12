import random
class Main:

    #====================GuessNumber function====================
    def GuessNumber(self, number):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        a = 0
        b = int(number)
        state = ''
        while True:
            comp = random.randint(a,b)
            state = input('Is '+ str(comp) + ' too high(h), too low(l), or correct(c): ')
            if(state == 'h'): b= comp -1
            elif(state == 'l'): a = comp +1
            elif(state == 'c'): break
            else:
                print("Error choice please try again!")
                continue
        print("Welldone! The computer guessed your number "+str(comp)+" correctly!")
        # end def

#==================DO NOT CHANGE THE CODE BELOW=====================
    def main(self):
        number = input("Enter a range for guessed number: ")
        print("OUTPUT")
        self.GuessNumber(number)
        print("FINISH")
main = Main()
main.main()
