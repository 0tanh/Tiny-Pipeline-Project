#Python Standard Library Imports
from functools import _lru_cache_wrapper

#FastAPI imports
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# FastAPI config
from .routes import router
# # import config

# # @_lru_cache_wrapper
# # def get_settings():
# #     return config.Settings

# # get_settings()
  
#Initialising Application
app = FastAPI()
app.include_router(router)
app.add_middleware(CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)