# IMPORTS

from datetime import  datetime
import hashlib
from flask import Flask, jsonify
import json


# Blockchain Class

class Blockchain:

    def __init__(self):
        '''chain constructor'''

        self.chain=[]
        self.create_block(proof=1,prev_hash=0)
        # hashing challenge : leading zeros , n_zeros=4 (more n more challenge)
        self.n_zeros=4
        self.zeros=str('0'*self.n_zeros)

    def formula(self,proof1,proof2):
        '''formula to get validate proof hash'''
        out=(proof1)**2-(proof2**2) #it can be anything that yeilds non symmetric output
        return str(out)

    def create_block(self,proof,prev_hash):
        '''create and returns blockchain block'''

        block={
            "index":len(self.chain)+1,
            "timestamp":str(datetime.now()),
            "proof":proof,
            "prev_hash":prev_hash
        }
        self.chain.append(block)
        return block



    def get_prev_block(self):
        "return prev block"
        
        return self.chain[-1]


    def get_pow(self,prev_proof):
        '''returns proof of work value or nonce value'''
        new_proof=0
        valid_proof=False

        while not valid_proof:
            proof_hash=hashlib.sha256(self.formula(new_proof,prev_proof).encode()).hexdigest() # encode() for byte string conversion and hexdigest() for converting hex to str
            if proof_hash[:self.n_zeros]==self.zeros:
                valid_proof=True
                break
            new_proof+=1
        
        return new_proof


    def get_hash(self,block):
        '''returns hash for the block'''

        encoded_block=json.dumps(block,sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest() 
    

    def is_chain_valid(self,chain):

        prev_block=chain[0]
        block_inx=1

        while block_inx<len(chain):
            block=chain[block_inx]
            if block["prev_hash"]!=self.get_hash(prev_block):
                return False

            proof_sol=self.formula(block["proof"],prev_block["proof"])
            proof_hash=hashlib.sha1(proof_sol.encode()).hexdigest()

            if proof_hash[:self.n_zeros]!=self.zeros:
                return False

            block_inx+=1
            prev_block=block
        
        return True
