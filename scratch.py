from app.element_parsers.resp3_array import test_array
from app.element_parsers.resp3_attribute import test_attribute
from app.element_parsers.resp3_bignum import test_bignum
from app.element_parsers.resp3_boolean import test_boolean
from app.element_parsers.resp3_bulk_error import test_bulk_error
from app.element_parsers.resp3_bulk_string import test_bulk_string
from app.element_parsers.resp3_double import test_double
from app.element_parsers.resp3_integer import test_integer
from app.element_parsers.resp3_map import test_map
from app.element_parsers.resp3_null import test_null
from app.element_parsers.resp3_push import test_push
from app.element_parsers.resp3_set import test_set
from app.element_parsers.resp3_simple_error import test_simple_error
from app.element_parsers.resp3_simple_string import test_simple_string
from app.element_parsers.resp3_verbatim_string import test_verbatim_string

if __name__ == "__main__":
    test_array()
    test_attribute()
    test_bignum()
    test_boolean()
    test_bulk_error()
    test_bulk_string()
    test_double()
    test_integer()
    test_map()
    test_null()
    test_push()
    test_set()
    test_simple_error()
    test_simple_string()
    test_verbatim_string()

