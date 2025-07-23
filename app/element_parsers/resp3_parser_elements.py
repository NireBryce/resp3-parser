import resp3_array
import resp3_attribute
import resp3_bignum
import resp3_boolean
import resp3_bulk_error
import resp3_bulk_string
import resp3_double
import resp3_integer
import resp3_map
import resp3_null
import resp3_push
import resp3_set
import resp3_simple_error
import resp3_simple_string
import resp3_verbatim_string

class RESP3: 
    """RESP3 parser elements"""
    @classmethod
    def array(cls, data):
        resp3_array.parse_array(data)
    @classmethod
    def attribute(cls, data):
        resp3_attribute.parse_attribute(data)
    @classmethod
    def bignum(cls, data):
        resp3_bignum.parse_bignum(data)
    @classmethod
    def boolean(cls, data):
        resp3_boolean.parse_boolean(data)
    @classmethod
    def bulk_error(cls, data):
        resp3_bulk_error.parse_bulk_error(data)
    @classmethod
    def bulk_string(cls, data):
        resp3_bulk_string.parse_bulk_string(data)
    @classmethod
    def double(cls, data):
        resp3_double.parse_double(data)
    @classmethod
    def integer(cls, data):
        resp3_integer.parse_integer(data)
    @classmethod
    def map(cls, data):
        resp3_map.parse_map(data)
    @classmethod
    def null(cls, data):
        resp3_null.parse_null(data)
    @classmethod
    def push(cls, data):
        resp3_push.parse_push(data)
    @classmethod
    def set(cls, data):
        resp3_set.parse_set(data)
    @classmethod
    def simple_error(cls, data):
        resp3_simple_error.parse_simple_error(data)
    @classmethod
    def simple_string(cls, data):
        resp3_simple_string.parse_simple_string(data)
    @classmethod
    def verbatim_string(cls, data):
        resp3_verbatim_string.parse_verbatim_string(data)
        
