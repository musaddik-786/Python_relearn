# # #Working code 
# # storage_utils.py
# import os
# import aiofiles
# from azure.storage.blob.aio import BlobServiceClient
# from azure.core.exceptions import ResourceNotFoundError
# from service import AZURE_STORAGE_CONNECTION_STRING, _parse_blob_url

# async def download_blob_to_input_folder(blob_url: str, input_folder: str = "input") -> str:
#     """
#     Downloads the blob at blob_url into input_folder (root-level) preserving filename.
#     Returns the local path to the downloaded file.
#     """
#     if not AZURE_STORAGE_CONNECTION_STRING:
#         raise RuntimeError("AZURE_STORAGE_CONNECTION_STRING not set")

#     container, blob_path = _parse_blob_url(blob_url)
#     filename = os.path.basename(blob_path)
#     os.makedirs(input_folder, exist_ok=True)
#     local_path = os.path.join(input_folder, filename)

#     async with BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING) as service:
#         container_client = service.get_container_client(container)
#         blob_client = container_client.get_blob_client(blob_path)
#         try:
#             await blob_client.get_blob_properties()
#         except ResourceNotFoundError:
#             raise FileNotFoundError(f"Blob not found: container={container} blob={blob_path}")
#         stream = await blob_client.download_blob()
#         data = await stream.readall()

#     # write file async
#     async with aiofiles.open(local_path, "wb") as f:
#         await f.write(data)

#     return local_path



# from azure.storage.blob.aio import BlobServiceClient
# from azure.core.exceptions import ResourceNotFoundError
# from service import AZURE_STORAGE_CONNECTION_STRING, _parse_blob_url

# async def download_blob_bytes(blob_url: str):
#    container, blob_path = _parse_blob_url(blob_url)
#    async with BlobServiceClient.from_connection_string(
#        AZURE_STORAGE_CONNECTION_STRING
#    ) as service:
#        container_client = service.get_container_client(container)
#        blob_client = container_client.get_blob_client(blob_path)
#        try:
#            await blob_client.get_blob_properties()
#        except ResourceNotFoundError:
#            raise FileNotFoundError("Blob not found")
#        stream = await blob_client.download_blob()
#        data = await stream.readall()
#    return data


# # from azure.storage.blob.aio import BlobServiceClient
# from urllib.parse import urlparse
# import os
# from service import AZURE_STORAGE_CONNECTION_STRING

# async def upload_text_to_blob(blob_url: str, text: str):
#    parsed = urlparse(blob_url)
#    path = parsed.path.lstrip("/")
#    container, blob_path = path.split("/", 1)
#    filename = os.path.basename(blob_path)
#    base_name = os.path.splitext(filename)[0]
#    new_blob_name = f"{base_name}_extracted_text.txt"
#    blob_service = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
#    container_client = blob_service.get_container_client(container)
#    blob_client = container_client.get_blob_client(new_blob_name)
#    await blob_client.upload_blob(text, overwrite=True)
#    return f"{parsed.scheme}://{parsed.netloc}/{container}/{new_blob_name}"









from azure.storage.blob.aio import BlobServiceClient
from azure.core.exceptions import ResourceNotFoundError
from service import AZURE_STORAGE_CONNECTION_STRING, _parse_blob_url
from urllib.parse import urlparse
import os

TEXT_CONTAINER = "layout-detection-text-of-document"

async def download_blob_bytes(blob_url: str):
   container, blob_path = _parse_blob_url(blob_url)
   async with BlobServiceClient.from_connection_string(
       AZURE_STORAGE_CONNECTION_STRING
   ) as service:
       container_client = service.get_container_client(container)
       blob_client = container_client.get_blob_client(blob_path)
       try:
           await blob_client.get_blob_properties()
       except ResourceNotFoundError:
           raise FileNotFoundError("Blob not found")
       stream = await blob_client.download_blob()
       data = await stream.readall()
   return data

async def upload_text_to_blob(blob_url: str, text: str):
   parsed = urlparse(blob_url)
   path = parsed.path.lstrip("/")
   container, blob_path = path.split("/", 1)
   filename = os.path.basename(blob_path)
   base_name = os.path.splitext(filename)[0]
   new_blob_name = f"{base_name}.txt"
   async with BlobServiceClient.from_connection_string(
       AZURE_STORAGE_CONNECTION_STRING
   ) as blob_service:
       # create container if not exists
       container_client = blob_service.get_container_client(TEXT_CONTAINER)
       try:
           await container_client.create_container()
       except Exception:
           pass   # container already exists
       blob_client = container_client.get_blob_client(new_blob_name)
       await blob_client.upload_blob(text, overwrite=True)
   return f"{parsed.scheme}://{parsed.netloc}/{TEXT_CONTAINER}/{new_blob_name}"