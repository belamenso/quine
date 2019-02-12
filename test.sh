#!/bin//bash

python3 quine.py > replica.py
D=$(diff quine.py replica.py)
if [ -z "$D" ]; then
	echo -e "\033[32mSUCCESS\033[0m"
else
	echo -e "\033[31mFAILED:\033[0m\n$D"
fi
