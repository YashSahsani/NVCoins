import imports
import transaction as trans
app = imports.Flask(__name__)

@app.route('/')
def index():
        return imports.render_template('./index.html')

@app.route('/make/transaction')
def make_transaction():
    return imports.render_template('./make_transaction.html')

@app.route('/view/transactions')
def view_transaction():
    return imports.render_template('./view_transactions.html')

@app.route('/wallet/new', methods=['GET'])
def new_wallet():
        random_gen = imports.Crypto.Random.new().read
        private_key = imports.RSA.generate(1024, random_gen)
        public_key = private_key.publickey()
        response = {
                'private_key': imports.binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii'),
                'public_key': imports.binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii')
        }

        return imports.jsonify(response), 200

@app.route('/generate/transaction', methods=['POST'])
def generate_transaction():
                sender_address = imports.request.form['sender_address']
                sender_private_key = imports.request.form['sender_private_key']
                recipient_address = imports.request.form['recipient_address']
                value = imports.request.form['amount']
                MReward = imports.request.form['miningReward']

                transaction = trans.Transaction(sender_address, sender_private_key, recipient_address, value, MReward)
                response = {'transaction': transaction.to_dict(), 'signature': transaction.sign_transaction()}
                return imports.jsonify(response), 200


