import uvicorn
from .settings import settings


uvicorn.run(
    'workshop.app:app',
    port=settings.sever_port,
    host=settings.server_host,
    reload=True
)