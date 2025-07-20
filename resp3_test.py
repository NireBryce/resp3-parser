import pytest


# from resp3_parser import resp3_simple_string resp3_integer, resp3_bulk_string, ...

# simple string

# "+hello\r\n"
# empty ("+\r\n")
# spaces "+hello world\r\n"

# integer

#  ":123\r\n"
#  ":-456\r\n"
#    ":0\r\n"

# bulk_string
#     "$5\r\nhello\r\n"
#     "$-1\r\n"     # null bulk string
#     "$0\r\n\r\n"  # empty bulk string

