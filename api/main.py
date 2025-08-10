from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.db.mongo_db import connect_to_mongo,close_mongo_connection
from api.v1.endpoints import students,staff,firebase_storage,event,gallery,contact,setting,auth
from api.db.firebase_client import connect_to_firebase

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
    connect_to_firebase()



@app.on_event("shutdown")
def shutdown_db():
    close_mongo_connection()


app.include_router(students.router,prefix="/api/v1/students",tags=["Students"])
app.include_router(staff.router,prefix="/api/v1/staff",tags=["Staff"])
app.include_router(firebase_storage.router,prefix="/api/v1/store",tags=["firebase store"])
app.include_router(event.router,prefix="/api/v1/event",tags=["Event"])
app.include_router(gallery.router,prefix="/api/v1/gallery",tags=["Gallery"])
app.include_router(contact.router,prefix="/api/v1/contact",tags=["Contact"])
app.include_router(setting.router,prefix="/api/v1/setting",tags=["Setting"])
app.include_router(auth.router,prefix="/api/v1/auth",tags=["Auth"])