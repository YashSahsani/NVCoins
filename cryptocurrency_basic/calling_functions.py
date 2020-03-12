import client
import displaying_methods
from transaction import Transaction
from Block import Block
import hash as hashes
def main():
        # Creating Clients
        Dinesh = client.Client()
        yash = client.Client()
        John = client.Client()
        Dexter = client.Client()
        
        # Creating Transactions (Senders , reciver , Amount/Value)
        t0 = Transaction("Genesis",Dinesh.identity,10)
        t1 = Transaction(Dinesh,yash.identity,100)
        t2 = Transaction(yash,John.identity,1000)
        t3 = Transaction(yash,Dexter.identity,1000)
        t4 = Transaction(John,Dexter.identity,223)
        t5 = Transaction(John,Dexter.identity,102)
        t6 = Transaction(yash,Dexter.identity,100)
        t7 = Transaction(Dinesh,yash.identity,10000)
        t8 = Transaction(yash,John.identity,100)
        t9 = Transaction(yash,John.identity,500)
        
        # Signing_transactions
        t1.sign_transaction()
        t2.sign_transaction()
        t3.sign_transaction()
        t4.sign_transaction()
        t5.sign_transaction()
        t6.sign_transaction()
        t7.sign_transaction()
        t8.sign_transaction()
        t9.sign_transaction()
        
        # appending to global transaction list
        client.transactions.append(t0)
        client.transactions.append(t1)
        client.transactions.append(t2)
        client.transactions.append(t3)
        client.transactions.append(t4)
        client.transactions.append(t5)
        client.transactions.append(t6)
        client.transactions.append(t7)
        client.transactions.append(t8)
        client.transactions.append(t9)
        
        
        # Miner adds a block ( every block has three trasaction details)
        for i in range (0,3):
            block = Block()
            for i in range(3):
                            temp_transaction = client.transactions[client.last_transaction_index]
                            # validate transaction (remaining)
                            # if valid (remaining)
                            block.verified_transactions.append(temp_transaction)
                            client.last_transaction_index += 1
            #  updating pervious hash
            block.previous_block_hash = client.last_block_hash
            # calling miner
            block.Nonce = hashes.mine(block, 10)
            digest = hash(block)
            # adding block to the blockchain
            client.TPCoins.append(block)
            client.last_block_hash = digest
        # dumping blockChain
        displaying_methods.dump_blockchain(client.TPCoins)
