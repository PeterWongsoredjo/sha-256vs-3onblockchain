import hashlib
import time


class Block:
    # Initializes a block with its position, payload, previous hash, and chosen hash algorithm.
    def __init__(self, index, data, previous_hash, algorithm):
        self.index = index
        self.data = data
        self.previous_hash = previous_hash
        self.algorithm = algorithm
        self.timestamp = time.time()
        self.nonce = 0
        self.hash = None

    # Builds the block string and returns its hex digest using the baseline or ARIP interleaving rule.
    def compute_hash(self):
        block_string = f"{self.index}{self.data}{self.previous_hash}{self.timestamp}{self.nonce}"
        if self.algorithm == "sha256":
            return hashlib.sha256(block_string.encode()).hexdigest()
        if self.algorithm == "sha3_256":
            return hashlib.sha3_256(block_string.encode()).hexdigest()
        if self.nonce % 2 == 0:
            return hashlib.sha3_256(hashlib.sha256(block_string.encode()).hexdigest().encode()).hexdigest()
        return hashlib.sha256(hashlib.sha3_256(block_string.encode()).hexdigest().encode()).hexdigest()

    # Performs the Proof-of-Work by incrementing the nonce until the hash has enough leading zeros.
    def mine_block(self, difficulty):
        target = "0" * difficulty
        while not self.compute_hash().startswith(target):
            self.nonce += 1
        self.hash = self.compute_hash()
        return self.hash


class Blockchain:
    # Sets up the chain with its difficulty and algorithm, then creates the genesis block.
    def __init__(self, difficulty, algorithm):
        self.difficulty = difficulty
        self.algorithm = algorithm
        self.chain = [self.create_genesis_block()]

    # Builds and mines the first block of the chain with a fixed previous hash.
    def create_genesis_block(self):
        genesis = Block(0, "Genesis Block", "0", self.algorithm)
        genesis.mine_block(self.difficulty)
        return genesis

    # Creates the next block linked to the last block, mines it, appends it, and returns it.
    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), data, previous_block.hash, self.algorithm)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        return new_block
