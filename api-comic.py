from fastapi import FastAPI
from schemas.student import Studen
from config.db import con
from model.index import students


app = FastAPI()


@app.get('/api/students')
async def index():
    return {'Hello': 'world'}


# @app.post('/api/student')
# async def store(student: Studen):
#     data = con.execute(students.insert().values(
#         name=student.name,
#         email=student.email,
#         age=student.age,
#         country=student.country
#     ))

#     return data.is_insert
