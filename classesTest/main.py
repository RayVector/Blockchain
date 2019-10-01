import hashlib
import json


class Block:
    def __init__(self, id, date, transaction, prevhash=''):
        self.id = id
        self.date = date
        self.transaction = transaction
        self.prevhash = prevhash
        self.hash = self.calchash()

    def calchash(self):
        block_string = json.dumps(
            {"id": self.id, "date": self.date, "transaction": self.transaction, "prevhash": self.prevhash},
            sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def __str__(self):
        string = "id:" + str(self.id) + "\n"
        string += "date:" + str(self.date) + "\n"
        string += "transaction:" + str(self.transaction) + "\n"
        string += "prevhash:" + str(self.prevhash) + "\n"
        string += "hash:" + str(self.hash) + "\n"

        return string


class BlockChain:
    def __init__(self):
        self.chain = [self.generateGenesisBlock()]

    def generateGenesisBlock(self):
        return Block(0, '01/01/2017', 'Genesis Block')

    def getLastBlock(self):
        return self.chain[-1]

    def addBlock(self, newBlock):
        newBlock.prevhash = self.getLastBlock().hash
        newBlock.hash = newBlock.calchash()
        self.chain.append(newBlock)

    def isChainValid(self):
        for i in range(1, len(self.chain)):
            prevb = self.chain[i - 1]
            currb = self.chain[i]
            if (currb.hash != currb.calchash()):
                print("invalid block")
                return False
            if (currb.prevhash != prevb.hash):
                print("invalid chain")
                return False
        return True


testBC = BlockChain()
testBC.addBlock(Block(1, '20/05/2017', 100))
testBC.addBlock(Block(2, '20/05/2018', 20))
# testBC.chain[1].transaction = 1
# testBC.chain[1].hash = testBC.chain[1].calchash()
for b in testBC.chain:
    print(b)
print(testBC.isChainValid())
