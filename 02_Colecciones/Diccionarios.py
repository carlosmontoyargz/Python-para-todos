#!/usr/bin/env python
# La clave de un diccionario puede ser cualquier valor inmutable
movies = {"Love Actually": "Richard Curtis",
          "Kill Bill": "Tarantino",
          "Amelie": "Jean-Pierre Jeunet"}

print(movies)

movies["Kill Bill"] = "Quentin Tarantino"
print(movies)
print(movies["Amelie"])
