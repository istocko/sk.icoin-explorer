#!/bin/bash
mysql -u root -pneousb -e "drop database abe;create database abe;"
sudo python setup.py build
sudo python setup.py install
sudo python -m Abe.abe --config my-abe.conf  --commit-bytes 100000 --no-serve
sudo python -m Abe.abe --config my-abe.conf
