def trinome():
    print("Saisie les 3 coefficients de ton trinome :")
    a = float(input("a : "))
    b = float(input("b : "))
    c = float(input("c : "))

    if a != 0 :
        alpha = round((-1*b)/(2*a), 2)
        delta = round((b**2)-(4*a*c), 2)
        beta = round((-1*delta)/(4*a), 2)

        if delta < 0 :
            signe = "donc ? < 0"
            racines = " Ce qui veut dire que ce trinome n'a pas de solutions."
            factoriser = "Impossible de factoriser."

        if delta > 0 : 
            x1 = round((-b+sqrt(delta))/(2*a), 2)
            x2 = round((-b-sqrt(delta))/(2*a), 2)
            signe = "donc ? > 0"
            racines = " Et les 2 racines de ce trinome sont : x1=%s & x2=%s" % (x1, x2)
            factoriser = "Et on peut factoriser avec la forme : a(x-x1)(x-x2)"

        if delta == 0 :
            x = round((-b)/(2*a), 2)
            signe = "donc ? = 0"
            racines = " Et la racine de ce trinome est : x=%s" % (x)
            factoriser = "Et on peut factoriser avec la forme : a(x-x0) ou x0= -b/2a"

        print("Le descriminant est égal à %s %s.%s %s" % (delta, signe, racines, factoriser))

    else:
        print("Ce n'est pas un trinome car a = 0. c'est une fonction affine."