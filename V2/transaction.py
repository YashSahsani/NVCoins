import imports
class Transaction:
        def __init__(self,sender,reciver,value):
            self.sender = sender
            self.reciver = reciver
            self.value = value
            self.time = imports.datetime.datetime.now()

        def to_dict(self):
              if self.sender == "Genesis":
                    identity = "Genesis"
              else:
                    identity = self.sender.identity

              return imports.collections.OrderedDict({ "sender":identity, "reciver":self.reciver , "value":self.value, "time":self.time})

        def sign_transaction(self):
              # As name suggests it signs the transactions
              private_key = self.sender._private_key
              signer = imports.PKCS1_v1_5.new(private_key)
              h = imports.SHA.new(str(self.to_dict()).encode('utf-8'))
              return (imports.binascii.hexlify(signer.sign(h)).decode('ascii'))

