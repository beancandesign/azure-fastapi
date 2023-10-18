from fastapi import APIRouter, BackgroundTasks
from fastapi.responses import HTMLResponse

router = APIRouter()

# Login works by the following process:

# - user enters username and password on login screen
# - endpoint communicates with CSP credentials endpoint
# - CSP returns authentication token to client
# - client sends token with all other requests
#   - all other client requests send token in header
#       which then gets checked against CSP endpoint
#       prior to our endpoint getting executed

@router.get("/login", response_class=HTMLResponse)
async def login(background_tasks: BackgroundTasks):
    # This is different to the login screen in the react app!
    # This endpoint actually does the logging in to the CSP
    # authentication server using the user's credentials and
    # returns the JWT token required by the user to access all
    # the other python APIs and the CSP services.
    return HTMLResponse(content="", status_code=200)
