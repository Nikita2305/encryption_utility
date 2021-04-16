# Encryption utility
## How to run project?
* Clone this repo and change directory to there (e.g. `cd encryption_utility`)
* Make environment for python3 (e.g. `python3 -m venv env`)
* Activate environment (e.g. `source env/bin/activate`)
* In order to install modules - run `pip install requirements.txt`
* Change directory to the folder with sources: `cd encryption_utility`
* To run the project - execute `python3 main.py`


## How to use utility?
To encrypt the file use `encrypt filename encr_mode args`

* Possible encryption mode:
<<<<<<< HEAD
1) `caesar`, where `args = int key`
2) `vigenere`, where `args = str key`
3) `vernam`, where `args = str key`
=======
1) `caesar`, where `args = int shift`
2) `vigenere`, which is not implemented yet
3) `vernam`, which is not implemented too
>>>>>>> 40357009186363dca4d65e329a1a76d181caf294

To decrypt the file use `decrypt filename decr_mode args`

* Possible decryption mode:
1) `caesar`, where `args = [int shift]`
<<<<<<< HEAD
    If no shift passed, breaking a cipher begins in the assumption of an English text 
2) `vigenere`, where `args = str key`
3) `vernam`, where `args = str key`
=======
2) `vigenere`, which is not implemented yet
3) `vernam`, which is not implemented too
>>>>>>> 40357009186363dca4d65e329a1a76d181caf294

To exit use `exit`
