# Uso do Maritaca AI com Chainlit e Literal AI

Este repositório ajudará a criar um chatbot com o uso de Chainlit, Literal AI e Maritaca AI em Python.

## Sobre as Ferramentas

- [Literal AI](https://literalai.com/) é a plataforma de avaliação e observabilidade LLM preferida para desenvolvedores e proprietários de produtos.
- [MariTalk](https://www.maritaca.ai/) é um chatbot baseado em LLM e treinado para atender o Brasil. Maritaca AI é uma empresa brasileira que desenvolve inteligências artificiais especializadas em domínios e idiomas, garantindo que reflitam o conhecimento único de diversas regiões do planeta e segmentos de mercado. 

- [Chainlit](https://chainlit.io/) é um framework Python assíncrono de código aberto que permite aos desenvolvedores criar aplicativos de IA conversacional ou de agente escaláveis.

## Configuração do Ambiente

1. Clone o repositório [https://github.com/marcelobuzzetti/maritalk-chat](https://github.com/marcelobuzzetti/maritalk-chat).

2. Acesse o repositório
```bash
    cd maritalk-chat
```
3. Certifique-se de ter o Python instalado em sua máquina. Você pode verificar a versão do Python digitando o seguinte comando no terminal:

    ```bash
    python --version
    ```

    Se o Python não estiver instalado, faça o download e a instalação a partir do site oficial do Python: [Link do site oficial do Python](https://www.python.org/)

4. Crie um ambiente virtual (venv) para isolar as dependências do projeto. No terminal, execute o seguinte comando:

    ```bash
    python -m venv myenv
    ```

    Isso criará um novo diretório chamado `myenv` que conterá o ambiente virtual.

5. Ative o ambiente virtual. No terminal, execute o seguinte comando:

    - No Windows:

    ```bash
    myenv\Scripts\activate
    ```

    - No macOS/Linux:

    ```bash
    source myenv/bin/activate
    ```

6. Instale as dependências do projeto a partir do arquivo `requirements.txt`. No terminal, execute o seguinte comando:

    ```bash
    pip install -r requirements.txt
    ```

    Isso instalará todas as dependências listadas no arquivo `requirements.txt`.

7. Copie o arquivo [.env-example](.env-example) e cole como `.env`

8. Edita o arquivo `.env`:

**MODEL_MARITACA**=coloque modelo utilizado no Maritalk, ex. `sabia-3`, entre aspas.

Cadastra-se no site [https://chat.maritaca.ai/](https://chat.maritaca.ai/) e gere uma chave da API.

**API_KEY_MARITACA**=coloque a chave de acesso a API do Maritaca entre aspas.

Cadastra-se no site [https://cloud.getliteral.ai/auth/signin](https://cloud.getliteral.ai/auth/signin) e gere uma chave da API. 

**LITERAL_API_KEY**=coloque a chave de acesso a API do LITERAL AI entre aspas.

## Uso

Dentro da pasta `maritalk-chat`, no terminal rode o seguinte comando:

```bash
    chainlit run app.py -w
```
Acesse [http://localhost:8000](http://localhost:8000)

## Como Contribuir

Estamos abertos a contribuições! Se você tem melhorias ou correções, por favor, siga estes passos:

1. Faça um fork do repositório.
2. Crie uma nova branch para sua feature ou correção.
3. Envie um pull request com uma descrição clara de suas mudanças.

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.