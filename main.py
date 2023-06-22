from fastapi import FastAPI

app = FastAPI()

@app.get('/cantidad_filmaciones_mes/{mes}')
def cantidad_filmaciones_mes(mes: str):
    '''Se ingresa el mes y la función retorna la cantidad de películas que se estrenaron
       ese mes históricamente'''
    # respuesta = # Lógica para obtener la cantidad de películas por mes
    return {'mes': mes, 'cantidad': respuesta}

@app.get('/cantidad_filmaciones_dia/{dia}')
def cantidad_filmaciones_dia(dia: str):
    '''Se ingresa el día y la función retorna la cantidad de películas que se estrenaron ese día históricamente'''
    # respuesta = # Lógica para obtener la cantidad de películas por día
    #return {'dia': dia, 'cantidad': respuesta}
    return print('prueba films x día')

@app.get('/score_titulo/{titulo}')
def score_titulo(titulo: str):
    '''Se ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score'''
    #respuesta = # Lógica para obtener el score de un título
    #return {'titulo': titulo, 'anio': respuesta, 'popularidad': respuesta}
    return print('prueba score')

@app.get('/votos_titulo/{titulo}')
def votos_titulo(titulo: str):
    '''Se ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor promedio de las votaciones. 
    La misma variable deberá de contar con al menos 2000 valoraciones, 
    caso contrario, debemos contar con un mensaje avisando que no cumple esta condición y que por ende, no se devuelve ningún valor.'''
    #respuesta = # Lógica para obtener los votos de un título
    #return {'titulo': titulo, 'anio': respuesta, 'voto_total': respuesta, 'voto_promedio': respuesta}
    return print('prueba votos')

@app.get('/get_actor/{nombre_actor}')
def get_actor(nombre_actor: str):
    '''Se ingresa el nombre de un actor que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. 
    Además, la cantidad de películas en las que ha participado y el promedio de retorno'''
    #respuesta = # Lógica para obtener información del actor
    #return {'actor': nombre_actor, 'cantidad_filmaciones': respuesta, 'retorno_total': respuesta, 'retorno_promedio': respuesta}
    return print('prueb actor')

@app.get('/get_director/{nombre_director}')
def get_director(nombre_director: str):
    ''' Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. 
    Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.'''
    #respuesta = # Lógica para obtener información del director
    #return {'director': nombre_director, 'retorno_total_director': respuesta, 'peliculas': respuesta, 'anio': respuesta, 'retorno_pelicula': respuesta,     #'budget_pelicula': respuesta, 'revenue_pelicula': respuesta}
    return print('test dire')

@app.get('/recomendacion/{titulo}')
def recomendacion(titulo: str):
    '''Ingresas un nombre de película y te recomienda las similares en una lista'''
    respuesta = # Lógica para obtener la lista de recomendaciones
    #return {'lista_recomendada': respuesta}
    return print('test recomenda')