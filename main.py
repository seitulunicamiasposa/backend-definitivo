from fastapi import FastAPI
from handler.autenticazione import router as autenticazione_router
from handler.impianti import router as impianti_router
from handler.macchinari import router as macchinari_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(  

    openapi_url="/documentation/json",

    docs_url="/documentation",

    redoc_url=None

)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(autenticazione_router)
app.include_router(impianti_router)
app.include_router(macchinari_router)