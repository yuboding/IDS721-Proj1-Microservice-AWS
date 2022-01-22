from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "First AWS project!"}
    
@app.get("/celsius-fahrenheit/{num}")
async def culsiusToFahrenheit(num: int):
    result = num*9/5 + 32
    return {"Fahrenheit": result}

@app.get("/fahrenheit-celsius/{num}")
async def culsiusToFahrenheit(num: int):
    result = (num - 32) * 5 / 9
    return {"Celsius": result}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')