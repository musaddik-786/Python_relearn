
# #Working code 

# # main.py
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
# from file_router import router as file_router

# def apply_cors(app: FastAPI):
#     app.add_middleware(
#         CORSMiddleware,
#         allow_origins=["*"],
#         allow_methods=["*"],
#         allow_headers=["*"],
#     )

# app = FastAPI(title="Layout Detection MCP API", version="0.1.0")
# apply_cors(app)
# app.include_router(file_router, prefix="/api/v1/layout")

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8602, reload=False)


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from file_router import router as file_router

def apply_cors(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

app = FastAPI(title="Layout Detection MCP API", version="0.1.0")
apply_cors(app)
app.include_router(file_router, prefix="/api/v1/layout")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8667, reload=False)
