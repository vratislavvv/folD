import requests

def investment_data(api_key):

    url = "https://live.trading212.com/api/v0/equity/account/cash"

    try:
        headers = {"Authorization": api_key}

        # Tu sa vyhodi error
        response = requests.get(url, headers=headers)

        data = response.json()
        
        return data
    
    except requests.exceptions.HTTPError:
        print(f"HTTP error occurred: {err}")
        return None
    
    except ValueError as err:
        print(f"JSON decoding error occurred: {err}")
        return None
