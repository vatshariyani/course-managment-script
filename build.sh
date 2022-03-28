#!/bin/bash

sudo mysql_secure_installation
sudo service mysql start
sudo apt install pip
sudo pip3 install -r requirements.txt
