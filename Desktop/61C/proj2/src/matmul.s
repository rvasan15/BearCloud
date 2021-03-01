.globl matmul

.text
# =======================================================
# FUNCTION: Matrix Multiplication of 2 integer matrices
# 	d = matmul(m0, m1)
# Arguments:
# 	a0 (int*)  is the pointer to the start of m0 
#	a1 (int)   is the # of rows (height) of m0
#	a2 (int)   is the # of columns (width) of m0
#	a3 (int*)  is the pointer to the start of m1
# 	a4 (int)   is the # of rows (height) of m1
#	a5 (int)   is the # of columns (width) of m1
#	a6 (int*)  is the pointer to the the start of d
# Returns:
#	None (void), sets d = matmul(m0, m1)
# Exceptions:
#   Make sure to check in top to bottom order!
#   - If the dimensions of m0 do not make sense,
#     this function terminates the program with exit code 125.
#   - If the dimensions of m1 do not make sense,
#     this function terminates the program with exit code 126.
#   - If the dimensions of m0 and m1 don't match,
#     this function terminates the program with exit code 127.
# =======================================================
matmul:

  # Prologue
  #ebreak
  addi sp  sp  -52
  sw s0  0(sp)
  sw s1  4(sp)
  sw s2  8(sp)
  sw s3  12(sp)
  sw s4  16(sp)
  sw s5  20(sp)
  sw s6  24(sp)
  sw s7  28(sp)
  sw s8  32(sp)
  sw s9  36(sp)
  sw s10 40(sp)
  sw s11 44(sp)
  sw ra  48(sp)

  add s0, a0, x0 # sets s0 to pointer of m0
  add s1, a1, x0 # sets s1 to # of rows (height) of m0
  add s2, a2, x0 # sets s2 to # of columns (width) of m0
  add s3, a3, x0 # sets s3 to pointer to the start of m1
  add s4, a4, x0 # sets s4 to # of rows (height) of m1
  add s5, a5, x0 # sets s5 to # of columns (width) of m1
  add s6, a6, x0 # sets s6 to pointer to the the start of d

  # Error checks
  li s8, 1
  
  blt a1, s8, error_m0_dimension
  blt a2, s8, error_m0_dimension
  blt a4, s8, error_m1_dimension
  blt a5, s8, error_m1_dimension
  bne a2, a4, error_wrong_dimensions

  # reset the outer loop index
  li s8, 0


  #setup const 4 in temp variable
  li s11, 4
  
outer_loop_start:

  #compute number of bytes to move s0 based num cols of m0
  #s10 = s2 * 4
  mul s10, s2, s11

  
  #Set s7 to s3 as s7 will move forward for inner loop
  #and then reset to begin when next outer loop starts   
  add s7, s3, x0

  # reset the inner loop index 
  li s9, 0


inner_loop_start:

  #a0, a1, a2, a3, a4

  #Set fist array of dot to first matrix begin
  #and then increment s0 at end of first loop
  add a0, x0, s0

  #Set a2 to len of array 0, number of rows times number of cols of m1(a2 = s4 *s5)
  # add a2, s2, x0
  mul a2, s4, s5

  # set first stride is always 1 
  addi a3, x0, 1

  # set second stride to num cols of second matrix : m1
  add a4, s5, x0
  
  #Set second array to second matrix start
  add a1, x0, s7
  #ebreak
  jal ra dot
  #ebreak
  #save dot product to s6
  # add s6, a0, x0
  sw a0, 0(s6)


  # increment s6 by 4 as s6 is also a single dimenstional array
  # so all that we need to do is to go to the next slot of this array
  addi s6, s6, 4


  # increment s7 by 4
  addi s7, s7, 4

  addi s9, s9, 1 # increment array counter for inner loop

  # -If inner loop inx is >= second matrix num colums
  bge s9, s5, inner_loop_end 
  j inner_loop_start # start the loop again

inner_loop_end:

  #Move s0 to next row : s0 = s0 + 4*num_cols_m0 
  #update s0 to new row
  add s0, s0, s10 

  addi s8, s8, 1 # increment array counter for outer loop

  # -If outer loop inx is >= first matrix num rows
  bge s8, s1, outer_loop_end 
  j outer_loop_start # start the loop again

outer_loop_end:


  # Epilogue
  lw s0  0(sp)
  lw s1  4(sp)
  lw s2  8(sp)
  lw s3  12(sp)
  lw s4  16(sp)
  lw s5  20(sp)
  lw s6  24(sp)
  lw s7  28(sp)
  lw s8  32(sp)
  lw s9  36(sp)
  lw s10 40(sp)
  lw s11 44(sp)
  lw ra  48(sp)
  addi sp  sp  52
    
  ret

error_m0_dimension:
  # exit with user defined error code
  li a1, 125 # set a1 = 125
  jal exit2 # call exit2 with error code

error_m1_dimension:
  # exit with user defined error code
  li a1, 126 # set a1 = 126
  jal exit2 # call exit2 with error code

error_wrong_dimensions:
  # exit with user defined error code
  li a1, 127 # set a1 = 127
  jal exit2 # call exit2 with error code
