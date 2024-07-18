# Uso do Chainlit e Literal AI com Maritaca em Python

Este repositório é dedicado ao desenvolvimento e exploração da integração entre Chainlit, Literal AI e Maritaca usando Python. O objetivo é criar aplicações que tirem proveito das capacidades únicas de cada uma dessas ferramentas, proporcionando uma experiência rica e interativa para os usuários.

## Sobre as Ferramentas


Este repositório é dedicado ao desenvolvimento e exploração da integração entre Chainlit, Literal AI e Maritaca usando Python. O objetivo é criar aplicações que tirem proveito das capacidades únicas de cada uma dessas ferramentas, proporcionando uma experiência rica e interativa para os usuários.

## Sobre as Ferramentas

- **Literal AI**: [Literal AI](https://literalai.com/) é a plataforma de avaliação e observabilidade LLM preferida para desenvolvedores e proprietários de produtos.
- **Maritaca AI**: [MariTalk](https://www.maritaca.ai/) é um chatbot baseado em LLM e treinado para atender o Brasil.
- **Chainlit**: [Chainlit](https://chainlit.io/) é um framework Python assíncrono de código aberto que permite aos desenvolvedores construir aplicações escaláveis de IA conversacional ou agêntica.

## Configuração do Ambiente

1. Clone o repositório [https://github.com/marcelobuzzetti/maritalk-chat](https://github.com/marcelobuzzetti/maritalk-chat).

2. Acesse o repositório
```bash
    cd maritalk-chat
```
3. Certifique-se de ter o Python instalado em sua máquina. Você pode verificar a versão do Python digitando o seguinte comando no terminal:

    ```
    python --version
    ```

    Se o Python não estiver instalado, faça o download e a instalação a partir do site oficial do Python: [Link do site oficial do Python](https://www.python.org/)

4. Crie um ambiente virtual (venv) para isolar as dependências do projeto. No terminal, execute o seguinte comando:

    ```
    python -m venv myenv
    ```

    Isso criará um novo diretório chamado `myenv` que conterá o ambiente virtual.

5. Ative o ambiente virtual. No terminal, execute o seguinte comando:

    - No Windows:

    ```
    myenv\Scripts\activate
    ```

    - No macOS/Linux:

    ```
    source myenv/bin/activate
    ```

6. Instale as dependências do projeto a partir do arquivo `requirements.txt`. No terminal, execute o seguinte comando:

    ```
    pip install -r requirements.txt
    ```

    Isso instalará todas as dependências listadas no arquivo `requirements.txt`.

7. Copie o arquivo [.env-example](.env-example) e cole como `.env`

8. Edita o arquivo `.env`:

**MODEL_MARITACA**=coloque modelo utilizado no Maritalk, ex. `sabia-3`, entre aspas.

Cadastra-se no site [https://chat.maritaca.ai/](https://chat.maritaca.ai/) e gere uma chave da API.

**API_KEY_MARITACA**=coloque a chave de acesso a API do Maritaca entre aspas.

Cadastra-se no site [https://cloud.getliteral.ai/auth/signin](https://cloud.getliteral.ai/auth/signin) e gere uma chave da API. 

**LITERAL_API_KEY**="chave de acesso a API do LITERAL AI"

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

Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## Contato

Para mais informações, entre em contato com o mantenedor do projeto através de [inserir meio de contato].