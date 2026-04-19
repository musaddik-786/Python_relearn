# from dotenv import load_dotenv
# import os
# from azure.ai.formrecognizer import DocumentAnalysisClient
# from azure.core.credentials import AzureKeyCredential

# # Load environment variables from .env file
# load_dotenv()

# # Fetch variables
# endpoint = os.getenv("AZURE_FORMRECOG_ENDPOINT")
# key = os.getenv("AZURE_FORMRECOG_KEY")
# # Fail fast if missing
# if not endpoint:
#     raise ValueError("❌ AZURE_FORMRECOG_ENDPOINT is not set. Check your .env file.")
# if not key:
#     raise ValueError("❌ AZURE_FORMRECOG_KEY is not set. Check your .env file.")

# # Create the client using the key and endpoint
# client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# def load_document(file_path):
#     """
#     Extracts text and layout information using Form Recognizer's prebuilt-layout model.
#     """
#     with open(file_path, "rb") as f:
#         poller = client.begin_analyze_document("prebuilt-layout", document=f)
#         result = poller.result()

#     # Extract lines of text
#     lines = [line.content for page in result.pages for line in page.lines]

#     # Extract table information
#     tables = []
#     for page in result.pages:
#         for table in page.tables:
#             table_data = []
#             for row in table.cells:
#                 table_data.append(row.content)
#             tables.append(table_data)

#     # Combine text and table information
#     document_content = {
#         "text": "n".join(lines),
#         "tables": tables
#     }
#     return document_content





#Working Code

# from dotenv import load_dotenv
# import os
# from azure.ai.formrecognizer import DocumentAnalysisClient
# from azure.core.credentials import AzureKeyCredential

# # Load environment variables from .env file
# load_dotenv()

# # Fetch variables
# endpoint = os.getenv("LD_AZURE_FORMRECOG_ENDPOINT")
# key = os.getenv("LD_AZURE_FORMRECOG_KEY")
# # Fail fast if missing
# if not endpoint:
#     raise ValueError(" LD_AZURE_FORMRECOG_ENDPOINT is not set. Check your .env file.")
# if not key:
#     raise ValueError(" LD_AZURE_FORMRECOG_KEY is not set. Check your .env file.")

# # Create the client using the key and endpoint
# client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# def load_document(file_path):
#     """
#     Extracts text and layout information using Form Recognizer's prebuilt-layout model.
#     """
#     with open(file_path, "rb") as f:
#         poller = client.begin_analyze_document("prebuilt-layout", document=f)
#         result = poller.result()

#     # Debugging: Print available attributes in DocumentPage
#     # print("Available attributes in DocumentPage:")
#     # print(dir(result.pages[0]))
#     # print("/n")
#     # print("/n")

#     # Extract lines of text
#     lines = [line.content for page in result.pages for line in page.lines]

#     # Extract table information if available
#     tables = []
#     for page in result.pages:
#         if hasattr(page, "tables"):  # Check if 'tables' attribute exists
#             for table in page.tables:
#                 table_data = []
#                 for row in table.cells:
#                     table_data.append(row.content)
#                 tables.append(table_data)

#     # Combine text and table information
#     document_content = {
#         "text": "n".join(lines),
#         "tables": tables if tables else "No tables detected"
#     }
#     return document_content

import io
import mammoth
from weasyprint import HTML
from dotenv import load_dotenv
import os
import tempfile
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
load_dotenv()
endpoint = os.getenv("LD_AZURE_FORMRECOG_ENDPOINT")
key = os.getenv("LD_AZURE_FORMRECOG_KEY")
client = DocumentAnalysisClient(
   endpoint=endpoint,
   credential=AzureKeyCredential(key)
)

def convert_docx_bytes_to_pdf_bytes(docx_bytes: bytes):
   docx_stream = io.BytesIO(docx_bytes)
   html = mammoth.convert_to_html(docx_stream).value
   pdf_bytes = HTML(string=html).write_pdf()
   # print("This are the pdf bytes : ", pdf_bytes)
   return pdf_bytes

async def load_document_from_bytes(blob_url: str, file_bytes: bytes):
   extension = blob_url.split(".")[-1].lower()
   if extension == "docx":
       file_bytes = convert_docx_bytes_to_pdf_bytes(file_bytes)
   elif extension != "pdf":
       raise ValueError(f"Unsupported file type: {extension}")
   poller = client.begin_analyze_document(
       "prebuilt-read",
       document=file_bytes
   )
   result = poller.result()
   lines = [line.content for page in result.pages for line in page.lines]
#    tables = []
#    for table in result.tables:
#        row = []
#        for cell in table.cells:
#            row.append(cell.content)
#        tables.append(row)
   return {
       "text": "\n".join(lines),
    #    "tables": tables
   }















# import io
# import os
# from azure.core.credentials import AzureKeyCredential
# from azure.ai.documentintelligence import DocumentIntelligenceClient
# from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
# ENDPOINT = os.getenv("LD_AZURE_FORMRECOG_ENDPOINT")
# API_KEY = os.getenv("LD_AZURE_FORMRECOG_KEY")
# client = DocumentIntelligenceClient(
#    endpoint=ENDPOINT,
#    credential=AzureKeyCredential(API_KEY)
# )
# async def load_document_from_bytes(blob_url: str, file_bytes: bytes, model_id: str = "prebuilt-read"):
#    """
#    Supports DOCX, PDF, images via Azure Document Intelligence.
#    model_id: 'prebuilt-read' or 'prebuilt-layout'
#    """
#    poller = client.begin_analyze_document(
#        model_id,
#        body=io.BytesIO(file_bytes),       # ✅ wrap in BytesIO stream
#        content_type="application/octet-stream"        # ✅ required for DOCX
#    )
#    result = poller.result()
#    # --- Text extraction (both models) ---
#    lines = []
#    if result.pages:
#        for page in result.pages:
#            if page.lines:
#                for line in page.lines:
#                    lines.append(line.content)
#    # --- Fallback: use result.content (markdown) if pages are empty ---
#    # This often happens with DOCX — layout model returns content directly
#    full_text = "\n".join(lines) if lines else (result.content or "")
#    # --- Tables (prebuilt-layout only) ---
#    tables = []
#    if result.tables:
#        for i, table in enumerate(result.tables):
#            rows = {}
#            for cell in table.cells:
#                rows.setdefault(cell.row_index, {})[cell.column_index] = cell.content
#            tables.append({
#                "table_index": i,
#                "row_count": table.row_count,
#                "col_count": table.column_count,
#                "rows": rows
#            })
#    # --- Paragraphs with roles (prebuilt-layout only) ---
#    paragraphs = []
#    if result.paragraphs:
#        for para in result.paragraphs:
#            paragraphs.append({
#                "role": para.role or "body",
#                "content": para.content
#            })
#    return {
#        "text": full_text,
#        "tables": tables,
#        "paragraphs": paragraphs
#    }












# doc_client = DocumentAnalysisClient(
#     endpoint=os.getenv("DOCUMENTINTELLIGENCE_ENDPOINT"),
#     credential=AzureKeyCredential(os.getenv("DOCUMENTINTELLIGENCE_API_KEY"))
# )

# async def load_document_from_bytes(blob_url: str, docx_bytes: bytes):
#     """Extract text from DOCX using Azure Document Intelligence."""
#     with tempfile.NamedTemporaryFile(suffix=".docx", delete=False) as temp_docx:
#         temp_docx.write(docx_bytes)
#         temp_docx.flush()

#         try:
#             with open(temp_docx.name, "rb") as docx_file:
#                 poller = doc_client.begin_analyze_document(
#                     model_id="prebuilt-read",
#                     document=docx_file,
#                   #   content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
#                 )
#                 result = poller.result()

#                 # Extract text from all pages
#                 text = "\n".join([
#                     line.content
#                     for page in result.pages
#                     for line in page.lines
#                 ])
#                 return text
#         finally:
#             os.unlink(temp_docx.name)


# async def load_document_from_bytes(blob_url: str, docx_bytes: bytes):
#     """Extract text from DOCX using Azure Document Intelligence."""
#     with tempfile.NamedTemporaryFile(suffix=".docx", delete=False) as temp_docx:
#         temp_docx.write(docx_bytes)
#         temp_docx.flush()

#         try:
#             with open(temp_docx.name, "rb") as docx_file:
#                 poller = doc_client.begin_analyze_document(
#                     model_id="prebuilt-read",
#                     document=docx_file,
#                   #   content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
#                 )
#                 result = poller.result()

#                 # Extract text from all pages
#                 lines = [
#                     line.content
#                     for page in result.pages
#                     for line in page.lines
#                 ]
#                 return {
#                     "text": "\n".join(lines)
#                 }
#         finally:
#             os.unlink(temp_docx.name)