def stopnie():
    stopnie_c = range(-20, 40, 5)
    for i in stopnie_c:
        print(f"C:{i}, F:{32+9*i/5}")

stopnie()