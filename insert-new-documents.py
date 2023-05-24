from gpt_index import GPTListIndex, SimpleDirectoryReader
from llama_index import Document

# Assuming you have an existing index
index = GPTListIndex([])

# Load new documents from the folder
new_documents = SimpleDirectoryReader('<path_to_new_documents>').load_data()

# Create Document objects for the new documents
doc_chunks = []
for i, text in enumerate(new_documents):
    doc = Document(text, doc_id=f"doc_id_{i}")
    doc_chunks.append(doc)

# Insert new Document objects into the existing index
for doc_chunk in doc_chunks:
    index.insert(doc_chunk)