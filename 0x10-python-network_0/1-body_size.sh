#!/bin/bash

# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL from the command line argument
URL="$1"

# Use curl to get only the response header (-I option)
# Look for Content-Length in the header
# Extract the numeric part using awk
size_in_bytes=$(curl -sI "$URL" | grep -i Content-Length | awk '{print $2}')

# Display the size in bytes
echo "Size of the response body: $size_in_bytes bytes"

