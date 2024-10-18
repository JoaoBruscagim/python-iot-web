# Projeto IoT Device Manager

## Descrição

O **IoT Device Manager** é uma aplicação web desenvolvida em Django que permite o cadastro e gerenciamento de dispositivos IoT e suas respectivas ações. Com uma interface amigável, os usuários podem adicionar, visualizar e editar dispositivos, além de registrar as ações realizadas por cada um deles.

## Tecnologias Utilizadas

### Backend
- **Django**: Framework web para desenvolvimento de aplicações em Python.
- **SQLite**: Banco de dados leve e embutido para armazenamento dos dados dos dispositivos e ações.

### Frontend
- **HTML/CSS**: Estrutura e estilização da interface.
- **Bootstrap**: Framework CSS para estilização e responsividade.

## Funcionalidades

- **Cadastro de Dispositivos**: Adicionar novos dispositivos IoT com informações como nome, tipo e localização.
- **Registro de Ações**: Registrar ações realizadas pelos dispositivos, como ligar, desligar ou alterar configurações.
- **Listagem de Dispositivos**: Visualizar todos os dispositivos cadastrados em uma lista com detalhes.
- **Edição e Exclusão**: Editar informações dos dispositivos e remover dispositivos que não são mais utilizados.

## Como Executar o Projeto

### Pré-requisitos

- Python (versão 3.6 ou superior)
- Django (instalado via pip)

### Configuração do Ambiente

1. Clone o repositório:
   ```bash
   git clone https://github.com/JoaoBruscagim/python-iot-web
   cd python-iob-web
   
2. Crie um ambiente virtual e ative-o:
  python -m venv venv
  source venv/bin/activate  
Para Windows: venv\Scripts\activate

4. Instale as dependências
   pip install requirements.txt

5. Aplique as migrações
   python manage.py migrate

6. Inicie o servidor de desenvolvimento
   python manage.py runserver

7. Acesse a aplicação
  http://127.0.0.1:8000/dispositivos
