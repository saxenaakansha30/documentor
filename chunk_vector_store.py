from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.utils import filter_complex_metadata
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import chroma;
from langchain_community.embeddings import fastembed;

class ChunkVectorStore:

  def __init__(self) -> None:
    pass

  def split_into_chunks(self, file_path: str):
    doc = PyPDFLoader(file_path).load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=20)
    chunks = text_splitter.split_documents(doc)
    chunks = filter_complex_metadata(chunks)

    return chunks

  def store_to_vector_database(self, chunks):
    return chroma.Chroma.from_documents(documents=chunks, embedding=fastembed.FastEmbedEmbeddings())

