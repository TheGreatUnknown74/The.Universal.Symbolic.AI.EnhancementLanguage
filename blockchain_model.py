# blockchain_model.py
# Basic representation of transactional integrity in a blockchain system

import hashlib

class Block:
    def __init__(self, previous_hash, transaction):
        self.previous_hash = previous_hash
        self.transaction = transaction
        self.block_data = "-".join(transaction) + "-" + previous_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.genesis_block()

    def genesis_block(self):
        self.chain.append(Block("0", ["Genesis Block"]))

    def add_block(self, transaction):
        previous_hash = self.chain[-1].block_hash
        self.chain.append(Block(previous_hash, transaction))

    def display_chain(self):
        for block in self.chain:
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Transaction: {block.transaction}")
            print(f"Block Hash: {block.block_hash}\n")

# Example usage
blockchain = Blockchain()
blockchain.add_block(["Transaction 1"])
blockchain.add_block(["Transaction 2"])
blockchain.display_chain()
