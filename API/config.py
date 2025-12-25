from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    db = os.getenv("TEST_DB")
    
    model_config = SettingsConfigDict(env_file="./environmnets/.env")


test_settings = Settings()
live_settings = Settings()