import reflex as rx

# Inicializamos una clase donde se almacenara el estado de la aplicación
class State(rx.State):
    pass

# Creamos un Componente de texto
def index() -> rx.Component:
    return (
        rx.text(
            'Hola, mundo!',
            background = 'darkblue',
            color = 'white'
        )
    )

# Inicializamos nuestra aplicación
app = rx.App()

# Agregamos una página a nuestra aplicación
app.add_page(index)

# Compilamos nuestra aplicación
app.compile()