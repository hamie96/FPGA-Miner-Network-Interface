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
    def __init__(self, block_hash, version, prev_block_hash, merkle_root, time, bits, nonce):
        self.block_hash = block_hash
        self.version = version
        self.prev_block_hash = prev_block_hash
        self.merkle_root = merkle_root
        self.time = time
        self.nonce = 0
        self.bits = bits
    
    def getBlockHash(self):
        return self.block_hash
    
    def getVersion(self):
        return self.version

    def getPrevBlockHash(self):
        return self.prev_block_hash

    def getMerkleRoot(self):
        return self.merkle_root

    def getTime(self):
        return self.time

    def getBits(self):
        return self.bits
    
    def setNonce(self, nonce):
        self.nonce = nonce

    def printBlock(self):
        return [self.block_hash, self.version, self.prev_block_hash, self.merkle_root, self.time, self.bits, self.nonce]

class User:
    
    def __init__(self, name):
        self.name = name
        self.private_key = None

    def setPrivateKey(self, private_key):
        self.private_key = private_key

    def createPrivateKey(self):
        self_private_key = bitcoin.random_key()

    def createPublicKey(self, private_key):
        self_public_key = bitcoin.privtopub(private_key)

    def createBitcoinAddress(self, public_key):
        self_bitcoin_addr = bitcoin.pubtoaddr(public_key)

    def returnUser(self):
        return ("User:" + self.name + "\nPrivate Key:" + str(self.private_key))


user1 = User('Charles')
print(user1.returnUser())

block_request = requests.get('https://blockexplorer.com/api/block/0000000000000000079c58e8b5bce4217f7515a74b170049398ed9b8428beb4a')

block = loads(block_request.text)

block1 = Block(block['hash'],block['version'],block['previousblockhash'],block['merkleroot'],block['time'],block['bits'], block['nonce'])

print(block1.printBlock())
##print(block[0], block[1], block[2], block[3], block[4],block[5], block[6], block[7], block[8], block[9], block[10], block[13])
print('')
