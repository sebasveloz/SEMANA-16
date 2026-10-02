class Usuario:
    def __init__(
        self,
        identificacion: str,
        nombre: str,
        correo: str,
        usuario: str,
        contrasena: str,
        rol: str
    ) -> None:
        if not identificacion:
            raise ValueError("La identificación es obligatoria.")

        if not nombre:
            raise ValueError("El nombre es obligatorio.")

        if not correo:
            raise ValueError("El correo es obligatorio.")

        if not usuario:
            raise ValueError("El usuario es obligatorio.")

        if not contrasena:
            raise ValueError("La contraseña es obligatoria.")

        roles_validos = ["Administrador", "Empleado", "Cliente"]

        if rol not in roles_validos:
            raise ValueError(
                "El rol debe ser Administrador, Empleado o Cliente."
            )

        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo
        self.usuario = usuario
        self.contrasena = contrasena
        self.rol = rol

    def __str__(self) -> str:
        return (
            f"Identificación: {self.identificacion} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo} | "
            f"Rol: {self.rol}"
        )

    def to_dict(self) -> dict[str, str]:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo,
            "usuario": self.usuario,
            "contrasena": self.contrasena,
            "rol": self.rol
        }