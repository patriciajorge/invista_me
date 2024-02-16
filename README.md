# Gerenciador de Investimentos - invista_me

Este é um simples aplicativo web desenvolvido em Django para gerenciar investimentos. Com ele, você pode visualizar uma lista de investimentos, adicionar novos investimentos, editar investimentos existentes, excluir investimentos e cadastrar novos usuários.

# Funcionalidades

- Funcionalidades Principais
- investimentos/: Lista todos os investimentos cadastrados.
- investimentos/novo_investimento/: Permite adicionar um novo investimento.
- investimentos/<id_investimento>/: Mostra detalhes de um investimento específico.
- investimentos/novo_investimento/<id_investimento>: Permite editar um investimento existente.
- excluir_investimento/<id_investimento>: Permite excluir um investimento.
- conta/: Permite registrar um novo usuário.
- login/: Página de login.
- logout/: Permite fazer logout do usuário.

# Como usar

Para iniciar o servidor de desenvolvimento, execute o seguinte comando:

python manage.py runserver

O servidor estará disponível em http://localhost:8000/.

# Pré-requisitos

- Python 3.6 ou superior
- Django
- SQLite

# Instalação

1. Clone este repositório: git clone https://github.com/patriciajorge/invista_me.git

2. Instale as dependências: pip install -r requirements.txt

3. Execute as migrações do banco de dados: python manage.py migrate

4. Crie um superusuário: python manage.py createsuperuser

5. Inicie o servidor: python manage.py runserver

# Uso

- Acesse o aplicativo em http://localhost:8000/investimentos/
- Para adicionar um novo investimento, faça login e acesse http://localhost:8000/investimentos/novo/
- Para editar ou excluir um investimento, clique nos links correspondentes na lista de investimentos

# Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou abrir issues.

# Licença
Este projeto é licenciado sob a MIT License.