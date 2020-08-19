import imports
import class_miner as BlockC

# Instantiate the Node
app = imports.Flask(__name__)
imports.CORS(app)

# Instantiate the Blockchain
blockchain = BlockC.Blockchain()

@app.route('/')
def disclaimer():
    return imports.render_template('./disclaimer.html')
@app.route('/index')
def index():
    return imports.render_template('./index.html')

@app.route('/configure')
def configure():
    return imports.render_template('./configure.html')



@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = imports.request.form

    # Check that the required fields are in the POST'ed data
    required = ['sender_address', 'recipient_address', 'amount', 'signature','miningReward']
    if not all(k in values for k in required):
        return 'Missing values', 400
    # Create a new Transaction
    transaction_result = blockchain.submit_transaction(values['sender_address'], values['recipient_address'], values['amount'], values['signature'],values['miningReward'])

    if transaction_result == False:
        response = {'message': 'Invalid Transaction!'}
        return imports.jsonify(response), 404
    else:
        response = {'message': 'Transaction will be added to Block '+ str(transaction_result)}
        return imports.jsonify(response), 201

@app.route('/transactions/get', methods=['GET'])
def get_transactions():
    #Get transactions from transactions pool
    transactions = blockchain.transactions

    response = {'transactions': transactions}
    return imports.jsonify(response), 200

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return imports.jsonify(response), 200

@app.route('/mine', methods=['GET'])
def mine():
    # We run the proof of work algorithm to get the next proof...
    last_block = blockchain.chain[-1]
    nonce = blockchain.proof_of_work()

    # We must receive a reward for finding the proof.
    blockchain.submit_transaction(sender_address=BlockC.MINING_SENDER, recipient_address=blockchain.node_id, value=0, signature="",MReward=1)

    # Forge the new Block by adding it to the chain
    previous_hash = blockchain.hash(last_block)
    block = blockchain.create_block(nonce, previous_hash)

    response = {
        'message': "New Block Forged",
        'block_number': block['block_number'],
        'transactions': block['transactions'],
        'nonce': block['nonce'],
        'previous_hash': block['previous_hash'],
    }
    return imports.jsonify(response), 200



@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    values = imports.request.form
    nodes = values.get('nodes').replace(" ", "").split(',')

    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400

    for node in nodes:
        blockchain.register_node(node)

    response = {
        'message': 'New nodes have been added',
        'total_nodes': [node for node in blockchain.nodes],
    }
    return imports.jsonify(response), 201


@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = blockchain.resolve_conflicts()

    if replaced:
        response = {
            'message': 'Our chain was replaced',
            'new_chain': blockchain.chain
        }
    else:
        response = {
            'message': 'Our chain is authoritative',
            'chain': blockchain.chain
        }
    return imports.jsonify(response), 200


@app.route('/nodes/get', methods=['GET'])
def get_nodes():
    nodes = list(blockchain.nodes)
    response = {'nodes': nodes}
    return imports.jsonify(response), 200


