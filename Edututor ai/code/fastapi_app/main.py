from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from utils import get_ibm_response

app = FastAPI()

# Allow requests from Streamlit frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "EduTutor AI backend is running."}

@app.post("/ask/")
async def ask(req: Request):
    try:
        body = await req.json()
        prompt = body.get("prompt")

        if not prompt:
            return {"response": "No prompt provided."}

        # Get the response from IBM Granite model
        result = get_ibm_response(prompt)
        return {"response": result}

    except Exception as e:
        return {"response": f"Error: {str(e)}"}
