letras = 'ab'

# retorna um objeto iterador
interadores = iter(letras)

# acessa elementos no contêiner, um de cada vez
print( 
    #elemento na posição 0
    next(interadores)
)

print(
    #elemento na posição 1
    next(interadores)
)
# OBS.: Quando não há mais elementos, levanta uma exceção StopIteration que informa no terminar.