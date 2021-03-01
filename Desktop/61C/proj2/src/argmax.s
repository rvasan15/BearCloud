.globl argmax

.text
# =================================================================
# FUNCTION: Given a int vector, return the index of the largest
#	element. If there are multiple, return the one
#	with the smallest index.
# Arguments:
# 	a0 (int*) is the pointer to the start of the vector
#	a1 (int)  is the # of elements in the vector
# Returns:
#	a0 (int)  is the first index of the largest element
# Exceptions:
# - If the length of the vector is less than 1,
#   this function terminates the program with error code 120.
# =================================================================
argmax:

  # Prologue
  #ebreak
  addi sp  sp  -12
  sw s0  0(sp)
  sw s1  4(sp)
  sw ra  8(sp)

  #t0 : array index
  #t1 : temp to hold 1
  #t2 : content of array slots
  #t3 : max content
  #t4 : lowest index

  #s0 : a0 : begin of array addr
  #s1 : a1 : num slots in array


  add s0, a0, x0 # sets s0=a0
  add s1, a1, x0 # sets s1=a1

  li t0, 0 # sets array index = 0
  li t3, 0 # sets max = 0

  li t1, 1 # set t1=1
  bge s1, t1, loop_start # branch if s1>=1

arg_check:
  # exit with user defined error code
  li a1, 120 # set a1 = 120
  jal exit2 # call exit2 with error code

loop_start:
  lw t2, 0(s0) # set t2 = first element in s0 array
  blt t2, t3, after_max_update # if t2<t3, after_max_update

loop_continue:
  #ebreak
  beq t2, t3, after_max_update
  add t3, x0, t2
  add t4, x0, t0

after_max_update:    
  addi s0, s0, 4 # increment pointer to next element in s0 array
  addi t0, t0, 1 # increment array counter
  beq s1, t0, loop_end # if we have reached the total number of elements, go to loop_end
  j loop_start # start the loop again


loop_end:
  add a0, x0, t4

  # Epilogue
  lw s0  0(sp)
  lw s1  4(sp)
  lw ra  8(sp)
  addi sp  sp  12
   
  ret
