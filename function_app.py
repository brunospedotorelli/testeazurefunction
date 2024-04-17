from storage import Storage
import azure.functions as func
from requests import get, post
import logging

storage= Storage()

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)
@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    get_certificate(storage.blob_client(), get_token())
    return func.HttpResponse(
            'Success to get Analytics!',
            status_code=200
    )

def get_characters():
    url = f"https://rickandmortyapi.com/api"
    headers = {
        "Content-Type": "application/json"
    }
    response = get(url = url, headers = headers)
    characters = response.json()

    logging.info(f"API2Land Endpoint certificate. characters: testeconectividade")

    # Write response API2Land
    blob_name = f"rickandmorty/characters/17042024.json"
    storage.upload(characters, blob_name)