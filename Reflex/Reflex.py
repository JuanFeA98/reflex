import reflex as rx

from Reflex.components.navbar import navbar


# Inicializamos una clase donde se almacenara el estado de la aplicación
class State(rx.State):
    pass

# Creamos el bloque donde se almacenarn nuestros componentes
def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        navbar(),
        navbar(),
        navbar(),
        navbar()
    )

# Inicializamos nuestra aplicación
app = rx.App()

# Agregamos una página a nuestra aplicación
app.add_page(index)

# Compilamos nuestra aplicación
app.compile()