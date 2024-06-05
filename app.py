from fastapi import FastAPI, HTTPException, Request
from domain.Crud import Crud
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()
crud = Crud()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/crear/")
async def crear_persona(request: Request):
    try:
        data = await request.json()
        nombre = data.get('nombre')
        apellido = data.get('apellido')
        correo = data.get('correo')
        password = data.get('password')
        crud.crearUsuario(nombre, apellido, correo, password)
        return {"mensaje": "Persona creada correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def verificar_credenciales(correo: str, password: str):
    usuario = crud.getUsuario(correo)
    if usuario and usuario["contraseña"] == password:
        return True
    return False

@app.post("/login/")
async def login(request: Request):
    data = await request.json()
    correo = data.get('correo')
    password = data.get('password')
    if verificar_credenciales(correo, password):
        return {"mensaje": "Inicio de sesión exitoso"}
    else:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

@app.get("/nombre_usuario/")
async def obtener_nombre_usuario(correo: str):
    usuario = crud.getUsuario(correo)
    if usuario:
        return usuario
    else:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

@app.get("/obtener/ejercicios")
def obtener_ejercicios(request: Request):
    if request.method == 'GET':
        ejercicios = crud.getEjercicios()
        return JSONResponse(content=ejercicios)

@app.post("/crear/ejercicio")
async def crear_ejercicio(request: Request):
    try:
        data = await request.json()
        ejercicio = data.get('ejercicio')
        descripcion = data.get('descripcion')
        repeticiones = data.get('repeticiones')
        series = data.get('series')
        imagen = data.get('imagen')
        type = data.get('type')
        crud.crearEjercicio(ejercicio, descripcion, repeticiones, series, type, imagen)
        return True
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/ejercicios")
async def get_ejercicios_by_type(type: str):
    try:
        ejercicios = crud.getEjerciciosByType(type)
        return JSONResponse(content=ejercicios)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/eliminar/ejercicio/{ejercicio_id}")
async def eliminar_ejercicio(ejercicio_id: int):
    try:
        crud.eliminarEjercicio(ejercicio_id)
        return {"message": "Ejercicio eliminado exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/actualizar/ejercicio/{id}")
async def actualizar_ejercicio(id: int, request: Request):
    try:
        data = await request.json()
        ejercicio = data.get('ejercicio')
        descripcion = data.get('descripcion')
        repeticiones = data.get('repeticiones')
        series = data.get('series')
        imagen = data.get('imagen')
        tipo = data.get('tipo')
        crud.actualizarEjercicio(id, ejercicio, descripcion, repeticiones, series, tipo, imagen)
        return {"message": "Ejercicio actualizado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
