#Working code
# import os
# import json
# from typing import Dict, Any
# from service import _require_env
# from storage_utils import download_blob_to_input_folder
# from document_loader import load_document
# from classifier import classify_document

# INPUT_FOLDER = "input"
# OUTPUT_FOLDER = "output"

# async def classify_blob_pdf_layout(blob_url: str) -> Dict[str, Any]:
#     """
#     - Download PDF into input/
#     - Use Form Recognizer to analyze layout
#     - Classify layout using extracted content
#     - Return minimal verdict
#     """



#     try:
#         _require_env()
#     except Exception as e:
#         return {"status": False, "error": f"Environment misconfigured: {e}"}

#     # 1) Download PDF
#     try:
#         local_pdf = await download_blob_to_input_folder(blob_url, input_folder=INPUT_FOLDER)
#     except Exception as e:
#         return {"status": False, "error": f"Failed to download blob: {e}"}

#     # 2) Use Form Recognizer to analyze the document
#     try:
#         document_content = load_document(local_pdf)
#     except Exception as e:
#         return {"status": False, "error": f"Form Recognizer failed: {e}"}

#     # 3) Classify layout using extracted content
#     try:
#         layout_type = classify_document(document_content)
#     except Exception as e:
#         return {"status": False, "error": f"Classification failed: {e}"}
    
#     result = {"status": True, "layout_type": layout_type, "details": document_content}
#     # result = {"status": True, "layout_type": layout_type, "URL" : blob_url}

#     # 4) Save minimal output to ./output
#     try:
#         os.makedirs(OUTPUT_FOLDER, exist_ok=True)
#         out_path = os.path.join(OUTPUT_FOLDER, "layout_classification_result.json")
#         with open(out_path, "w", encoding="utf-8") as f:
#             json.dump(result, f, indent=2, ensure_ascii=False)
#     except Exception as e:
#         result["save_error"] = str(e)

#     return result





from typing import Dict, Any
from storage_utils import download_blob_bytes
from document_loader import load_document_from_bytes
from classifier import classify_document
from storage_utils import download_blob_bytes, upload_text_to_blob


async def classify_blob_pdf_layout(blob_url: str) -> Dict[str, Any]:
   try:
       blob_bytes = await download_blob_bytes(blob_url)
   except Exception as e:
       return {"status": False, "error": f"Failed to fetch blob: {e}"}
#    try:
#        document_content = await load_document_from_bytes(blob_url, blob_bytes)
#    except Exception as e:
#        return {"status": False, "error": f"Document parsing failed: {e}"}
   
#        extracted_text = document_content.get("text", "")
#    try:
#        text_blob_url = await upload_text_to_blob(blob_url, extracted_text)
#    except Exception as e:
#        return {"status": False, "error": f"Failed to upload extracted text: {e}"}


   try:
     document_content = await load_document_from_bytes(blob_url, blob_bytes)
   except Exception as e:
       return {"status": False, "error": f"Document parsing failed: {e}"}
   extracted_text = document_content.get("text", "")
   try:
       text_blob_url = await upload_text_to_blob(blob_url, extracted_text)
   except Exception as e:
       return {"status": False, "error": f"Failed to upload extracted text: {e}"}

   try:
       layout_type = classify_document(document_content)
   except Exception as e:
       return {"status": False, "error": f"Classification failed: {e}"}
   return {
       "status": True,
       "layout_type": layout_type,
       "URL": blob_url,
    #    "details": document_content,
       "text_blob_url": text_blob_url
   }









# from typing import Dict, Any
# from storage_utils import download_blob_bytes
# from document_loader import load_document_from_bytes
# from classifier import classify_document
# async def classify_blob_pdf_layout(blob_url: str, model_id: str = "prebuilt-read") -> Dict[str, Any]:
#    try:
#        blob_bytes = await download_blob_bytes(blob_url)
#    except Exception as e:
#        return {"status": False, "error": f"Failed to fetch blob: {e}"}
#    try:
#        # ✅ Pass model_id so you can switch between prebuilt-read / prebuilt-layout
#        document_content = await load_document_from_bytes(blob_url, file_bytes=blob_bytes, model_id=model_id)
#    except Exception as e:
#        return {"status": False, "error": f"Document parsing failed: {e}"}
#    # ✅ Guard: warn if text is still empty after extraction
#    if not document_content.get("text", "").strip():
#        return {
#            "status": False,
#            "error": "Text extraction returned empty. Check file format or Azure API version.",
#            "URL": blob_url
#        }
#    try:
#        layout_type = classify_document(document_content)
#    except Exception as e:
#        return {"status": False, "error": f"Classification failed: {e}"}
#    return {
#        "status": True,
#        "layout_type": layout_type,
#        "URL": blob_url,
#        "details": document_content
#    }
