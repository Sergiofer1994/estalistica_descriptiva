class Persona:
    def __init__(self, id_persona: int, origen: int, destino: int):
        self.id_persona = id_persona
        self.origen = origen
        self.destino = destino

    def es_par(self, piso: int) -> bool:
        return piso % 2 == 0

    def determinar_ascensor(self) -> str:
        origen_par = self.es_par(self.origen)
        destino_par = self.es_par(self.destino)

        # Regla: Si el origen y destino son de diferente paridad (par/impar),
        # ni el Ascensor A ni el B pueden completar el viaje directo.
        if origen_par != destino_par:
            return "Ascensor C (Único que conecta par con impar)"
        elif origen_par and destino_par:
            return "Ascensor A (Solo pisos pares)"
        else:
            return "Ascensor B (Solo pisos impares)"


# Definición de las personas según la situación
personas = [
    Persona(id_persona=1, origen=3, destino=8),
    Persona(id_persona=2, origen=6, destino=1),
    Persona(id_persona=3, origen=9, destino=2)
]

# Ejecución y visualización de resultados
for p in personas:
    ascensor = p.determinar_ascensor()
    print(f"Persona {p.id_persona}: Piso {p.origen} -> Piso {p.destino} | Tomar: {ascensor}")