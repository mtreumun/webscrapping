#consigue cierta pagina web con dominio correlativo
import wget
#path objetivo
path='E:/misdesarrollos/webscrapping/bib'
#for del correlativo
for i in range(108533, 108534):
    #sitio scrap
    site_url='http://www.cybertruffle.org.uk/cgi-bin/biblshow.pl?bibref=' + str(i)
    #metodo
    file_name = wget.download(site_url, out = path+str(i)+str('.pl'))
    #imprime resultados
    print(file_name)