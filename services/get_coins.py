import requests
from bs4 import BeautifulSoup
from fastapi import HTTPException


class GetCoins:
    @staticmethod
    def get_dollar():
        try:
            page = requests.get("https://dolarhoje.com")
            if page.status_code == 200:
                parser = BeautifulSoup(page.content, "html.parser")
                dollar_value_str = parser.find(id="nacional").get("value")
                dollar_value_float = float(dollar_value_str.replace(",", "."))
                return {"dollar_value": dollar_value_float}
            else:
                raise HTTPException(status_code=400, detail="Invalid Coin")
        except Exception as e:
            print(e)

    @staticmethod
    def get_euro():
        try:
            page = requests.get(
                "https://www.remessaonline.com.br/cotacao/cotacao-euro",
            )
            if page.status_code == 200:
                parser = BeautifulSoup(page.content, "html.parser")
                euro_value_str = parser.find(
                    "div", {"class": "style__Text-sc-1a6mtr6-2"}
                )
                euro_value_float = float(
                    euro_value_str.text.replace(" Reais", "").replace(",", ".")
                )
                return {"euro_value": euro_value_float}
            else:
                raise HTTPException(status_code=400, detail="Invalid Coin")
        except Exception as e:
            print(e)
