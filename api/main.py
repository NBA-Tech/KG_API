from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.mongo_db import connect_to_mongo,close_mongo_connection
from v1.endpoints import students,staff
app = FastAPI()

origins = [
    "*" 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            
    allow_credentials=True,
    allow_methods=["*"],              
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_db():
    connect_to_mongo()


@app.on_event("shutdown")
def shutdown_db():
    close_mongo_connection()


app.include_router(students.router,prefix="/api/v1/students",tags=["Students"])
app.include_router(staff.router,prefix="/api/v1/staff",tags=["Staff"])