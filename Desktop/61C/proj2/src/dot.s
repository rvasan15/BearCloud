# //define t1 t1
# //define t2 t2
# //define t3 t3
# //define t4 t4

.globl dot

.text
# =======================================================
# FUNCTION: Dot product of 2 int vectors
# Arguments:
#   a0 (int*) is the pointer to the start of v0
#   a1 (int*) is the pointer to the start of v1
#   a2 (int)  is the length of the vectors
#   a3 (int)  is the stride of v0
#   a4 (int)  is the stride of v1
# Returns:
#   a0 (int)  is the dot product of v0 and v1
# Exceptions:
# - If the length of the vector is less than 1,
#   this function terminates the program with error code 123.
# - If the stride of either vector is less than 1,
#   this function terminates the program with error code 124.
# =======================================================
dot:
  
  # Prologue
  addi sp  sp  -24
  sw s0  0(sp)
  sw s1  4(sp)
  sw s2  8(sp)
  sw s3  12(sp)
  sw s4  16(sp)
  sw ra  20(sp)

  #t0 : array loop index
  #t1 : temp to hold 1
  #t2 : content of array1
  #t3 : content of array2
  #t4 : computes max of stride1 and stride2
  #t5 : max loop index
  #t6 : product of 2 elements from corresponding vectors
  #t1 : t1 : dot product
  #t2 : t2 : s0 index with stride
  #t3 : t3 : s1 index with stride
  #t4 : t4 : temp to hold 4

  #s0 : a0 : begin of array1 addr
  #s1 : a1 : begin of array2 addr
  #s2 : a2 : num slots in array
  #s3 : a3 : stride1
  #s4 : a4 : stride2


  add s0, a0, x0 # sets s0=a0
  add s1, a1, x0 # sets s1=a1
  add s2, a2, x0 # sets s2=a2
  add s3, a3, x0 # sets s3=a3
  add s4, a4, x0 # sets s4=a4

  li t0, 0 # sets array index = 0

  li t1, 1 # set t1=1
  # If the length of the vector is less than 1,
  # this function terminates the program with error code 123.
  #bge s2, t1, arg_check_stride1 # branch if s2>=1

  blt s2, t1, exit_arg_len
  blt s3, t1, exit_arg_stride
  blt s4, t1, exit_arg_stride

  #Reuse t1 for t1 dot product
  li t1, 0 
  # First set t4 to s3 assuming that is the max
  # If s3 > s4 branch to next set of instrs : loop start
  # Set t4 to s4
  
  #compute max stride in s3,s4
  add t4, x0, s3
  bge s3, s4, compute_max_loop
  add t4, x0, s4

compute_max_loop:
  # compute max loop index: n/max_stride
  div t5, s2, t4
  

loop_start:
  #load s0 and s1 content into temp registers
  lw t2, 0(s0) # set t2 to element in s0 array
  lw t3, 0(s1) # set t3 to element in s1 array

  #multiply two elems and add to dot product
  mul t6, t2, t3
  #add to dot product
  add t1, t1, t6

loop_continue: 
  li t4, 4

  #increment loop index by 1
  #Do this before moving s0 and s1 so that loop index alings to next slot
  addi t0, t0, 1 # increment array counter

  # compute s0 index accounting for stride_s0 and increment s0
  # index_s0 = 4 * array_loop_index * stride_s0
  add t2, x0, s3
  mul t2, t2, t4
  add s0, s0, t2 # increment pointer to next element in s0 array

  # compute s1 index accounting for stride_s1 and increment s1
  # index_s1 = 4 * array_loop_index * stride_s1
  add t2, x0, s4
  mul t2, t2, t4
  add s1, s1, t2 # increment pointer to next element in s1 array
  
  

  #Check for max loop index and exit loop if we reached end
  bge t0, t5, loop_end # if we have reached max elements possible for max stride, go to loop_end
  j loop_start # start the loop again


loop_end:
  #return dot product computed in t1
  add a0, x0, t1
  # Epilogue
  
  lw s0  0(sp)
  lw s1  4(sp)
  lw s2  8(sp)
  lw s3  12(sp)
  lw s4  16(sp)
  lw ra  20(sp)
  addi sp  sp  24

  ret

#Error processing
exit_arg_len:
  # exit with user defined error code
  li a1, 123 # set a1 = 123
  jal exit2 # call exit2 with error code

exit_arg_stride:
  # exit with user defined error code
  li a1, 124 # set a1 = 124
  jal exit2 # call exit2 with error code

 
