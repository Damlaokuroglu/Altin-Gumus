import requests

API_KEY = "API_KEYIN"
BASE_URL = "https://metals-api.com/api/"

def get_price(metal, year):
    url = f"{BASE_URL}historical?access_key={API_KEY}&date={year}-01-01&base=USD&symbols={metal}"
    response = requests.get(url)
    data = response.json()
    
    if "rates" not in data:
        print(f"Hata: {data.get('error', {}).get('message', 'Bilinmeyen bir hata oluştu')}")
        return None
    return data["rates"][metal]  

def calculate_profit(start, end):
    if start is None or end is None:
        return None
    return ((end - start) / start) * 100  

def metal_analysis(year):
    gold_start = get_price("XAU", year)
    gold_end = get_price("XAU", str(int(year) + 1))  

    silver_start = get_price("XAG", year)
    silver_end = get_price("XAG", str(int(year) + 1))

    if None not in [gold_start, gold_end, silver_start, silver_end]:
        gold_profit = calculate_profit(gold_start, gold_end)
        silver_profit = calculate_profit(silver_start, silver_end)

        print(f"{year} yılında altın %{gold_profit:.2f} kazandırdı")
        print(f"{year} yılında gümüş %{silver_profit:.2f} kazandırdı")

        if gold_profit > silver_profit:
            print("Altın daha fazla kazandırdı")
        else:
            print("Gümüş daha fazla kazandırdı")
    else:
        print("Fiyat verileri alınamadı.")

year = input("Yıl girin: ")
metal_analysis(year)