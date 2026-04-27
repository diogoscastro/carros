# 🚗 Castro Multimarcas

Sistema web desenvolvido com **Django** para gerenciamento e visualização de veículos, com foco em aprendizado prático de back-end, front-end e deploy em nuvem.

---

## 🚀 Funcionalidades

* 🔍 Busca de veículos por nome
* ➕ Cadastro de novos veículos
* ✏️ Edição de veículos
* ❌ Exclusão de veículos
* 🔐 Autenticação de usuários (login/cadastro)
* 🌗 Modo claro/escuro (Dark Mode)
* 📱 Layout responsivo com Bootstrap

---

## 🛠️ Tecnologias utilizadas

### Back-end

* Python 3.12
* Django
* PostgreSQL

### Front-end

* HTML5
* CSS3
* Bootstrap 5
* Bootstrap Icons

### DevOps / Infra

* AWS EC2 (Ubuntu)
* Nginx
* uWSGI
* Systemd
* Git / GitHub

---

## 📂 Estrutura do projeto

```
carros/
├── app/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── cars/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   └── static/
│
├── static/
├── media/
├── venv/
├── manage.py
└── README.md
```

---

## ⚙️ Como rodar o projeto localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/SEU-USUARIO/carros.git
cd carros
```

---

### 2. Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

---

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 4. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz:

```env
SECRET_KEY=sua_chave
DEBUG=True

DB_NAME=seu_banco
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
```

---

### 5. Aplicar migrações

```bash
python manage.py migrate
```

---

### 6. Criar superusuário

```bash
python manage.py createsuperuser
```

---

### 7. Rodar servidor

```bash
python manage.py runserver
```

---

## 🌐 Deploy (AWS EC2)

O projeto foi deployado utilizando:

* Instância Ubuntu na AWS EC2
* uWSGI para rodar a aplicação Django
* Nginx como proxy reverso
* Systemd para gerenciamento do serviço

### Fluxo de deploy

```bash
git pull
python manage.py migrate
python manage.py collectstatic
sudo systemctl restart carros
```

---

## 🔐 Segurança

* Uso de variáveis de ambiente com `.env`
* Credenciais sensíveis não versionadas
* Configuração de firewall (UFW)
* Acesso remoto via SSH

---

## 📚 Aprendizados

Este projeto foi importante para consolidar conhecimentos em:

* Estrutura MVT do Django
* Integração com PostgreSQL
* Criação de filtros dinâmicos com QuerySets
* Uso de Bootstrap para UI responsiva
* Deploy completo em servidor Linux
* Configuração de Nginx + uWSGI
* Boas práticas de versionamento com Git

---

## 👨‍💻 Autor

Desenvolvido por **Diogo Castro**
