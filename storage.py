import json

from azure.storage.blob import BlobServiceClient
from azure.storage.blob import BlobClient


class Storage:
    def __init__(self):
        self.conn_str=("DefaultEndpointsProtocol=https;"
                  "AccountName=sto9gm7i6pd7nxahewnfr8y;"
                  "AccountKey=KTJuy6yA28UYyl1m+38nVKrtHGauG2Sir3C5JtOfKwRXvINTQfnylrlKPNanAzyjCYZJDfvK5r7Q+AStA24pyg==;"
                  "EndpointSuffix=core.windows.net")
    def blob_client(self):
        blob_service_client = BlobServiceClient.from_connection_string(self.conn_str)

        container_name = "land"
        container_client = blob_service_client.get_container_client(container=container_name)
        blob_list = container_client.list_blobs(name_starts_with="rickandmorty/inicial/")
        courses = []
        for blob in blob_list:
            blob_name = f"{blob.name}"
            blob_client = container_client.get_blob_client(blob_name)
            partial = blob_client.download_blob().readall()
            treatment_data = json.loads(partial)
            courses.extend(treatment_data['data'])

        return courses

    def upload(self, json_string, blob_name):
            blob_client = BlobClient.from_connection_string(conn_str=self.conn_str,
                                                            container_name="land",
                                                            blob_name=blob_name
                                                            )
            body = json.dumps(json_string, ensure_ascii=False).encode("utf8")
            blob_client.upload_blob(body, overwrite=True)


