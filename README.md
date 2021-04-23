# Encryption utility
## How to run project?
* Clone this repo and change directory to there (e.g. `cd encryption_utility`)
* Make environment for python3 (e.g. `python3 -m venv env`)
* Activate environment (e.g. `source env/bin/activate`)
* Change local environment pythonpath: export PYTHONPATH=${PYTHONPATH}:\`pwd\`
* In order to install modules - run `pip install requirements.txt`
* To run the project - execute `python3 encryption_utility/main.py`


## How to use utility?
To encrypt the file use `encrypt filename encr_mode args`

* Possible `encr_mode`:
1) `caesar`, where `args = int key`
2) `vigenere`, where `args = str key`
3) `vernam`, where `args = str key`

To decrypt the file use `decrypt filename decr_mode args`

* Possible `decr_mode`:
1) `caesar`, where `args = [int key]`
    * If no `key` passed, breaking a cipher begins in the assumption of an English text 
2) `vigenere`, where `args = str key`
3) `vernam`, where `args = str key`

To exit use `exit`

