import sys
import datetime
import hashlib
import time
class Block:
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.now()
    def __init__(self, data):
        self.data = data

    def hash(self):
        h = hashlib.sha256()
        # previous_hash is include this is what makes blockchain
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest()

    def __str__(self):
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\n--------------"
class Blockchain:
    maxNonce = 2**32 # max number of Nouncce or tries
    target = None # for hash mining
    block = Block("Genesis")  # creation of genesis blocks
    dummy = head = block
    def add(self, block):
        # for adding a block to the chain
        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1
        # every block has a pointer to next block (this add block at end of block_chain)
        self.block.next = block
        # It moves next pointer up (so that we can keep adding new block)
        self.block = self.block.next
    def mine(self, block, diff):
        self.target = 2 ** (256-diff)
        for n in range(self.maxNonce):
            # check if hash is vaild or not
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                break
            else:
                block.nonce += 1
if(len(sys.argv) != 3):
	print("Usage python block-chain.py <Mining Diffcultly> <No. of Blocks>")
	sys.exit(0)
try:
    blockchain = Blockchain()
    min_diff = int(sys.argv[1])
    for n in range(int(sys.argv[2])):
            blockchain.mine(Block("Block " + str(n+1)),min_diff)
    while blockchain.head != None:
           print(blockchain.head)
           blockchain.head = blockchain.head.next
except Exception as e:
	print("Invalid Inputs")