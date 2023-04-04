#!/bin/bash
#curl
curl -sI "$1" | grep "Allow"
