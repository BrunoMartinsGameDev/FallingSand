# Falling Sand Simulator

Este repositório contém um simulador de "areia caindo", implementado em Python com a biblioteca `pygame`. O simulador utiliza três scripts principais (`main.py`, `Mouse.py`, `Screen.py`) para criar uma experiência interativa, onde os blocos caem e se comportam de forma semelhante a partículas de areia.

---

## Requisitos

- **Python 3.8 ou superior**
- **Pygame 2.6.1**

---

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/BrunoMartinsGameDev/fallingsand.git
cd falling-sand-simulator
```
---
### 2. Crie um ambiente virtual (opcional, mas recomendado)

No terminal, execute:

```bash
python -m venv venv
```
Ative o ambiente virtual:

No Windows:
```bash
venv\Scripts\activate
```
No Linux/MacOS:
```bash
source venv/bin/activate
```
---
### 3. Instale as dependências
Utilize o pip para instalar o pygame:

```bash
pip install -r requirements.txt
```
---
## Utilização
### 1. Inicialize o simulador
No terminal, execute o comando:

```bash
python main.py
```
### 2. Controles
Segurar clique esquerdo: Adiciona continuamente blocos de areia.

---
## Estrutura do Repositório
```plaintext
falling-sand-simulator/
│
├── main.py          # Script principal, inicializa o simulador.
├── Mouse.py         # Gerencia os eventos do mouse.
├── Screen.py        # Configura a tela do simulador.
├── requirements.txt # Dependências do projeto.
└── README.md        # Instruções de uso.
```
---
## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests no repositório.

## Licença
Este projeto está licenciado sob a MIT License. Consulte o arquivo LICENSE para mais detalhes.