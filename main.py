from fastapi import FastAPI
from tkinter import Tk, Label, Button

app = FastAPI()


@app.get("/")
def main():
    root = Tk()

    label = Label(root, text="Hola mundo")
    label.pack()

    button = Button(root, text="Salir", command=root.destroy)
    button.pack()

    root.mainloop()
    return {"message": "Aplicación Tkinter ejecutada exitosamente"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)