#Import statements
from fastapi import FastAPI
from routes.students import student_router

#Create app
app =FastAPI()
#register your router
app.include_router(student_router)