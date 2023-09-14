
# URL Isolator
Given input text, this program identifies all the urls that meet the following DFA criteria:
1.  Starts with http (`http://www.uaa.alaska.edu`)
2. Have an IP address (`192.168.0.1/check-it-out/`)
3. Contain .com .edu .org .net .gov (`coolbeans.org/coffee`)

**STATUS.**
This project is in completed.

## Setup 
This program only requires python.

## Usage
In this directory, run `python main.py`. The output of this program will be printed to the terminal.
In order to test this program on different text, replace the text in the input variable in main.