
class Strint(int):    
    def __init__(self,number):
        self.number = str(number)

    def __lt__(self, other):
        return (int(self.number)%10) < (int(other.number)%10)

    def __gt__(self, other):
        return (int(self.number)%10) > (int(other.number)%10)
        
    def __le__(self, other):
        return (int(self.number)%10) <= (int(other.number)%10)

    def __ge__(self, other):
        return (int(self.number)%10) >= (int(other.number)%10)

    def __eq__(self, other):
        return int(self.number)%10 == int(other.number)%10

    def __ne__(self, other):
        return int(self.number)%10 != int(other.number)%10 

    def __add__(self, other):
        if self.number == '0':
            self.number = other.number
        else:    
            self.number += other.number
        return int(self.number)

    def __sub__(self, other):
        length = len(self.number) - len(other.number)
        if self.number[length:] == other.number:
            self.number = self.number[0:length]
            if self.number == '':
                self.number = '0'
            return int(self.number)
        else:
            raise Exception("The subtraction is not valid!")


    def __len__(self):
        return len(self.number)

    def __call__(self): 
        exit = ''
        for i in range(len(self.number)):
            if self.number[i] == '0':
                exit += '۰'
            elif self.number[i] == '1':
                exit += '۱'
            elif self.number[i] == '2':
                exit += '۲'
            elif self.number[i] == '3':
                exit += '۳'
            elif self.number[i] == '4':
                exit += '۴'
            elif self.number[i] == '5':
                exit += '۵'
            elif self.number[i] == '6':
                exit += '۶'
            elif self.number[i] == '7':
                exit += '۷'
            elif self.number[i] == '8':
                exit += '۸'
            elif self.number[i] == '9':
                exit += '۹'
        return exit
