import client
def display_transaction(transaction):             
              # displays transactions
              dict = transaction.to_dict()
              print("sender: "+dict['sender'])
              print('-'*20)
              print("reciver: "+dict['reciver'])
              print('-'*20)
              print("amount: "+str(dict['value']))
              print('-'*20)
              print("time: "+str(dict['time']))
              print('-'*20)
              print('#'*30)

def dump_blockchain (self):
            # Displays block Chains
            print ("Number of blocks in the chain: " + str(len (self)))
            for x in range (len(client.TPCoins)):
                      block_temp = client.TPCoins[x]
                      print ("block # " + str(x))
                      for transaction in block_temp.verified_transactions:
                            display_transaction (transaction)


