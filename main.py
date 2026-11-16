from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health():
  return {"status" : "Okay"}

@app.get("/complaints")
def get_complaints():
  return {"message" : "List of all complaints"}

@app.get("/departments")
def get_departments():
  return {"message" : "List of all departments"}
