#!/bin/bash
# Get the byte size of the HTTP response header for a given URL.
url="$1"; response=$(curl -s -w "%{size_download}" -o /dev/null "$url"); echo "Response size: $response bytes"
