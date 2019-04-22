import time
import json
import hashlib
import struct
import sys
import base64
import blockchain
import binascii
import ecdsa
import requests
import bitcoin
from json_with_dates import loads

class Block:
    def __init__(self, block_hash, size, height, version, merkle_root, time, nonce, bits, difficulty, hash_prev_block):
        self.block_hash = block_hash
        self.size = size
        self.height = height
        self.version = version
        self.hash_prev_block = hash_prev_block
        self.merkle_root = merkle_root
        self.difficulty = difficulty
        self.time = time
        self.nonce = 0
        self.bits = bits


    def setNonce(self, nonce):
        self.nonce = nonce

    def addTransactions(self, transaction):
        self.transactions.append(transaction)

    def __str__(self):
        return '-'.join([self.hash_merkle_block, str(self.nonce)])

def createPrivateKey():
    private_key = bitcoin.random_key()
    return private_key

def createPublicKey():
    return bitcoin.privtopub(createPrivateKey())

def createBitcoinAddress():
    return bitcoin.pubtoaddr(createPublicKey())




print(createPrivateKey())
print(createPublicKey())
print(createBitcoinAddress())

block_request = requests.get('https://blockexplorer.com/api/block/0000000000000000079c58e8b5bce4217f7515a74b170049398ed9b8428beb4a')

block = loads(block_request.text)
print(block['hash'])

block1 = Block(block['hash'],block['size'],block['height'],block['version'],block['merkleroot'],block['time'], block['nonce'],block['bits'],block['difficulty'],block['previousblockhash'])

print(block1)
##print(block[0], block[1], block[2], block[3], block[4],block[5], block[6], block[7], block[8], block[9], block[10], block[13])
print('')
