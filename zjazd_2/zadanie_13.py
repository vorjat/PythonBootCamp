lista = [x/10 for x in range(11)]
print(lista)

lista = {(x,x**2, x**3) for x in range(-10,11)}
print(lista)

zbior_napisow = {"a","abc","asdas","dsdfdfsfdsf","klsjkdfsjgkl","dfjgklfdjg"}
print({x:len(x) for x in zbior_napisow})