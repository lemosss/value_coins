from fastapi import FastAPI, HTTPException
from services.get_coins import GetCoins

app = FastAPI()

@app.get("/")
def heath_check():
    return {"status": "OK"}


@app.get("/items/{coin}")
def get_coin(coin: str):
    if coin == "dollar":
        dollar = GetCoins.get_dollar()
        return {"dollar_value": dollar}
    if coin == "euro":
        euro = GetCoins.get_euro()
        return {"euro_value": euro}
    else:
        raise HTTPException(status_code=400, detail="Invalid Coin")
