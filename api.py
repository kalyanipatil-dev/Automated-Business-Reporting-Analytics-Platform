from fastapi import FastAPI, UploadFile, File
import pandas as pd

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Business Reporting API is running"}

@app.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...)):
    try:
        df = pd.read_csv(file.file)
        return {
            "rows": len(df),
            "columns": list(df.columns),
            "preview": df.head().to_dict()
        }
    except Exception as e:
        return {"error": str(e)}
