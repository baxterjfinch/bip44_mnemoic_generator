For python 3, ensure correct pip3 version.

I had to run
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python3 get-pip.py

and then
python3 -m pip install -r requirements.txt
