import argparse
from engine.processor import DocumentProcessor
from engine.summarizer import Summarizer


def main():
    parser = argparse.ArgumentParser(
        description="Pipeline de Sumarização com LangChain + Cohere"
    )

    parser.add_argument("--text", type=str, help="Texto direto")
    parser.add_argument("--file", type=str, help="Arquivo .txt ou .pdf")

    parser.add_argument(
        "--mode",
        choices=["short", "detailed", "bullet", "executive"],
        default="short"
    )

    args = parser.parse_args()

    processor = DocumentProcessor()
    summarizer = Summarizer()

    # INPUT
    if args.text:
        docs = processor.load_text(args.text)

    elif args.file:
        if args.file.endswith(".txt"):
            docs = processor.load_txt_file(args.file)

        elif args.file.endswith(".pdf"):
            docs = processor.load_pdf(args.file)

        else:
            raise ValueError("Formato não suportado")

    else:
        raise ValueError("Use --text ou --file")

    # CHUNK
    split_docs = processor.split_documents(docs)

    # SUMMARIZE
    result = summarizer.summarize(split_docs, mode=args.mode)

    print("\n===== RESUMO =====\n")
    print(result)


if __name__ == "__main__":
    main()