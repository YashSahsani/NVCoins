import imports
def sha256(message):
    # converts into hash
    return imports.hashlib.sha256(message.encode('ascii')).hexdigest()

def mine(message, difficulty=1):
   # miners method
   assert difficulty >= 1
   prefix = '1' * difficulty
   for i in range(1000):
      digest = sha256(str(hash(message)) + str(i))
      if digest.startswith(prefix):
         print ("after " + str(i) + " iterations found nonce: "+ digest)
      return digest

