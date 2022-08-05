#abre cierto documento ubicado en la ejecucion de la terminal
with open("robi (262833).pl", "r") as f:
    #lee la cantidad de lineas
    s = f.readlines()
    #inspecciona cada linea
    for x in s:
        #regex
        if x.__contains__("cliquear aqu&iacute; para ver informaci&oacute;n nomenclatural & taxon&oacute;mica"):
            start = x.find("cliquear aqu&iacute; para ver informaci&oacute;n nomenclatural & taxon&oacute;mica")
            end = x.find("</A></B>")
            substring = x[start:end] + " - "
    f.close()
    #imprime resultados
print(s)
print(start)
print(end)
print(substring)
print(x)
