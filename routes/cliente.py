from flask import Blueprint

cliente_route = Blueprint('cliente', __name__)

'''
Rota de Clientes

/clientes/ (GET) – Listar os clientes
/clientes/ (POST) – inserir o cliente no servidor
/clientes/new (GET) – renderizar o formulário para criar um cliente
/clientes/<id> (GET) – obter os dados de um cliente
/clientes/<id>/edit (GET) – renderizar um formulário para editar um cliente
/clientes/<id>/update (PUT) – atualizar os dados do cliente
/clientes/<id>/delete (DELETE) – deleta o registro do usuário
'''

@cliente_route.route('/')
def lista_clientes():
    pass

@cliente_route.route('/', methods= ['POST'])
def inserir_cliente():
    pass

@cliente_route.route('/new')
def form_cliente():
    pass

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    pass

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    pass

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    pass

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    pass
