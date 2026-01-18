# Email AI Classifier

Aplicação web que utiliza Inteligência Artificial para classificar emails automaticamente como Produtivos ou Improdutivos e sugerir respostas automáticas, reduzindo o trabalho manual de equipes que lidam com alto volume de emails.

Este projeto foi desenvolvido como **desafio técnico**, com foco em clareza, organização de código, uso consciente de IA e deploy em nuvem.

---

## Funcionalidades

*  Classificação automática de emails em:

  * **Produtivo**: requer ação, suporte ou resposta
  * **Improdutivo**: mensagens sociais ou informativas
* Geração de resposta automática usando IA (Hugging Face)
* Suporte a:

  * Texto colado diretamente
  * Upload de arquivos `.txt` e `.pdf`
* Interface web simples e intuitiva
* Aplicação hospedada na nuvem

---

## Arquitetura da Solução

A aplicação segue uma arquitetura simples e eficiente:

1. **Frontend (HTML, CSS, JavaScript)**

   * Interface para inserção de texto ou upload de arquivos
   * Comunicação assíncrona com a API

2. **Backend (FastAPI – Python)**

   * Leitura e extração de texto (TXT/PDF)
   * Classificação do email
   * Geração de resposta automática

3. **Inteligência Artificial**

   * **Classificação**: abordagem heurística com técnicas básicas de NLP (keywords)
   * **Geração de resposta**: Hugging Face Inference API (modelo generativo)

> A abordagem híbrida foi escolhida para garantir **confiabilidade na classificação** e **uso eficiente da IA**, aplicando modelos generativos onde eles agregam mais valor.

---

## Tecnologias Utilizadas

* **Python 3.11**
* **FastAPI** – backend e API REST
* **Hugging Face Inference API** – geração de respostas automáticas
* **HTML5, CSS3 e JavaScript** – interface web
* **PyPDF2** – leitura de arquivos PDF
* **Jinja2** – renderização de templates HTML
* **Render** – hospedagem em nuvem

---

## Estrutura do Projeto

```
email-ai-classifier/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI (rotas e configuração)
│   └── ai_service.py    # Classificação e IA
│
├── static/
│   ├── style.css        # Estilos da interface
│   └── script.js        # Lógica do frontend
│
├── templates/
│   └── index.html       # Interface web
│
├── requirements.txt
├── start.sh
├── .gitignore
└── README.md
```

---

## Executando o Projeto Localmente

### Clonar o repositório

git clone https://github.com/joboueke/email-ai-classifier.git
cd email-ai-classifier

### Instalar dependências

pip install -r requirements.txt

### Configurar variável de ambiente

Crie um arquivo `.env` na raiz do projeto:
HF_API_TOKEN=hf_seu_token_aqui

>  O token da Hugging Face **não deve ser versionado**.

### Executar a aplicação

uvicorn app.main:app --reload

Acesse:

* Interface web: [http://127.0.0.1:8000/ui](http://127.0.0.1:8000/ui)
* Documentação da API: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Deploy em Nuvem

A aplicação está hospedada no **Render**, com:

* Build automático via `requirements.txt`
* Variáveis de ambiente configuradas diretamente na plataforma
**Link da aplicação:** *(inserir URL do Render aqui)*

## Exemplos de Uso

### Email Produtivo
```
Olá, poderia me informar o status do meu chamado em aberto?
```
 Classificação: **Produtivo**

### Email Improdutivo
```
Feliz natal! Desejo boas festas a todos.
```
Classificação: **Improdutivo**

---

## Vídeo Demonstrativo

📺 Vídeo de apresentação (3–5 minutos): *(inserir link do YouTube aqui)*

O vídeo demonstra:

* Funcionamento da interface
* Classificação de emails
* Geração de respostas automáticas
* Explicação técnica da solução

---

## 👨‍💻 Autor

**João Hollanda Boueke**
Estudante de Análise e Desenvolvimento de Sistemas
Projeto desenvolvido como desafio técnico com foco em backend, IA e arquitetura de software.

---

## Conclusão

Este projeto demonstra a aplicação prática de **APIs REST**, **Processamento de Linguagem Natural** e **Inteligência Artificial**, com foco em clareza, organização e resolução de problemas reais.

Obrigado pela oportunidade de apresentar esta solução.
