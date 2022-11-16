
readLines('data/entity/10004.pl') -> entity



# ID --------------------------------------------------------------------
str_match_all(entity[23], "organism=\\s*(.*?)\\s*&glo=esp") -> id
id[[1]][,2] -> id


# Nombre cientifico -----------------------------------------------------
str_match_all(entity[23], "<I>\\s*(.*?)\\s*</I>") -> nombre_cient
nombre_cient[[1]][,2] -> nombre_cient


# Autor -----------------------------------------------------------------
str_match_all(entity[23], '</A></B>\\s*(.*?)\\s*</A></B>') -> autor
autor[[1]][,2] -> autor

# # si autor = .sp, NA 
# 
# 
# cbind(id, nombre_cient, autor) 
# mutate(autor = ifelse(autor == 'sp.',
#                       '',
#                       autor))|> view()



