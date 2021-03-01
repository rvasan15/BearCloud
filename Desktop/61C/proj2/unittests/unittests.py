from unittest import TestCase
from framework import AssemblyTest, print_coverage


class TestAbs(TestCase):
    def test_zero(self):
        t = AssemblyTest(self, "abs.s")
        # load 0 into register a0
        t.input_scalar("a0", 0)
        # call the abs function
        t.call("abs")
        # check that after calling abs, a0 is equal to 0 (abs(0) = 0)
        t.check_scalar("a0", 0)
        # generate the `assembly/TestAbs_test_zero.s` file and run it through venus
        t.execute()

    def test_one(self):
        # same as test_zero, but with input 1
        t = AssemblyTest(self, "abs.s")
        t.input_scalar("a0", 1)
        t.call("abs")
        t.check_scalar("a0", 1)
        t.execute()

    def test_negative_one(self):
        # same as test_zero, but with input -1
        t = AssemblyTest(self, "abs.s")
        t.input_scalar("a0", -1)
        t.call("abs")
        t.check_scalar("a0", 1)
        t.execute()

    def test_big_neg_number(self):
        # same as test_zero, but with input -1
        t = AssemblyTest(self, "abs.s")
        t.input_scalar("a0", -2147483648)
        t.call("abs")
        t.check_scalar("a0", 2147483648)
        t.execute()

    def test_big_pos_number(self):
        # same as test_zero, but with input -1
        t = AssemblyTest(self, "abs.s")
        t.input_scalar("a0", 2147483647)
        t.call("abs")
        t.check_scalar("a0", 2147483647)
        t.execute()

    @classmethod
    def tearDownClass(cls):
        print_coverage("abs.s", verbose=False)


class TestRelu(TestCase):

    def test_simple_2(self):
        t = AssemblyTest(self, "relu.s")
        # create an array in the data section
        array0 = t.array([1, -2])
        # load address of `array0` into register a0
        t.input_array("a0", array0)
        # set a1 to the length of our array
        t.input_scalar("a1", len(array0))
        # call the relu function
        t.call("relu")
        # check that the array0 was changed appropriately
        t.check_array(array0, [1, 0])
        # generate the `assembly/TestRelu_test_simple.s` file and run it through venus
        t.execute()

    def test_zero_length_input(self):
        t = AssemblyTest(self, "relu.s")
        # create an array in the data section
        array0 = t.array([1])
        # load address of `array0` into register a0
        t.input_array("a0", array0)
        # set a1 to the length of our array
        #t.input_scalar("a1", len(array0))
        t.input_scalar("a1", 0)
        # call the relu function
        t.call("relu")
        # check that the array0 was changed appropriately
        t.check_array(array0, [1])
        # generate the `assembly/TestRelu_test_simple.s` file and run it through venus
        t.execute(115)

    def test_simple(self):
        t = AssemblyTest(self, "relu.s")
        # create an array in the data section
        array0 = t.array([1, -2, 3, -4, 5, -6, 7, -8, 9])
        # load address of `array0` into register a0
        t.input_array("a0", array0)
        # set a1 to the length of our array
        t.input_scalar("a1", len(array0))
        # call the relu function
        t.call("relu")
        # check that the array0 was changed appropriately
        t.check_array(array0, [1, 0, 3, 0, 5, 0, 7, 0, 9])
        # generate the `assembly/TestRelu_test_simple.s` file and run it through venus
        t.execute()

    def test_big_array(self):
        t = AssemblyTest(self, "relu.s")
        # create an array in the data section
        array0 = t.array([0, 0, 0, 0, 0, 0, 1, -2, 3, -4, 5, -6, 7, -8, 9, 1, -2, 3, -4, 5, -6, 7, -8, 9, 1, -2, 3, -4, 5, -6, 7, -8, 9])
        # load address of `array0` into register a0
        t.input_array("a0", array0)
        # set a1 to the length of our array
        t.input_scalar("a1", len(array0))
        # call the relu function
        t.call("relu")
        # check that the array0 was changed appropriately
        t.check_array(array0, [0, 0, 0, 0, 0, 0, 1, 0, 3, 0, 5, 0, 7, 0, 9, 1, 0, 3, 0, 5, 0, 7, 0, 9, 1, 0, 3, 0, 5, 0, 7, 0, 9])
        # generate the `assembly/TestRelu_test_simple.s` file and run it through venus
        t.execute()

    def test_all_zeros(self):
        t = AssemblyTest(self, "relu.s")
        # create an array in the data section
        array0 = t.array([0, 0, 0, 0, 0, 0])
        # load address of `array0` into register a0
        t.input_array("a0", array0)
        # set a1 to the length of our array
        t.input_scalar("a1", len(array0))
        # call the relu function
        t.call("relu")
        # check that the array0 was changed appropriately
        t.check_array(array0, [0, 0, 0, 0, 0, 0])
        # generate the `assembly/TestRelu_test_simple.s` file and run it through venus
        t.execute()


    @classmethod
    def tearDownClass(cls):
        print_coverage("relu.s", verbose=False)


class TestArgmax(TestCase):
    def test_simple_2(self):
        t = AssemblyTest(self, "argmax.s")
        # create an array in the data section
        # raise NotImplementedError("TODO")
        # TODO
        array0 = t.array([1, -2, 9])
        # load address of the array into register a0
        # TODO
        t.input_array("a0", array0)
        # set a1 to the length of the array
        # TODO
        t.input_scalar("a1", len(array0))
        # call the `argmax` function
        # TODO
        t.call("argmax")
        # check that the register a0 contains the correct output
        # TODO
        t.check_scalar("a0", 2)
        # generate the `assembly/TestArgmax_test_simple.s` file and run it through venus
        t.execute()

    # tests for duplicate max
    def test_simple_3(self):
        t = AssemblyTest(self, "argmax.s")
        # create an array in the data section
        # raise NotImplementedError("TODO")
        # TODO
        array0 = t.array([1, 0, 1])
        # load address of the array into register a0
        # TODO
        t.input_array("a0", array0)
        # set a1 to the length of the array
        # TODO
        t.input_scalar("a1", len(array0))
        # call the `argmax` function
        # TODO
        t.call("argmax")
        # check that the register a0 contains the correct output
        # TODO
        t.check_scalar("a0", 0)
        # generate the `assembly/TestArgmax_test_simple.s` file and run it through venus
        t.execute()

    def test_simple_7(self):
        t = AssemblyTest(self, "argmax.s")
        # create an array in the data section
        # raise NotImplementedError("TODO")
        # TODO
        array0 = t.array([1, -2, 9, 0, 11, 0, 11])
        # load address of the array into register a0
        # TODO
        t.input_array("a0", array0)
        # set a1 to the length of the array
        # TODO
        t.input_scalar("a1", len(array0))
        # call the `argmax` function
        # TODO
        t.call("argmax")
        # check that the register a0 contains the correct output
        # TODO
        t.check_scalar("a0", 4)
        # generate the `assembly/TestArgmax_test_simple.s` file and run it through venus
        t.execute()

    def test_zero_length_input(self):
        t = AssemblyTest(self, "argmax.s")
        # create an array in the data section
        # raise NotImplementedError("TODO")
        # TODO
        array0 = t.array([1])
        # load address of the array into register a0
        # TODO
        t.input_array("a0", array0)
        # set a1 to the length of the array
        # TODO
        t.input_scalar("a1", 0)
        # call the `argmax` function
        # TODO
        t.call("argmax")
        # check that the register a0 contains the correct output
        # TODO
        t.check_scalar("a0", 1)
        # generate the `assembly/TestArgmax_test_simple.s` file and run it through venus
        t.execute(120)

    @classmethod
    def tearDownClass(cls):
        print_coverage("argmax.s", verbose=False)


class TestDot(TestCase):
    def test_simple(self):
        t = AssemblyTest(self, "dot.s")
        # create arrays in the data section
        #raise NotImplementedError("TODO")
        # TODO
        array0 = t.array([1, 2])
        array1 = t.array([1, 2])

        # load array addresses into argument registers
        # TODO
        t.input_array("a0", array0)
        t.input_array("a1", array1)

        # load array attributes into argument registers
        # TODO
        t.input_scalar("a2", len(array0))
        # load stride0
        t.input_scalar("a3", 1)
        # load stride1
        t.input_scalar("a4", 1)

        # call the `dot` function
        t.call("dot")
        # check the return value
        # TODO
        t.check_scalar("a0", 5)
        t.execute()

    def test_simple_1(self):
        t = AssemblyTest(self, "dot.s")
        # create arrays in the data section
        #raise NotImplementedError("TODO")
        # TODO
        array0 = t.array([1])
        array1 = t.array([1])

        # load array addresses into argument registers
        # TODO
        t.input_array("a0", array0)
        t.input_array("a1", array1)

        # load array attributes into argument registers
        # TODO
        t.input_scalar("a2", len(array0))
        # load stride0
        t.input_scalar("a3", 1)
        # load stride1
        t.input_scalar("a4", 1)

        # call the `dot` function
        t.call("dot")
        # check the return value
        # TODO
        t.check_scalar("a0", 1)
        t.execute()

    def test_simple_4_2(self):
        t = AssemblyTest(self, "dot.s")
        # create arrays in the data section
        #raise NotImplementedError("TODO")
        # TODO
        array0 = t.array([1, 2, 3, 4])
        array1 = t.array([1, 2, 3, 4])

        # load array addresses into argument registers
        # TODO
        t.input_array("a0", array0)
        t.input_array("a1", array1)

        # load array attributes into argument registers
        # TODO
        t.input_scalar("a2", len(array0))
        # load stride0
        t.input_scalar("a3", 1)
        # load stride1
        t.input_scalar("a4", 2)

        # call the `dot` function
        t.call("dot")
        # check the return value
        # TODO
        t.check_scalar("a0", 7)
        t.execute()

    def test_simple_3(self):
        t = AssemblyTest(self, "dot.s")
        # create arrays in the data section
        #raise NotImplementedError("TODO")
        # TODO
        array0 = t.array([1, 2, 3])
        array1 = t.array([1, 2, 3])

        # load array addresses into argument registers
        # TODO
        t.input_array("a0", array0)
        t.input_array("a1", array1)

        # load array attributes into argument registers
        # TODO
        t.input_scalar("a2", len(array0))
        # load stride0
        t.input_scalar("a3", 1)
        # load stride1
        t.input_scalar("a4", 1)

        # call the `dot` function
        t.call("dot")
        # check the return value
        # TODO
        t.check_scalar("a0", 14)
        t.execute()

    def test_simple_4(self):
        t = AssemblyTest(self, "dot.s")
        # create arrays in the data section
        #raise NotImplementedError("TODO")
        # TODO
        array0 = t.array([1, 2, 3, -2])
        array1 = t.array([1, 2, 3, 2])

        # load array addresses into argument registers
        # TODO
        t.input_array("a0", array0)
        t.input_array("a1", array1)

        # load array attributes into argument registers
        # TODO
        t.input_scalar("a2", len(array0))
        # load stride0
        t.input_scalar("a3", 1)
        # load stride1
        t.input_scalar("a4", 1)

        # call the `dot` function
        t.call("dot")
        # check the return value
        # TODO
        t.check_scalar("a0", 10)
        t.execute()

    def test_negative_4(self):
        t = AssemblyTest(self, "dot.s")
        # create arrays in the data section
        #raise NotImplementedError("TODO")
        # TODO
        array0 = t.array([1, 2, 3, -8])
        array1 = t.array([1, 2, 3, 2])

        # load array addresses into argument registers
        # TODO
        t.input_array("a0", array0)
        t.input_array("a1", array1)

        # load array attributes into argument registers
        # TODO
        t.input_scalar("a2", len(array0))
        # load stride0
        t.input_scalar("a3", 1)
        # load stride1
        t.input_scalar("a4", 1)

        # call the `dot` function
        t.call("dot")
        # check the return value
        # TODO
        t.check_scalar("a0", -2)
        t.execute()

    # test with stride value 2 for both strides and 4 elements in array
    def test_stride_2_2_4(self):
        t = AssemblyTest(self, "dot.s")
        # create arrays in the data section
        #raise NotImplementedError("TODO")
        # TODO
        array0 = t.array([1, 2, 3, 4])
        array1 = t.array([1, 2, 3, 4])

        # load array addresses into argument registers
        # TODO
        t.input_array("a0", array0)
        t.input_array("a1", array1)

        # load array attributes into argument registers
        # TODO
        t.input_scalar("a2", len(array0))
        # load stride0
        t.input_scalar("a3", 2)
        # load stride1
        t.input_scalar("a4", 2)

        # call the `dot` function
        t.call("dot")
        # check the return value
        # TODO
        t.check_scalar("a0", 10)
        t.execute()

    def test_length_error_4(self):
        t = AssemblyTest(self, "dot.s")
        # create arrays in the data section
        #raise NotImplementedError("TODO")
        # TODO
        array0 = t.array([])
        array1 = t.array([1, 2, 3, 4])

        # load array addresses into argument registers
        # TODO
        t.input_array("a0", array0)
        t.input_array("a1", array1)

        # load array attributes into argument registers
        # TODO
        t.input_scalar("a2", len(array0))
        # load stride0
        t.input_scalar("a3", 2)
        # load stride1
        t.input_scalar("a4", 2)

        # call the `dot` function
        t.call("dot")
        # check the return value
        # TODO
        t.check_scalar("a0", 10)
        t.execute(123)

    def test_stride_length_error_4(self):
        t = AssemblyTest(self, "dot.s")
        # create arrays in the data section
        #raise NotImplementedError("TODO")
        # TODO
        array0 = t.array([])
        array1 = t.array([1, 2, 3, 4])

        # load array addresses into argument registers
        # TODO
        t.input_array("a0", array0)
        t.input_array("a1", array1)

        # load array attributes into argument registers
        # TODO
        t.input_scalar("a2", len(array0))
        # load stride0
        t.input_scalar("a3", 0)
        # load stride1
        t.input_scalar("a4", 2)

        # call the `dot` function
        t.call("dot")
        # check the return value
        # TODO
        t.check_scalar("a0", 10)
        t.execute(123)

    def test_stride_length_error_4(self):
        t = AssemblyTest(self, "dot.s")
        # create arrays in the data section
        #raise NotImplementedError("TODO")
        # TODO
        array0 = t.array([1, 2, 3, 4])
        array1 = t.array([1, 2, 3, 4])

        # load array addresses into argument registers
        # TODO
        t.input_array("a0", array0)
        t.input_array("a1", array1)

        # load array attributes into argument registers
        # TODO
        t.input_scalar("a2", len(array0))
        # load stride0
        t.input_scalar("a3", 0)
        # load stride1
        t.input_scalar("a4", 2)

        # call the `dot` function
        t.call("dot")
        # check the return value
        # TODO
        t.check_scalar("a0", 10)
        t.execute(124)

    def test_diff_stride_length_4(self):
        t = AssemblyTest(self, "dot.s")
        # create arrays in the data section
        #raise NotImplementedError("TODO")
        # TODO
        array0 = t.array([1, 2, 3, 4])
        array1 = t.array([1, 2, 3, 4])

        # load array addresses into argument registers
        # TODO
        t.input_array("a0", array0)
        t.input_array("a1", array1)

        # load array attributes into argument registers
        # TODO
        t.input_scalar("a2", len(array0))
        # load stride0
        t.input_scalar("a3", 1)
        # load stride1
        t.input_scalar("a4", 2)

        # call the `dot` function
        t.call("dot")
        # check the return value
        # TODO
        t.check_scalar("a0", 7)
        t.execute()

    def test_diff_stride_length_2_4(self):
        t = AssemblyTest(self, "dot.s")
        # create arrays in the data section
        #raise NotImplementedError("TODO")
        # TODO
        array0 = t.array([1, 2, 3, 4])
        array1 = t.array([1, 2, 3, 4])

        # load array addresses into argument registers
        # TODO
        t.input_array("a0", array0)
        t.input_array("a1", array1)

        # load array attributes into argument registers
        # TODO
        t.input_scalar("a2", len(array0))
        # load stride0
        t.input_scalar("a3", 2)
        # load stride1
        t.input_scalar("a4", 1)

        # call the `dot` function
        t.call("dot")
        # check the return value
        # TODO
        t.check_scalar("a0", 7)
        t.execute()

    def test_diff_stride_equal_length_2_4(self):
        t = AssemblyTest(self, "dot.s")
        # create arrays in the data section
        #raise NotImplementedError("TODO")
        # TODO
        array0 = t.array([1, 2, 3, 4])
        array1 = t.array([1, 2, 3, 4])

        # load array addresses into argument registers
        # TODO
        t.input_array("a0", array0)
        t.input_array("a1", array1)

        # load array attributes into argument registers
        # TODO
        t.input_scalar("a2", len(array0))
        # load stride0
        t.input_scalar("a3", 1)
        # load stride1
        t.input_scalar("a4", 4)

        # call the `dot` function
        t.call("dot")
        # check the return value
        # TODO
        t.check_scalar("a0", 1)
        t.execute()

    def test_diff_stride_greaterthan_length_2_4(self):
        t = AssemblyTest(self, "dot.s")
        # create arrays in the data section
        #raise NotImplementedError("TODO")
        # TODO
        array0 = t.array([1, 2, 3, 4])
        array1 = t.array([1, 2, 3, 4])

        # load array addresses into argument registers
        # TODO
        t.input_array("a0", array0)
        t.input_array("a1", array1)

        # load array attributes into argument registers
        # TODO
        t.input_scalar("a2", len(array0))
        # load stride0
        t.input_scalar("a3", 1)
        # load stride1
        t.input_scalar("a4", 5)

        # call the `dot` function
        t.call("dot")
        # check the return value
        # TODO
        t.check_scalar("a0", 1)
        t.execute()



    @classmethod
    def tearDownClass(cls):
        print_coverage("dot.s", verbose=False)


class TestMatmul(TestCase):

    def do_matmul(self, m0, m0_rows, m0_cols, m1, m1_rows, m1_cols, result, code=0):
        t = AssemblyTest(self, "matmul.s")
        # we need to include (aka import) the dot.s file since it is used by matmul.s
        t.include("dot.s")

        # create arrays for the arguments and to store the result
        array0 = t.array(m0)
        array1 = t.array(m1)
        array_out = t.array([0] * len(result))

        # load address of input matrices and set their dimensions
        #raise NotImplementedError("TODO")
        # TODO
        t.input_array("a0", array0)
        t.input_scalar("a1", m0_rows)
        t.input_scalar("a2", m0_cols)

        t.input_array("a3", array1)
        t.input_scalar("a4", m1_rows)
        t.input_scalar("a5", m1_cols)

        # load address of output array
        # TODO
        t.input_array("a6", array_out)

        # call the matmul function
        t.call("matmul")

        # check the content of the output array
        # TODO
        t.check_array(array_out, result)

        # generate the assembly file and run it through venus, we expect the simulation to exit with code `code`
        t.execute(code=code)

    def test_simple_1_1_1_1(self):
        self.do_matmul(
            [1], 1, 1,
            [1], 1, 1,
            [1]
        )

    def test_simple_2_2_2_2(self):
        self.do_matmul(
            [1, 2, 3, 4], 2, 2,
            [1, 2, 3, 4], 2, 2,
            [7, 10, 15, 22]
        )

    def test_simple_2_2_2_2_identity_1(self):
        self.do_matmul(
            [1, 0, 0, 1], 2, 2,
            [1, 2, 3, 4], 2, 2,
            [1, 2, 3, 4]
        )

    def test_simple_2_2_2_2_identity_2(self):
        self.do_matmul(
            [1, 2, 3, 4], 2, 2,
            [1, 0, 0, 1], 2, 2,
            [1, 2, 3, 4]
        )

    def test_simple_2_2_2_2_transpose(self):
        self.do_matmul(
            [1, 2, 3, 4], 2, 2,
            [1, 3, 2, 4], 2, 2,
            [5, 11, 11, 25]
        )

    def test_simple_2_2_2_2_zero_1(self):
        self.do_matmul(
            [0, 0, 0, 0], 2, 2,
            [1, 2, 3, 4], 2, 2,
            [0, 0, 0, 0]
        )


    def test_simple_2_2_2_2_zero_2(self):
        self.do_matmul(
            [1, 2, 3, 4], 2, 2,
            [0, 0, 0, 0], 2, 2,
            [0, 0, 0, 0]
        )

    def test_big_10_10_10_10_identity_1(self):
        self.do_matmul(
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 10, 10,
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 10,
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        )


    def test_big_10_10_10_10_identity_2(self):
        self.do_matmul(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 10,
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 10, 10,
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        )


    def test_simple_2_2_2_1(self):
        self.do_matmul(
            [1, 2, 3, 4], 2, 2,
            [1, 3], 2, 1,
            [7, 15]
        )

    def test_simple_1_2_2_1(self):
        self.do_matmul(
            [1, 2], 1, 2,
            [1, 3], 2, 1,
            [7]
        )

    def test_simple_2_1_1_2(self):
        self.do_matmul(
            [1, 3], 2, 1,
            [1, 2], 1, 2,
            [1, 2, 3, 6]
        )

    def test_simple(self):
        self.do_matmul(
            [1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3,
            [1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3,
            [30, 36, 42, 66, 81, 96, 102, 126, 150]
        )

    def test_simple_negative(self):
        self.do_matmul(
            [1, 2, 3, -4, 5, 6, -7, 8, 9], 3, 3,
            [1, 2, 3, 4, -5, 6, 7, 8, -9], 3, 3,
            [30, 16, -12, 58, 15, -36, 88, 18, -54]
        )

    def test_m0_row_dimension(self):
        self.do_matmul(
            [1, 2, 3, -4, 5, 6, -7, 8, 9], 0, 3,
            [1, 2, 3, 4, -5, 6, 7, 8, -9], 3, 3,
            [30, 16, -12, 58, 15, -36, 88, 18, -54], 125
        )

    def test_m0_column_dimension(self):
        self.do_matmul(
            [1, 2, 3, -4, 5, 6, -7, 8, 9], 3, 0,
            [1, 2, 3, 4, -5, 6, 7, 8, -9], 3, 3,
            [30, 16, -12, 58, 15, -36, 88, 18, -54], 125
        )

    def test_m1_row_dimension(self):
        self.do_matmul(
            [1, 2, 3, -4, 5, 6, -7, 8, 9], 3, 3,
            [1, 2, 3, 4, -5, 6, 7, 8, -9], 0, 3,
            [30, 16, -12, 58, 15, -36, 88, 18, -54], 126
        )

    def test_m1_column_dimension(self):
        self.do_matmul(
            [1, 2, 3, -4, 5, 6, -7, 8, 9], 3, 3,
            [1, 2, 3, 4, -5, 6, 7, 8, -9], 3, 0,
            [30, 16, -12, 58, 15, -36, 88, 18, -54], 126
        )

    def test_m0_m1_match(self):
        self.do_matmul(
            [1, 2, 3, -4, 5, 6, -7, 8, 9], 3, 2,
            [1, 2, 3, 4, -5, 6, 7, 8, -9], 3, 3,
            [30, 16, -12, 58, 15, -36, 88, 18, -54], 127
        )



    @classmethod
    def tearDownClass(cls):
        print_coverage("matmul.s", verbose=False)


class TestReadMatrix(TestCase):

    def do_read_matrix(self, fail='', code=0):
        t = AssemblyTest(self, "read_matrix.s")
        # load address to the name of the input file into register a0
        t.input_read_filename("a0", "inputs/test_read_matrix/test_input.bin")
        #t.input_read_filename("a0", "/Users/rinivasan/desktop/61c/proj2/inputs/test_read_matrix/test_input.bin")

        # allocate space to hold the rows and cols output parameters
        rows = t.array([-1])
        cols = t.array([-1])

        # load the addresses to the output parameters into the argument registers
        #raise NotImplementedError("TODO")
        # TODO
        t.input_array("a1", rows)
        t.input_array("a2", cols)

        # call the read_matrix function
        t.call("read_matrix")

        #array_result = t.array([-1, -1, -1, -1, -1, -1, -1, -1])
        # check the output from the function
        # TODO
        t.check_array_pointer("a0", [1,2,3,4,5,6,7,8,9])
        t.check_array(rows, [3])
        t.check_array(cols, [3])

        # generate assembly and run it through venus
        t.execute(fail=fail, code=code)

    def test_simple(self):
        self.do_read_matrix()

    @classmethod
    def tearDownClass(cls):
        print_coverage("read_matrix.s", verbose=False)


class TestWriteMatrix(TestCase):

    def do_write_matrix(self, fail='', code=0):
        t = AssemblyTest(self, "write_matrix.s")
        outfile = "outputs/test_write_matrix/student.bin"
        # load output file name into a0 register
        t.input_write_filename("a0", outfile)
        # load input array and other arguments
        #raise NotImplementedError("TODO")
        # TODO
        elements = t.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
        t.input_array("a1", elements)
        t.input_scalar("a2", 3)
        t.input_scalar("a3", 3)

        # call `write_matrix` function
        t.call("write_matrix")
        # generate assembly and run it through venus
        t.execute(fail=fail, code=code)
        # compare the output file against the reference
        t.check_file_output(outfile, "outputs/test_write_matrix/reference.bin")

    def test_simple(self):
        self.do_write_matrix()

    @classmethod
    def tearDownClass(cls):
        print_coverage("write_matrix.s", verbose=False)


class TestClassify(TestCase):

    def make_test(self):
        t = AssemblyTest(self, "classify.s")
        t.include("argmax.s")
        t.include("dot.s")
        t.include("matmul.s")
        t.include("read_matrix.s")
        t.include("relu.s")
        t.include("write_matrix.s")
        return t

    def test_simple0_input0(self):
        t = self.make_test()
        out_file = "outputs/test_basic_main/student0.bin"
        ref_file = "outputs/test_basic_main/reference0.bin"
        args = ["inputs/simple0/bin/m0.bin", "inputs/simple0/bin/m1.bin",
                "inputs/simple0/bin/inputs/input0.bin", out_file]

        # args = ["src/test.S", "inputs/simple0/bin/m0.bin", "inputs/simple0/bin/m1.bin",
        #         "inputs/simple0/bin/inputs/input0.bin", out_file]
        
  
        # call classify function
        t.input_scalar("a2", 0)
        t.call("classify")

        # generate assembly and pass program arguments directly to venus
        t.execute(args=args)

        # compare the output file and
        #raise NotImplementedError("TODO")
        # TODO
        # compare the classification output with `check_stdout`
        t.check_file_output(out_file, ref_file)
        t.check_stdout("2")


    @classmethod
    def tearDownClass(cls):
        print_coverage("classify.s", verbose=False)


# The following are some simple sanity checks:
import subprocess, pathlib, os
script_dir = pathlib.Path(os.path.dirname(__file__)).resolve()

def compare_files(test, actual, expected):
    assert os.path.isfile(expected), f"Reference file {expected} does not exist!"
    test.assertTrue(os.path.isfile(actual), f"It seems like the program never created the output file {actual}!")
    # open and compare the files
    with open(actual, 'rb') as a:
        actual_bin = a.read()
    with open(expected, 'rb') as e:
        expected_bin = e.read()
    test.assertEqual(actual_bin, expected_bin, f"Bytes of {actual} and {expected} did not match!")

class TestMain(TestCase):
    """ This sanity check executes src/main.S using venus and verifies the stdout and the file that is generated.
    """

    def run_main(self, inputs, output_id, label):
        args = ["src/main.S", f"{inputs}/m0.bin", f"{inputs}/m1.bin",
                f"{inputs}/inputs/input0.bin",
                f"outputs/test_basic_main/student{output_id}.bin"]
        reference = f"outputs/test_basic_main/reference{output_id}.bin"

        # args = [f"{inputs}/m0.bin", f"{inputs}/m1.bin",
        #         f"{inputs}/inputs/input0.bin",
        #         f"outputs/test_basic_main/student{output_id}.bin"]
        # reference = f"outputs/test_basic_main/reference{output_id}.bin"

        # args = ["src/main.S", f"{inputs}/m0.bin", f"{inputs}/m1.bin",
        #         f"{inputs}/inputs/input0.bin",
        #         f"outputs/test_basic_main/student{output_id}.bin", "src/main.S"]
        # reference = f"outputs/test_basic_main/reference{output_id}.bin"



        t= AssemblyTest(self, "main.s", no_utils=True)
        t.call("main")
        t.execute(args=args)
        t.check_stdout(label)
        t.check_file_output(args[-1], reference)

    def test0(self):
        self.run_main("inputs/simple0/bin", "0", "2")

    def test1(self):
        self.run_main("inputs/simple1/bin", "1", "1")
