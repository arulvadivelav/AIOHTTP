from aiohttp import web
from app.routes import setup_routes
import aiohttp_jinja2
import jinja2


async def create_app():
    app = web.Application()

    # Set up Jinja2 template engine
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))

    # Set up routes
    setup_routes(app)

    return app


if __name__ == '__main__':
    web.run_app(create_app())

print("hello")