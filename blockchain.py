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
        '''create blockchain block'''

        block={
            "index":len(self.chain)+1,
            "timestamp":str(datetime.now()),
            "proof":proof,
            "prev_hash":prev_hash
        }
        self.chain.append(block)
    