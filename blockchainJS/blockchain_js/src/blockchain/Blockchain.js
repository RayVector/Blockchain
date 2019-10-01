const SHA256 = require('crypto-js/sha256');

Date.prototype.yyyymmdd = function () {
  let mm = this.getMonth() + 1;
  let dd = this.getDate();

  return [
    (mm > 9 ? '' : '0') + mm,
    (dd > 9 ? '' : '0') + dd,
    this.getFullYear()
  ].join('/');
};

export class Block {
  constructor(timestamp, data, previousHash = '') {
    this.index = 0;
    this.timestamp = timestamp;
    this.creationDate = new Date().yyyymmdd();
    this.previousHash = '0';
    this.hash = this.calculateHash();
    this.nonce = 0;
    this.data = data;
  }

  calculateHash() {
    return SHA256(this.index + this.previousHash + this.timestamp + this.creationDate + JSON.stringify(this.data) + this.nonce).toString();
  }

  mineBlock(difficulty) {
    while (this.hash.substring(0, difficulty) !== Array(difficulty + 1).join('0')) {
      this.nonce++;
      this.hash = this.calculateHash();
    }
    console.log('Block mined: ' + this.hash);
  }
}


export default class Blockchain {
  constructor() {
    this.chain = [this.createGenesis()];
    this.difficulty = 4;
  }

  createGenesis() {
    return new Block(new Date().yyyymmdd(), 'Genesis block', '0')
  }

  latestBlock() {
    return this.chain[this.chain.length - 1]
  }

  addBlock(newBlock) {
    newBlock.index = this.latestBlock().index + 1;
    newBlock.previousHash = this.latestBlock().hash;
    newBlock.mineBlock(this.difficulty);
    this.chain.push(newBlock);
  }

  checkValid() {
    for (let i = 1; i < this.chain.length; i++) {
      const currentBlock = this.chain[i];
      const previousBlock = this.chain[i - 1];

      if (currentBlock.hash !== currentBlock.calculateHash()) {
        return false;
      }

      if (currentBlock.previousHash !== previousBlock.hash) {
        return false
      }
    }
    return true;
  }

}
