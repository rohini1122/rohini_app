from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    TOPIC_TENANTMANAGEMENT_SERVICE: str = "queryTopic"
    KAFKA_BOOTSTRAP_SERVER: str = "kafka:9092"
    