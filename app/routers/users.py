from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import Request, status, Form
from app.dependencies import SessionDep
from . import api_router
from app.services.user_service import UserService
from app.repositories.user import UserRepository
from app.utilities.flash import flash
from app.schemas import UserResponse


# API endpoint for listing users
@api_router.get("/todos")
async def list_todos(request: Request, db: SessionDep):
    user_repo = UserRepository(db)
    username = request.session.get("user", {}).get("username") if isinstance(request.session.get("user"), dict) else None
    if not username:
        username = request.session.get("username")
    user_id = 1
    if username:
        user = user_repo.get_by_username(username)
        if user:
            user_id = user.id