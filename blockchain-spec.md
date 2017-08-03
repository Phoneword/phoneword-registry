Genesis
=> Signature (Blockroot)
=> Blockroot
  => Header:
    -> Previous (null)
    -> Datetime (unixtime)
    -> Block Height
  => Txns:
    -> Register Initial Master Key
    -> Blockchain Structure Specification
    -> Transactions / Transaction Types Specification
    -> Effective Block # For This Spec (0)
  => State:
    -> Sorted Array of Current/Future Blockchain Specifications
    -> Blank Phoneword Tree with Master Key Record at Root

Block #1
=> Signature (Blockroot)
=> Blockroot
  => Header:
    -> Previous (genesis)
    -> Datetime (unixtime)
    -> Block Height
  => Txns:
    -> Register Request From Individual Keys for Foundational Numbers w/ Individual Key and Master Key Signature
      -> Creates a "null" record for the numbers with only the authoritative key
    -> Individual Keys Assign Data in Transactions
      -> Include Initial Data for Prototyping:
        -> Ownership Info (Important)
          -> Authoritative Key(s) w/ History (pointers to origin block+transaction for initial registration and any changes in keys/ownership)
          -> Alias
          -> E-mail
          -> Phone Number
          -> Website
        -> IPFS Key
          -> Pub/sub Communication
          -> Arbitrary Lookup

/_/key

genesis
-> sig
-> root
  -> header
    -> prev
    -> 
  -> txns
  -> state

# State Tree
  CALCULATED AT INCLUSION:
  /1/2/3/4/5/etc/_/last_state => /block/.../state/1/2/3/4/5/etc/_/
  /1/2/3/4/5/etc/_/this_txn => /block/.../txns/txn#

  CALCULATED PER TXN(S) OR PREV_STATE:
  /1/2/3/4/5/etc/_/key
  /1/2/3/4/5/etc/_/owner/alias
  /1/2/3/4/5/etc/_/owner/email
  /1/2/3/4/5/etc/_/owner/phone
  /1/2/3/4/5/etc/_/owner/website
  /1/2/3/4/5/etc/_/ipfs

# State
## Ideal
- State should always be deterministic given all inputs (genesis block with specification, and all future blocks that include future hashes).
- State should always be included in all valid blocks for the sake of verification of state->state and for the benefit of "light" clients.
- The initial state (genesis) should consist of a single MASTER_UPDATE that includes a CHAIN_MAP (from null) to set initial state and valid BLOCK and TRANSACTION rules.

## Example
- Phoneword specific, the genesis state tree should look like:
  /_/ => root state information
  /_/txn_rules
  /_/block_rules
  /_/master_key

- Phoneword specific, a future state might look like:
  /_/txn_rules
  /_/block_rules
  /_/master_key
  /1/2/3/4/5/6/7/8/9/0/1/2/3/4/5/_/ => root number information
  /1/2/3/4/5/6/7/8/9/0/1/2/3/4/5/_/key => number authoritative key
  /1/2/3/4/5/6/7/8/9/0/1/2/3/4/5/_/claim => number authoritative key

  /2/3/4/5/6/7/8/9/0/1/2/3/4/5/6/_/ => root number information
  /2/3/4/5/6/7/8/9/0/1/2/3/4/5/6/_/key => number authoritative key
  /2/3/4/5/6/7/8/9/0/1/2/3/4/5/6/_/claim => information on who can change what and when (eg expiration, whether a parent prefix key can overwrite, etc)
  /2/3/4/5/6/7/8/9/0/1/2/3/4/5/6/_/owner/alias => alias for owner
  /2/3/4/5/6/7/8/9/0/1/2/3/4/5/6/_/owner/email => e-mail for owner
  /2/3/4/5/6/7/8/9/0/1/2/3/4/5/6/_/owner/website => website for owner
  /2/3/4/5/6/7/8/9/0/1/2/3/4/5/6/_/ipfs => ipfs pointer for owners (arbitrary)

  /1/2/3/4/5/6/7/8/9/_/ => prefix information
  /1/2/3/4/5/6/7/8/9/_/key => prefix authoritative key
  /1/2/3/4/5/6/7/8/9/_/owner/alias => alias for owner
  /1/2/3/4/5/6/7/8/9/_/owner/email => email for owner
  /1/2/3/4/5/6/7/8/9/_/owner/website => website for owner
  /1/2/3/4/5/6/7/8/9/_/ipfs => alias for owner

# Blocks
## Ideal
- Blocks should boil down to code: how to validate a block, how to validate a block against a known valid previous block, and how to apply a block to get expected state
- Block x should be organized as:
  BLOCK_X<objhash>
    MINER_SIG<sig> (against BLOCKROOT hash)
    BLOCKROOT<objhash>
      MINER_KEY<key> - for nonrepudiation, authentication, and possible reward
      BLOCK_DATETIME<unixtime> - for convenience and to maybe mitigate transactions authored too far in the past
      BLOCK_HEIGHT<int> - 
      BLOCK_IDX<indexed arr of block objs>
        0 => genesis block
        1 => block #1
        ...
        BLOCK_HEIGHT-1 => block #x-1
      TXNS[arr of txns in order of application]
        ...
      STATE{arbitrary state tree}

# Transactions
## Ideal
- Transactions should ultimately be able to be boiled down to an atomic protobuf structure.
- Transactions should always be signed by at least one party, even if self-signed
- Transactions should always include a known state at time of authorship in order to lock it down from being applied to a future state. This should be relatively arbitrary but there should be a mandatory minimum level of specification.
- Transactions should eventually boil down to code: inputs needed to create the transaction, how to create a transaction given those inputs, how to validate a transaction given a state, and how to apply the transaction to the state given the validated transaction and previous state (and thus include it in a block).

## Types

### MASTER_UPDATE
This is the type of transaction that explicitly induces a hardfork. It changes the specification of the chain at a particular block number. This block number should be "pegged" in future clients if they agree with the change, since a MASTER_UPDATE could contain things that would completely decimate the integrity of the chain if forked. Update could be new transaction types, modifying or removing existing transaction types, mandatory shape change (aka mapping) of old chain state to new chain state (including changes of the root key).

This transaction is used to create the genesis block and is self-signed by the master key.

This is an nTimeLock transaction that is mandatory and thus should be kept in state.

TYPE: MASTER_UPDATE
CURRENT_SPECIFICATION_STATE:
EFFECTIVE_BLOCK_NUMBER:
DELTA:
  < MAP_CHAIN_STATE | NEW_TRANSACTION_TYPE | MODIFY_TRANSACTION_TYPE | SET_MASTER_KEY >
  ...
  AUTH_SIGNATURE: <SIGNATURE OF ABOVE W/ MASTER KEY>

### UPDATE_NUMBER
A standard transaction that assigns or changes information in a number. In the case of a number with no history, CURRENT_LOCATION_STATE is null and DELTA must contain a key.

TYPE: UPDATE_NUMBER
LOCATION: /1/2/4/5/7/etc
VALID_PREV_LOCATION_STATE: <IPFS PATH/HASH OR NULL>
REQUEST_KEY: <ECDSA KEY>
DELTA:
  <KEY | OWNER/ALIAS | OWNER/EMAIL | ... | IPFS>
  ...
REQ_METADATA: <arbitrary IPFS hash>
  REQ_SIGNATURE: <SIGNATURE OF ABOVE W/ ECDSA KEY>
    AUTH_SIGNATURE: <SIGNATURE OF A CURRENT AUTHORITATIVE KEY>