#!/bin/bash
# A script that displays the size of the body of a request response
curl -s $1 | wc -c
