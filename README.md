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
1) caesar, where `args = int shift`
2) vigenere, which is not implemented yet
3) vernam, which is not implemented too

To decrypt the file use `decrypt filename decr_mode args`

* Possible encryption mode:
1) caesar, where `args = [int shift]`
2) vigenere, which is not implemented yet
3) vernam, which is not implemented too

To exit use `exit`
