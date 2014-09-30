#!/bin/bash

HOST=$1
shift
for ARG in "$@"
do
nmap -PN --host_timeout 201 --max-retries 0 -p $ARG $HOST
done
