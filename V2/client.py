import imports
transactions = []
TPCoins = []
last_transaction_index = 0
last_block_hash = ""
class Client:
   # Create a Client which can send and recivie  money
   def __init__(self):
      random = imports.Crypto.Random.new().read
      self._private_key = imports.RSA.generate(1024, random)
      self._public_key = self._private_key.publickey()
      self._signer = imports.PKCS1_v1_5.new(self._private_key)

   @property
   def identity(self):
      return imports.binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')
