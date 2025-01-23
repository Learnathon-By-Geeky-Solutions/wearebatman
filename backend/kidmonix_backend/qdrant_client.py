import qdrant_client
from qdrant_client import QdrantClient
from .settings import QDRANT_HOST, QDRANT_API_KEY

qdrantClient = qdrant_client.QdrantClient(QDRANT_HOST, api_key = QDRANT_API_KEY, timeout=60.0)