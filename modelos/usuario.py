class Usuario:
    def __init__(
        self,
        identificacion: str,
        nombre: str,
        correo: str
    ) -> None:
        if not identificacion:
            raise ValueError(
                "La identificación es obligatoria."
            )

        if not nombre:
            raise ValueError(
                "El nombre es obligatorio."
            )

        if not correo:
            raise ValueError(
                "El correo es obligatorio."
            )

        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo

    def __str__(self) -> str:
        return (
            f"Identificación: {self.identificacion} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo}"
        )

    def to_dict(self) -> dict[str, str]:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo
        }