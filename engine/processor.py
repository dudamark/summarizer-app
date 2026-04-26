from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader, PyPDFLoader


class DocumentProcessor:

    def load_text(self, text: str):
        return [{"page_content": text}]

    def load_txt_file(self, path: str):
        loader = TextLoader(path, encoding="utf-8")
        return loader.load()

    def load_pdf(self, path: str):
        loader = PyPDFLoader(path)
        return loader.load()

    def split_documents(self, documents):
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        # suporta tanto dict quanto Document
        if isinstance(documents[0], dict):
            texts = [doc["page_content"] for doc in documents]
            return [{"page_content": t} for t in splitter.split_text("\n".join(texts))]

        return splitter.split_documents(documents)