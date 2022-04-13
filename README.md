# API V0

## Tecnologías Aplicadas

---

- Python3 (Fastapi)

## Migraciones

---

#### Seguir los siguientes pasos para generar/actualizar las tablas en la base de datos ligada

#### Generar carpeta alembic (Solo para aplica para primera vez )

1. Correr en la terminal a nivel root del proyecto el siguiente script `$ alembic init alembic`

#### Actualizar tablas de base de datos

##### Generar migración y sincronizarla con la base de datos

- Correr los siguientes comandos

1. `alembic revision --autogenerate -m "titulo migracion"`
2. `alembic upgrade head`
