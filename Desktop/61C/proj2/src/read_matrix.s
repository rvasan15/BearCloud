.globl read_matrix

.text
# ==============================================================================
# FUNCTION: Allocates memory and reads in a binary file as a matrix of integers
#
# FILE FORMAT:
#   The first 8 bytes are two 4 byte ints representing the # of rows and columns
#   in the matrix. Every 4 bytes afterwards is an element of the matrix in
#   row-major order.
# Arguments:
#   a0 (char*) is the pointer to string representing the filename
#   a1 (int*)  is a pointer to an integer, we will set it to the number of rows
#   a2 (int*)  is a pointer to an integer, we will set it to the number of columns
# Returns:
#   a0 (int*)  is the pointer to the matrix in memory
# Exceptions:
# - If malloc returns an error,
#   this function terminates the program with error code 116.
# - If you receive an fopen error or eof, 
#   this function terminates the program with error code 117.
# - If you receive an fread error or eof,
#   this function terminates the program with error code 118.
# - If you receive an fclose error or eof,
#   this function terminates the program with error code 119.
# ==============================================================================
read_matrix:

  # Prologue

  #ebreak
  addi sp, sp, -28
  sw s0, 0(sp)
  sw s1, 4(sp)
  sw s2, 8(sp)
  sw s3, 12(sp)
  sw s4, 16(sp)
  sw s5, 20(sp)
  sw ra, 24(sp)

  mv s0, a0 # sets s0 to the pointer to string representing the filename
  #IMPORTANT_NOTE
  #Setting s1 and s2 to a1 and a2 implies that fread will write num_rows
  #and num_cols directly into passed addresses
  #Thus we do not have to set values into passed addresses corr. to a1 and a2
  #at the end of this function
  mv s1, a1 # sets s1 to the number of rows
  mv s2, a2 # sets s2 to the number of columns
 
 # set a1 to be filename for calling fopen
  mv a1, s0
  # set a2 = r
  addi a2, x0, 0
  jal fopen
  #ebreak
  
  addi t0, x0, -1
  bne a0, t0, read_file_num_rows
  li a1, 117
  jal exit2



read_file_num_rows:

#save file descriptor returned by fopen into s3
  mv s3, a0
#Read num rows
  #ebreak
  mv a1, s3
  mv a2, s1
  addi a3, x0, 4
  jal fread
  #ebreak
  
  addi t4, x0, 4

  beq a0, t4, read_file_num_cols
  li a1, 118
  jal exit2

read_file_num_cols:
#Read num cols
  mv a1, s3     
  mv a2, s2
  addi a3, x0, 4
  jal fread
  #ebreak

  addi t4, x0, 4

  beq a0, t4, malloc_elements
  li a1, 118
  jal exit2


malloc_elements:
  
  # load contents of addresses pointed to by s1 and s2 that hold num rows and num cols
  lw t1, 0(s1)
  lw t2, 0(s2)

  #compute num bytes to read : num_rows*num_cols
  #s4 : total number of bytes
  li t4, 4
  mul s4, t1, t2
  mul s4, s4, t4
  
  mv a0, s4
  jal malloc
  #ebreak

  # s5 holds return address of malloc
  mv s5, a0
  addi t0, x0, 0
  bne a0, t0, read_matrix_contents
  li a1, 116
  jal exit2

read_matrix_contents:
# Read matrix contents
  mv a1, s3
  mv a2, s5
  add a3, x0, s4
  jal fread
  #ebreak
  
  beq a0, s4, close_file
  li a1, 118
  jal exit2
  
close_file:
  mv a1, s3
  jal fclose

  beq a0, x0, end_read_matrix
  li a1, 119
  jal exit2

end_read_matrix:

  #return address of malloced buffer that is filled in with read element values
  mv a0, s5

  # ebreak
  # lw t1, 0(a0)
  # lw t1, 4(a0)
  # lw t1, 8(a0)
  # lw t1, 12(a0)
  # lw t1, 16(a0)
  # lw t1, 20(a0)
  # lw t1, 24(a0)
  # lw t1, 28(a0)
  # lw t1, 32(a0)

  # lw t2, 0(s2)

  # Epilogue
  lw s0, 0(sp)
  lw s1, 4(sp)
  lw s2, 8(sp)
  lw s3, 12(sp)
  lw s4, 16(sp)
  lw s5, 20(sp)
  lw ra, 24(sp)
  addi sp, sp, 28


  ret


