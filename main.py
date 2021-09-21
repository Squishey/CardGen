from random import randint

def generate(type):
    card = ""
    firstNum = ['4', '5']
    visa = ['4026', '417500', '4508', '4844', '4913', '4917']
    masterCard = [2221,2720]
    cardFirstNum = firstNum[randint(0,1)]
    #print(f'first num: {str(cardFirstNum)}')
    card = card + cardFirstNum

    if type.lower() == "visa" or type == "0":
        issuer = visa[randint(0,5)]
        card = card + issuer
        #print(f'Card Issuer number: {str(issuer)}')
        issuer = str(issuer)

    elif type.lower() == "mastercard" or type == "1":
        issuer = randint(masterCard[0], masterCard[1])
        card = card + str(issuer)
        #print(f'Card Issuer number: {str(issuer)}')
        issuer = str(issuer)

    if len(issuer) == 4:
        accountNumber = str(randint(1000000000,9999999999))
        card = card + accountNumber
        #print(f'Card account number: {str(accountNumber)}')
    
    elif len(issuer) == 5:
        accountNumber = str(randint(100000000, 999999999))
        card = card + accountNumber
        #print(f'Card account number: {str(accountNumber)}')
    
    elif len(issuer) == 6:
      accountNumber = str(randint(10000000, 99999999))
      card = card + accountNumber
      #print(f'Card account number: {str(accountNumber)}')


    cardForOtherThing = card + "0"
    algorythm = card [:: -1]
    algorythm = algorythm [::2]
    nonMultipliedNumbers = cardForOtherThing [:: -1]
    nonMultipliedNumbers = nonMultipliedNumbers [::2]
    nonMultipliedNumbers = nonMultipliedNumbers [2:]
    nonMultipliedNumbersArray = []
    for number in nonMultipliedNumbers:
      nonMultipliedNumbersArray.append(number)
    nonMultipliedNumbersArray.insert(0, card[len(card) - 2])
    #print(f'Card: {card[:: -1]}')
    #print(f'Non Multiplied numbers: {nonMultipliedNumbers[:: -1]}')
    #print(f'Multiplied numbers: {algorythm[:: -1]}')

    multipliedNumbers = []

    for number in algorythm:
        number = int(number)
        number = number * 2
        if number >= 10:
            strNumber = str(number)
            firstNumber = strNumber[0]
            secondNumber = strNumber[1]
            number = int(firstNumber) + int(secondNumber)
        multipliedNumbers.append(str(number))
        
    sumMultiplied = 0
    sumNotMultiplied = 0
    for number in range(0, len(multipliedNumbers)):
      sumMultiplied = sumMultiplied + int(multipliedNumbers[number])
      #print(f'suma: {sumMultiplied}')

    for number in range(0, len(nonMultipliedNumbersArray)):
      sumNotMultiplied = sumNotMultiplied + int(nonMultipliedNumbersArray[number])
      #print(f'suma: {sumNotMultiplied}')

    lastNumber = sumNotMultiplied + sumMultiplied
    lastNumber = str(lastNumber)
    lastNumber = lastNumber[-1]
    lastNumber = int(lastNumber)
    if lastNumber !=  0:
      lastNumber = 10 - lastNumber
    #print(f'Card last number : {str(lastNumber)}')
    card = card + str(lastNumber)
    cvv = randint(100,999)
    return(f"""
    
    Card number: {card}
    Expiracy date: {randint(1,12)}/{randint(2022,2026)}
    Cvv: {cvv}
    """)

while True:
  input = input("Type visa or mastercard: ")
  print(generate(input))
  break
