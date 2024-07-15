import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, voter_id, vote, hash, nonce):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.voter_id = voter_id
        self.vote = vote
        self.hash = hash
        self.nonce = nonce

class VotingBlockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        # Create the first block (genesis block)
        genesis_block = Block(0, "0", int(time.time()), "Genesis", "None", self.calculate_hash(0, "0", int(time.time()), "Genesis", "None", 0), 0)
        self.chain.append(genesis_block)

    def add_vote(self, voter_id, vote):
        previous_block = self.chain[-1]
        index = previous_block.index + 1
        timestamp = int(time.time())
        previous_hash = previous_block.hash
        nonce = self.proof_of_work(index, previous_hash, timestamp, voter_id, vote)
        new_hash = self.calculate_hash(index, previous_hash, timestamp, voter_id, vote, nonce)
        new_block = Block(index, previous_hash, timestamp, voter_id, vote, new_hash, nonce)
        self.chain.append(new_block)

    def proof_of_work(self, index, previous_hash, timestamp, voter_id, vote):
        nonce = 0
        while True:
            new_hash = self.calculate_hash(index, previous_hash, timestamp, voter_id, vote, nonce)
            if new_hash[:4] == "0000":
                return nonce
            nonce += 1

    def calculate_hash(self, index, previous_hash, timestamp, voter_id, vote, nonce):
        value = str(index) + str(previous_hash) + str(timestamp) + str(voter_id) + str(vote) + str(nonce)
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    def print_chain(self):
        for block in self.chain:
            print(vars(block))

if __name__ == '__main__':
    voting_blockchain = VotingBlockchain()
    voting_blockchain.add_vote("Voter_1", "Candidate_A")
    voting_blockchain.add_vote("Voter_2", "Candidate_B")
    voting_blockchain.add_vote("Voter_3", "Candidate_A")
    voting_blockchain.print_chain()
