import pandas as pd
import openpyxl
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Cargar los datos desde 'xlsx'
df_work = pd.read_excel('dfwork.xlsx', sheet_name='Sheet1')
############ F U N C I O N E S ###########
def cantidad_filmaciones_mes(v_Mes):
    return 'test pelis mes'

def cantidad_filmaciones_dia(v_Dia):
    return 'test pelis dia'

def score_titulo(v_nom_pel):
    return 'test score'

def votos_titulo(v_titulo):
    return 'test votos'        

def get_actor(v_nom_actor):
    return 'test actor'

def get_director(v_nom_dire):
    return 'test director'

def recomendacion(gustos):
    return 'test director'

def open_readme():
    return 'test readme'

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/consulta")
async def consulta(request: Request, opcion: int):
    if opcion == 1:
        v_Mes = input("Ingrese un mes a consultar (Ejemplo: Enero, Febrero): ")
        cantidad_filmaciones_mes(v_Mes)
        return {"message": "Consulta realizada pel x mes"}
    elif opcion == 2:
        v_Dia = input("Ingrese el día a consultar (Ejemplo: Lunes, Martes): ")
        cantidad_filmaciones_dia(v_Dia)
        return {"message": "Consulta realizada pel x día"}
    elif opcion == 3:
        v_nom_pel = input("Ingrese el nombre de una película (Ejemplo: 'Star Wars', 'Casablanca'): ")
        score_titulo(v_nom_pel)
        return {"message": "Consulta realizada pel score"}
    elif opcion == 4:
        v_titulo = input("Ingrese el nombre de una película (Ejemplo: 'Jumanji', 'Grease'): ")
        votos_titulo(v_titulo)
        return {"message": "Consulta realizada votos"}
    elif opcion == 5:
        v_nom_actor = input("Ingrese el nombre de un actor (Ejemplo: 'Tom Hanks', 'Frank Sinatra'): ")
        get_actor(v_nom_actor)
        return {"message": "Consulta realizada actor"}
    elif opcion == 6:
        v_nom_dire = input("Ingrese el nombre de un director (Ejemplo: 'Tom Hanks', 'Frank Capra'): ")
        get_director(v_nom_dire)
        return {"message": "Consulta realizada director"}
    elif opcion == 7:
        gustos = input("Ingrese su gusto en pelis o nombre de peli: ")
        recomendacion(gustos)
        return {"message": "Consulta realizada recomendación"}
    elif opcion == 8:
        open_readme()
        return {"message": "Consulta realizada"}
  
    else:
        return {"message": "Opción no válida"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
