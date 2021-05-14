lastTicket = None
def lucky(ticket):
    
    def summa(number):
        number = str(number)
        while len(number) != 6:
            number = '0'+ number
        x = list(map(int,number))
        return sum(x[:3] ) == sum(x[3:] )
 
    return  'Счастливый' if  summa(ticket) == summa(lastTicket) else 'Несчастливый'