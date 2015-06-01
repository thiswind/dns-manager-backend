#!/bin/bash

#sudo apt-get update
#sudo apt-get -y -f upgrade
#sudo apt-get install python-dev

#sudo pip install --upgrade virtualenv

if [ -e .venv ]; then
    echo '.venv already exists.'
else
    virtualenv .venv
    echo '.venv created.'

fi


. .venv/bin/activate

pip install -q --upgrade pip
pip install -q --upgrade flask-restful
pip install -q --upgrade Flask-Testing
pip install -q --upgrade pyOpenSSL
pip install -q --upgrade flask-cors
pip install -q --upgrade dnspython
pip install -q --upgrade docker-py

deactivate

#gen keys
KEY_HOME=".keys"
mkdir -p ${KEY_HOME}
sudo -H openssl genrsa -des3 -out ${KEY_HOME}/key.key 1024
sudo -H openssl req -new -key ${KEY_HOME}/key.key -out ${KEY_HOME}//csr.csr
sudo -H openssl x509 -req -days 365 -in ${KEY_HOME}/csr.csr -signkey ${KEY_HOME}/key.key -out ${KEY_HOME}/crt.crt
sudo -H cp ${KEY_HOME}/key.key ${KEY_HOME}/key.key.bak
sudo -H openssl rsa -in ${KEY_HOME}/key.key.bak -out ${KEY_HOME}/key.key

