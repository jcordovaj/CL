import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

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
    return 'test recomendacion'

def open_readme():
    return 'test readme'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/consulta", methods=["GET"])
def consulta():
    opcion = request.args.get("opcion", type=int)
    
    if opcion == 1:
        v_Mes = request.args.get("v_Mes")
        cantidad_filmaciones_mes(v_Mes)
        return {"message": "Consulta realizada pel x mes"}
    elif opcion == 2:
        v_Dia = request.args.get("v_Dia")
        cantidad_filmaciones_dia(v_Dia)
        return {"message": "Consulta realizada pel x día"}
    elif opcion == 3:
        v_nom_pel = request.args.get("v_nom_pel")
        score_titulo(v_nom_pel)
        return {"message": "Consulta realizada pel score"}
    elif opcion == 4:
        v_titulo = request.args.get("v_titulo")
        votos_titulo(v_titulo)
        return {"message": "Consulta realizada votos"}
    elif opcion == 5:
        v_nom_actor = request.args.get("v_nom_actor")
        get_actor(v_nom_actor)
        return {"message": "Consulta realizada actor"}
    elif opcion == 6:
        v_nom_dire = request.args.get("v_nom_dire")
        get_director(v_nom_dire)
        return {"message": "Consulta realizada director"}
    elif opcion == 7:
        gustos = request.args.get("gustos")
        recomendacion(gustos)
        return {"message": "Consulta realizada recomendación"}
    elif opcion == 8:
        open_readme()
        return {"message": "Consulta realizada"}
    else:
        return {"message": "Opción no válida"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
