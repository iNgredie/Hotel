import uvicorn

from hotel.settings import settings

if __name__ == '__main__':
    uvicorn.run(
        'hotel.app:app',
        host=settings.server_host,
        port=settings.server_port,
        reload=True
    )
