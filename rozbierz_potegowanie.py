# coding: UTF-8
def rozb_pot(liczba, potega):

    i = 1
    a = liczba
    b = liczba
    pot = potega
    lic = int(liczba)
    lista =[]
#Exceptions
    if lic == 0:
        return '1'
    elif pot == 0:
        return '1'
    elif pot == 1:
        return b
    elif lic == 1:
        return '1'
    elif pot < 0:
        return "Ten program obsługuje tylko potęgi należące do zbioru liczb naturalnych"
    elif lic < 0:
        return "Ten program obsługuje tylko liczby należące do zbioru liczb naturalnych"
#calculations
    else:
        while i < pot:
            a = a + "*" + liczba
            i += 1
        i = 1
        lista.append(a)
        while i < lic:
            b = b + "+" + liczba
            i += 1
        i = 1
        if pot > 2:
            c = b
            k = lic ** (pot - 2)
            while i < k:
                c = c + "+" + b
                i += 1
            lista.append(c)
        else:
            lista.append(b)
        return lista