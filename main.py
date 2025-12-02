from hashlib import sha256

transactions1 = ["Daníel le envia 5 a Mauro",
                "Luis le envia  3  a Aida",
                "Luis le envia  2 a Mauro"]

transactions2 = ["Piero le envia  5 a Luis",
                "Lis le envia  3  a Aida",
                "Luis le envia 2 a Mau"]

class Block: 

      def __init__(self,previous_hash_block,data) :
        self.previous_hash_block = previous_hash_block
        self.data= data
        self.nonce= 0
    

      def hash(self):
        info= "#".join(self.data) +self.previous_hash_block + str(self.nonce)
        return sha256(info.encode()).hexdigest()

class Blockchain:
    
    difficulty = 3

    def __init__(self):
      self.chain= []

    
    def add(self,block):
        self.chain.append(block)

    
    def mine(self,block):
        while True:
            if block.hash()[:self.difficulty] == "0"* self.difficulty:
                self.add(block)
                break
            else:
                block.nonce +=1


block_chain = Blockchain()



b1 = Block("0"*64,transactions1)
print("Hash bloque 1:", b1.hash())

block_chain.mine(b1)
print("Hash final 1:",block_chain.chain[0].hash())
print("Valor de nonce:", block_chain.chain[0].nonce)



b2= Block(block_chain.chain[-1].hash(),transactions2)
block_chain.mine(b2)

block_chain.mine(b2)
print("Hash final 2:",block_chain.chain[1].hash())
print("Valor de nonce:", block_chain.chain[1].nonce)

