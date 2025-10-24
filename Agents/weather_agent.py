import requests

async def get_wether(city: str) -> str :
    response = await requests.get(f"https://wttr.in/{city.lower()}?format=%C+%t")

    if response.status_code == 200 :
        return response.text
    
    return 'someting goes wrong'