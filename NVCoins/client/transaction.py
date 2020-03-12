import imports
class Transaction:
    def __init__(self, sender_address, sender_private_key, recipient_address, value,miningReward):
        self.sender_address = sender_address
        self.sender_private_key = sender_private_key
        self.recipient_address = recipient_address
        self.value = value
        self.miningReward = miningReward
        print(self.miningReward)

    def __getattr__(self, attr):
        #print(attr)
        #return self.data[attr]
        pass

    def to_dict(self):
        return imports.OrderedDict({'sender_address': self.sender_address,
                            'recipient_address': self.recipient_address,
                            'value': self.value,
                            'miningReward': self.miningReward})

    def sign_transaction(self):
        """
        Sign transaction with private key
        """
        try:
                  private_key = imports.RSA.importKey(imports.binascii.unhexlify(self.sender_private_key))
                  signer = imports.PKCS1_v1_5.new(private_key)
                  h = imports.SHA.new(str(self.to_dict()).encode('utf8'))
                  return imports.binascii.hexlify(signer.sign(h)).decode('ascii')
        except Exception as e:
            pass
