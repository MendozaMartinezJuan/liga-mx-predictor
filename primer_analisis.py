
import pandas as pd

# Datos ficticios de partidos de Liga MX
partidos = {
    "Equipo": ["América", "Cruz Azul", "Toluca", "Chivas", "Monterrey"],
    "Partidos": [5, 5, 5, 5, 5],
    "Victorias": [4, 3, 3, 2, 2],
    "Empates": [1, 1, 0, 2, 1],
    "Derrotas": [0, 1, 2, 1, 2],
    "Goles_favor": [12, 10, 11, 8, 9],
    "Goles_contra": [4, 5, 7, 6, 8]
}

# Convertimos los datos en una tabla
df = pd.DataFrame(partidos)

# Calculamos puntos
df["Puntos"] = (
    df["Victorias"] * 3 +
    df["Empates"]
)

# Calculamos diferencia de goles
df["Diferencia"] = (
    df["Goles_favor"] -
    df["Goles_contra"]
)

# Ordenamos la tabla
df = df.sort_values(
    by=["Puntos", "Diferencia"],
    ascending=False
)

print("\nTABLA DE RENDIMIENTO")
print(df.to_string(index=False))

print("\nEquipo con más puntos:")
print(df.iloc[0]["Equipo"])
