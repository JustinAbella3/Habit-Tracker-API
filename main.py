from fastapi import FastAPI
import asyncio
from api import users as user_routes
from database.db_setup import async_engine
from database.models import users as users_models
from api import habits as habit_routes
from database.models import habits as habits_models
from core.config import settings

app = FastAPI(
    title="ToDo List API",
    description="A simple ToDo list API",
    version="1.0",
    contact={"name": "John Doe", "email": "qwe@gmail.com"},
    license_info={"name": "MIT"},
    debug=settings.DEBUG
)

async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(users_models.Base.metadata.create_all)
        await conn.run_sync(habits_models.Base.metadata.create_all)

@app.on_event("startup")
async def on_startup():
    await init_db()

app.include_router(user_routes.router)
app.include_router(habit_routes.router)



# from fastapi import FastAPI

# import asyncio
# from api import users as user_routes
# from database.db_setup import async_engine
# from database.models import users as users_models

# users_models.Base.metadata.create_all(bind=async_engine)
# #course.Base.metadata.create_all(bind=engine)

# app = FastAPI(
#     title="ToDo List API",
#     description="A simple ToDo list API",
#     version="1.0",
#     contact={"name": "John Doe", "email": "qwe@gmail.com" },
#     license_info={"name": "MIT"}
# )

# app.include_router(user_routes.router)
# #app.include_router(sections.router)
# #app.include_router(courses.router)

