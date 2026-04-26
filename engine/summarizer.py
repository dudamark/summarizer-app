from dotenv import load_dotenv
from langchain_cohere import ChatCohere
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


class Summarizer:

    def __init__(self):
        self.parser = StrOutputParser()
        self.llm = self._init_llm()

    def _init_llm(self):
        # lista de modelos válidos (tentativa automática para mitigar o problema de modelo inválido)
        models = [
            "command-light",   # mais seguro
            "command-nightly"  # fallback
        ]

        for model in models:
            try:
                llm = ChatCohere(
                    model=model,
                    temperature=0.2
                )
                # teste rápido
                llm.invoke("Teste")
                print(f"[OK] Usando modelo: {model}")
                return llm
            except Exception:
                continue

        raise Exception("Nenhum modelo da Cohere disponível na sua conta.")

    def _get_prompts(self, mode):

        if mode == "short":
            map_prompt = "Resuma de forma curta:\n\n{input}"
            reduce_prompt = "Consolide em resumo curto:\n\n{input}"

        elif mode == "detailed":
            map_prompt = "Resuma com detalhes:\n\n{input}"
            reduce_prompt = "Una mantendo detalhes:\n\n{input}"

        elif mode == "bullet":
            map_prompt = "Liste pontos principais:\n\n{input}"
            reduce_prompt = "Organize os pontos:\n\n{input}"

        elif mode == "executive":
            map_prompt = "Resumo executivo focado em decisão:\n\n{input}"
            reduce_prompt = "Resumo executivo final:\n\n{input}"

        else:
            raise ValueError("Modo inválido")

        return map_prompt, reduce_prompt

    def summarize(self, docs, mode="short"):

        map_prompt, reduce_prompt = self._get_prompts(mode)

        map_chain = ChatPromptTemplate.from_template(map_prompt) | self.llm | self.parser
        reduce_chain = ChatPromptTemplate.from_template(reduce_prompt) | self.llm | self.parser

        partials = []

        for doc in docs:
            content = doc["page_content"] if isinstance(doc, dict) else doc.page_content
            partials.append(map_chain.invoke({"input": content}))

        combined = "\n\n".join(partials)

        final = reduce_chain.invoke({"input": combined})

        return final