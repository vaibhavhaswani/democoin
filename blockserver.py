import json
from flask import Flask, jsonify
from blockchain import Blockchain
from datetime import datetime

app=Flask(__name__)
blockchain=Blockchain()

@app.route('/')
def home():
    return '<p>Blockchain Home</p>'

@app.route('/mine',methods=['GET'])
def mine_block():
    prev_block=blockchain.get_prev_block()
    prev_proof=prev_block['proof']
    proof=blockchain.get_proof(prev_proof)
    prev_hash=blockchain.get_hash(prev_block)
    block=blockchain.create_block(proof,prev_hash)
    block_response={
        "message":"Congratulations! block has been mined successfully",
        "block_index":block["index"],
        "timestamp":str(datetime.now()),
        "proof":proof,
        "prev_hash":prev_hash
    }
    return jsonify(block_response,200)

@app.route('/getchain',methods=['GET'])
def get_chain():
    response={
        "chain":blockchain.chain,
        "length":len(blockchain)
    }
    return jsonify(response,200)


@app.route('/isvalid',methods=['GET'])
def is_valid():
    valid=blockchain.is_chain_valid()
    if valid:
        response={
            "message":"Chain is Valid",
            "is_valid":True
        }
    else:
        response={
            "message":"Chain is Invalid or Tampered",
            "is_valid":False
        }
    return jsonify(response,200)



app.run(host='0.0.0.0',port=8000,debug=True) #making public network