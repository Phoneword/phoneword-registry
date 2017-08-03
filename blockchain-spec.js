// Utils
let obj_hash = (obj) => {
  // deterministically and recursively walk an object's properties and 
  // values to create a hash; maybe use jsIPFS for this?
}

let gen_priv_key = (entropy) => {/*generate a private key using entropy*/}

let calc_pub_key = (private_key) => {/*calculate a public key from a private key*/}

let create_signature = (hash, private_key) => {/*sign a hash with a private key*/}

// Pre-Genesis State
// Single transaction type to establish genesis block. All other pieces only function to facilitate that.
let state = {
  rules: {
    create_block: (prev_blk, txns, options) => {/*block*/},
    validate_block: (prev_blk, new_blk) => {/*bool*/},
    create_txn: (state, type, options) => {/*transaction*/},
    validate_txn: (state, txn) => {/*bool*/},
    apply_txn: (state, txn) => {/*state*/},
    transaction_types: {
      "MASTER_UPDATE": {
        create: (state, options) => {/*transaction*/},
        validate: (state, txn) => {/*bool*/},
        apply: (state, txn) => {/*state*/}
      }
    }
  },
  data: {}
}

// Phoneword Genesis Transaction

// Phoneword Genesis Block

// Phoneword Block #1 Transactions

// Phoneword Block #1 Block
// Genesis Transaction
// Single self-signed MASTER_UPDATE transaction establishing master key, initial state and rules.

