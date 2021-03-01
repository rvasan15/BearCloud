.globl relu

.text
# ==============================================================================
# FUNCTION: Performs an inplace element-wise ReLU on an array of ints
# Arguments:
# 	a0 (int*) is the pointer to the array
#	a1 (int)  is the # of elements in the array
# Returns:
#	None
# Exceptions:
# - If the length of the vector is less than 1,
#   this function terminates the program with error code 115.
# ==============================================================================
relu:
    # Prologue
	#ebreak
  addi sp  sp  -12
  sw s0  0(sp)
  sw s1  4(sp)
  sw ra  8(sp)

  add s0, a0, x0 # sets s0=a0
  add s1, a1, x0 # sets s1=a1
  li t0, 0 # sets array counter = 0

  li t1, 1 # set t1=1
  #bge s1, t1, loop_start # branch if s1>=1
  blt s1, t1, exit_arg_len

# exit_arg_len:
# 	  # exit with user defined error code
# 	  li a1, 115 # set a1 = 115
# 	  jal exit2 # call exit2 with error code 115

loop_start:

    lw t2, 0(s0) # set t2 = first element in s0 array
    bge t2, x0, loop_continue # if t2>=0, loop_continue
    sw x0, 0(s0) # else set the negative element to 0


loop_continue:

	addi s0, s0, 4 # increment pointer to next element in s0 array
	addi t0, t0, 1 # increment array counter
	beq s1, t0, loop_end # if we have reached the total number of elements, go to loop_end
	j loop_start # start the loop again


loop_end:

  # Epilogue
  lw s0  0(sp)
  lw s1  4(sp)
  lw ra  8(sp)
  addi sp  sp  12
  ret
  
exit_arg_len:
  # exit with user defined error code
  li a1, 115 # set a1 = 115
  jal exit2 # call exit2 with error code 115
   
