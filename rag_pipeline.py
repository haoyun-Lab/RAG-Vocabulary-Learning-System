from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema import Document
import re
import time

# 配置
CHUNK_SIZE = 15
CHUNK_OVERLAP = 3
TOP_K = 3

class VocabRAG:
    def __init__(self, api_key: str, persist_dir="./chroma_db"):
        self.embedding = OpenAIEmbeddings(openai_api_key=api_key)
        self.vector_db = Chroma(
            persist_directory=persist_dir,
            embedding_function=self.embedding
        )

    def split_text(self, text: str):
        chunks = []
        tokens = text.split()
        start = 0
        while start < len(tokens):
            chunk = tokens[start: start + CHUNK_SIZE]
            chunks.append(" ".join(chunk))
            start += CHUNK_SIZE - CHUNK_OVERLAP
        return chunks

    def add_corpus(self, raw_text: str):
        chunks = self.split_text(raw_text)
        docs = [Document(page_content=c) for c in chunks]
        self.vector_db.add_documents(docs)
        self.vector_db.persist()

    def retrieve(self, query_word: str):
        return self.vector_db.similarity_search(query_word, k=TOP_K)

    def build_prompt(self, word: str, context_docs):
        context = "\n".join([d.page_content for d in context_docs])
        prompt = f"""
You are an English vocabulary assistant.
Reference context: {context}
Target word: {word}
Output:
1. Root and affix parsing
2. One CET exam style long sentence containing this word
Output strictly in JSON format.
"""
        return prompt

    @staticmethod
    def format_check(response: str):
        pattern = r"\{.*\}"
        match = re.search(pattern, response, re.DOTALL)
        return match is not None
