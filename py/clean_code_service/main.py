import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config import AppConfig
from src.api import router as api_router


app = FastAPI(
    title='Check Service',
    description='API',
    version='0.0.1',
    terms_of_service='http://example.com/terms/',
    contact={
        'name': 'Shabalinov Stepan',
        'email': 'shabalinov@example.com',
    },
    license_info={
        'name': 'Apache 2.0',
        'url': 'https://www.apache.org/licenses/LICENSE-2.0.html',
    },
    )

origins = ["http://localhost:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


if __name__ == "__main__":

    config = AppConfig()
    uvicorn.run("main:app", host=config.host, port=config.port, reload=config.reload_after_change)
