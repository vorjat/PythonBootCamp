def rysuj(liczba=0):
    liczba = int(input("Podaj liczbe: "))

    if liczba == 0:
        print(f""" *** 
*   *
*   *
*   *
 ***""")
    elif liczba == 1:
        print(f"""   *
 * *
   *
   *
   *
    """)
    elif liczba == 2:
        print(f""" *** 
*   *
   *
  *
*****""")
    elif liczba == 3:
        print(f"""***** 
    *
  *** 
    *
*****""")
    elif liczba == 4:
        print(f"""*   *
*   *
*****
    *
	*""")
    elif liczba == 5:
        print(f"""*****
*
***** 
	*
*****""")
    elif liczba == 6:
        print(f"""*****
*
*****
*   *
*****""")
    elif liczba == 7:
        print(f"""*****
	*
	*
	*
	*
""")
    elif liczba == 8:
        print(f"""*****
*   *
***** 
*	*
*****
""")
    elif liczba == 9:
        print(f"""*****
*   *
***** 
	*
*****
""")

rysuj()