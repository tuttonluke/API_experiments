# %%
from fastapi import FastAPI

app = FastAPI()

# Path operation function
@app.get("/")
def root():
    return {"message": "Welcome to my API"}

@app.get("/posts")
def get_posts():
    return {"data" : "These are your posts."}