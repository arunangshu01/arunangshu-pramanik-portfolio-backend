import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from routers import health_check, personal_info, profile_summary, skills, education_details, experience, \
    awards_recognitions, send_email
from utility.settings import API_COMMON_PREFIX, HOST, PORT, DEBUG_MODE

tags_metadata = [
    {
        "name": "Health Check",
        "description": "For API Health Check"
    },
    {
        "name": "Personal Information",
        "description": "Extract Personal Information"
    },
    {
        "name": "Profile Summary",
        "description": "Extract Profile Summary"
    },
    {
        "name": "Education Details",
        "description": "Extract Education Details"
    },
    {
        "name": "Skills",
        "description": "Extract Skills"
    },
    {
        "name": "Experience",
        "description": "Extract Experience"
    },
    {
        "name": "Awards & Recognitions",
        "description": "Extract Awards & Recognitions"
    },
    {
        "name": "Drop Me A Message",
        "description": "Send an EMail to me."
    }
]

debug_mode = True if DEBUG_MODE == "True" else False

app = FastAPI(
    openapi_tags=tags_metadata,
    title="Arunangshu Pramanik's Personal Portfolio",
    docs_url=f"{API_COMMON_PREFIX}/docs",
    redoc_url=f"{API_COMMON_PREFIX}/redoc",
    debug=debug_mode
)

app.include_router(health_check.router, prefix=API_COMMON_PREFIX)
app.include_router(personal_info.router, prefix=API_COMMON_PREFIX)
app.include_router(profile_summary.router, prefix=API_COMMON_PREFIX)
app.include_router(education_details.router, prefix=API_COMMON_PREFIX)
app.include_router(skills.router, prefix=API_COMMON_PREFIX)
app.include_router(experience.router, prefix=API_COMMON_PREFIX)
app.include_router(awards_recognitions.router, prefix=API_COMMON_PREFIX)
app.include_router(send_email.router, prefix=API_COMMON_PREFIX)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["*"]
)

if __name__ == '__main__':
    uvicorn.run("app.main:app",
                host=HOST,
                port=PORT,
                access_log=True)
