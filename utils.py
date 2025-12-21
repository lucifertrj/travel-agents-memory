import os,pathlib
from cognee import config
from cognee_community_vector_adapter_qdrant import register

async def get_db_config():
    #os.environ["ENABLE_BACKEND_ACCESS_CONTROL"] = "false"
    system_path = pathlib.Path(__file__).parent
    config.system_root_directory(os.path.join(system_path, ".cognee_system"))
    config.data_root_directory(os.path.join(system_path, ".data_storage"))

    config.set_relational_db_config({"db_provider": "sqlite"})
    config.set_vector_db_config({
        "vector_db_provider": "qdrant",
        "vector_db_url": os.getenv("QDRANT_URL", "http://localhost:6333"),
        "vector_db_key": os.getenv("QDRANT_API_KEY", ""),
    })
    config.set_graph_db_config({"graph_database_provider": "kuzu"})