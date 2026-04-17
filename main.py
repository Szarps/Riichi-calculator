# from src.infrastructure.database import Database
# from src.application.service import MiServicio
# from src.interfaces.api import App


def bootstrap():
    # 1. Preparo la infraestructura
    # db = Database(url="sqlite:///prod.db")

    # 2. Inyecto la db en la lógica de aplicación
    # servicio = MiServicio(repository=db)

    # 3. Paso todo a la interfaz (ej. una API)
    # app = App(logic=servicio)

    return app


if __name__ == "__main__":
    app = bootstrap()
    app.run()  # Arranca la magia
