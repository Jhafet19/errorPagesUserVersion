class message:
    def __init__(self, type: str, message: str, code: int, img: str = None):
        self.type = type  # Tipo de mensaje (ej: "error", "success", "warning")
        self.message = message  # Contenido del mensaje
        self.code = code  # Código del mensaje (ejemplo: 200 para éxito, 400 para error)
        self.img = img  # Imagen opcional asociada al mensaje

    def __str__(self):
        return f"[{self.type.upper()}] Código {self.code}: {self.message} (Imagen: {self.img})"

    def to_dict(self):
        return {
            "tipo": self.type,
            "mensaje": self.message,
            "codigo": self.code,
            "imagen": self.img,
        }
