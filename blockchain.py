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
        # hashing challenge : leading zeros , n_zeros=4 (more n more challenge)
        n_zeros=4
        zeros=str('0'*n_zeros)
        new_proof=0
        valid_proof=False

        def formula(proof1,proof2):
            out=proof1**2-proof2**2 #it can be anything that yeilds non symmetric output
            return str(out)

        while not valid_proof:
            proof_hash=hashlib.sha256(formula(new_proof,prev_proof).encode()).hexdigest() # encode() for byte string conversion and hexdigest() for converting hex to str
            if proof_hash[:n_zeros]==zeros:
                valid_proof=True
                break
            new_proof+=1
        
        return new_proof
    