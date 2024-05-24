import asyncio
from fastapi import FastAPI, HTTPException
import aiohttp
from datetime import datetime, timedelta, timezone

app = FastAPI()

API_KEY = 'cp3md19r01qs3665mih0cp3md19r01qs3665mihg'
BASE_URL = 'https://finnhub.io/api/v1'
STOCK_SYMBOL = 'ACB'  # Biểu tượng cổ phiếu bạn muốn theo dõi

# Define UTC and VN timezones
UTC_timezone = timezone.utc
VN_timezone = timezone(timedelta(hours=7))  # UTC+7

# Biến toàn cục để lưu trữ dữ liệu cổ phiếu
stock_data_cache = {}

async def fetch_stock_data(symbol):
    params = {
        "symbol": symbol,
        "token": API_KEY
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{BASE_URL}/quote", params=params) as response:
            data = await response.json()
            print("API response data:", data)  # In ra kết quả API call
            if 'c' not in data:
                raise HTTPException(status_code=404, detail="Stock symbol not found")
            # Extract relevant information
            stock_data = {
                "symbol": symbol,
                "price": data["c"],
                "change": data["d"],
                "last_refreshed": datetime.utcfromtimestamp(data["t"]).strftime('%Y-%m-%d %H:%M:%S')
            }
            return stock_data

async def update_stock_data():
    while True:
        try:
            global stock_data_cache
            stock_data_cache[STOCK_SYMBOL] = await fetch_stock_data(STOCK_SYMBOL)
            print("Updated stock data cache:", stock_data_cache)
        except Exception as e:
            print(f"Error updating stock data: {e}")
        await asyncio.sleep(30)

@app.on_event("startup")
async def startup_event():
    # Khởi động nhiệm vụ cập nhật dữ liệu cổ phiếu
    asyncio.create_task(update_stock_data())

@app.get("/stock/{symbol}")
async def get_stock_info(symbol: str):
    try:
        if symbol not in stock_data_cache:
            raise HTTPException(status_code=404, detail="Stock symbol not found in cache")
        stock_data = stock_data_cache[symbol]
        # Convert last refreshed time from UTC to VN timezone
        last_refreshed_utc = datetime.strptime(stock_data["last_refreshed"], "%Y-%m-%d %H:%M:%S")
        last_refreshed_vn = last_refreshed_utc.replace(tzinfo=UTC_timezone).astimezone(VN_timezone)
        stock_data["last_refreshed"] = last_refreshed_vn.strftime("%Y-%m-%d %H:%M:%S %Z%z")
        return stock_data
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
