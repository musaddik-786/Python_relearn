# from fastapi import APIRouter
# from fastapi.responses import JSONResponse
# from pydantic import BaseModel, Field
# from handler import classify_blob_pdf_layout

# router = APIRouter()

# class LayoutDetectRequest(BaseModel):
#     """
#     Payload:
#     {
#       "attachment_url": "https://<account>.blob.core.windows.net/<container>/<path>/file.pdf"
#     }
#     """
#     attachment_url: str = Field(..., description="Full Azure Blob URL to the PDF attachment.")

# @router.post("/layout_detection_mcp", operation_id="layout_detection_mcp",
#              summary="Download PDF from blob, analyze layout using Form Recognizer, and classify layout")
# async def detect_layout(request: LayoutDetectRequest):
#     try:
#         result = await classify_blob_pdf_layout(request.attachment_url)
#         return JSONResponse(content={"jsonrpc": "2.0", "id": 1, "result": result}, status_code=200)
#     except Exception as e:
#         return JSONResponse(content={"jsonrpc": "2.0", "id": 1,
#                                      "result": {"status": False, "error": str(e)}}, status_code=200)




from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from handler import classify_blob_pdf_layout

router = APIRouter()

class LayoutDetectRequest(BaseModel):
    attachment_url: str = Field(..., description="Full Azure Blob URL to the PDF attachment.")

@router.post("/layout_detection_mcp", operation_id="layout_detection_mcp",
             summary="Download PDF from blob, analyze layout using Form Recognizer, and classify layout")
async def detect_layout(request: LayoutDetectRequest):
    """Analyze the document to classify if the document is ACORD/SOV/LOSS_RUN/INSPECTION_REPORT/Property_Detailed_Report/Submission_Document

    
    Args:
        attachment_url: The Blob URL oreturned by the email_attachment_mcp
    
    Returns:
        JSONResponse: returns the json response containing the classification of the layout.
    """
    try:
        result = await classify_blob_pdf_layout(request.attachment_url)
        return JSONResponse(content={"jsonrpc": "2.0", "id": 1, "result": result}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"jsonrpc": "2.0", "id": 1,
                                     "result": {"status": False, "error": str(e)}}, status_code=200)



