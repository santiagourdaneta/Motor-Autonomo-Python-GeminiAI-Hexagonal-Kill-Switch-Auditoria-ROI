import chromadb
from uuid import uuid4


class VectorDBAdapter:
    def __init__(self):
        # Esto crea una base de datos local en una carpeta, cero costo de RAM
        self.client = chromadb.PersistentClient(path="./chroma_db")
        self.collection = self.client.get_or_create_collection(name="legacy_knowledge")

    def store_knowledge(self, code_content: str, plan_summary: str):
        self.collection.add(
            documents=[code_content],
            metadatas=[{"plan": plan_summary}],
            ids=[str(uuid4())],
        )

    def query_similar_code(self, code_content: str):
        # Busca si ya migramos algo parecido antes
        results = self.collection.query(query_texts=[code_content], n_results=1)
        return results["documents"][0] if results["documents"] else None
