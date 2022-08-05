#consigue cierta pagina web con dominio correlativo
import wget
#for del correlativo
for i in range(263884, 1000000):
    #sitio scrap
    site_url = 'http://www.cybertruffle.org.uk/cgi-bin/robi.pl?glo=esp&location=CL&assoge=&assorg=&link=&organism=' + str(i)
    #metodo
    file_name = wget.download(site_url)
    #imprime resultados
    print(file_name)