
def powerSum(powers,x):
    counter =0
    suma=0
    lenght = len(powers)
    indice = 0
    limite = pow(2,lenght)

    while(indice<limite):
        binary = format(indice, f'0{lenght}b')

        i=0
        while(i<len(binary)):
            if(binary[i]=='1'):
                suma = suma + powers[i]

            i = i+1

        if (suma == x):
            counter = counter + 1

        indice = indice+1
        i=0
        suma =0

    return counter

def main():
    #I = input()
    #I = I.split()

    x = int(input())
    n = int(input())


    powers=[]

    i=1
    while(pow(i,n) <= x):
        powers.append(pow(i,n))
        i = i+1


    print(powerSum(powers,x))


main()
