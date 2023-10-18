from fastapi import APIRouter, BackgroundTasks
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def root(background_tasks: BackgroundTasks):
    # This will serve the base index.html file from the react app
    # with all associated packaged up react files served in
    # the static folder
    return HTMLResponse(content="", status_code=200)
