.globl write_matrix

.text
# ==============================================================================
# FUNCTION: Writes a matrix of integers into a binary file
# FILE FORMAT:
#   The first 8 bytes of the file will be two 4 byte ints representing the
#   numbers of rows and columns respectively. Every 4 bytes thereafter is an
#   element of the matrix in row-major order.
# Arguments:
#   a0 (char*) is the pointer to string representing the filename
#   a1 (int*)  is the pointer to the start of the matrix in memory
#   a2 (int)   is the number of rows in the matrix
#   a3 (int)   is the number of columns in the matrix
# Returns:
#   None
# Exceptions:
# - If you receive an fopen error or eof,
#   this function terminates the program with error code 112.
# - If you receive an fwrite error or eof,
#   this function terminates the program with error code 113.
# - If you receive an fclose error or eof,
#   this function terminates the program with error code 114.
# ==============================================================================
write_matrix:

  # Prologue
  #ebreak
  addi sp, sp, -32
  sw s0, 0(sp)
  sw s1, 4(sp)
  sw s2, 8(sp)
  sw s3, 12(sp)
  sw s4, 16(sp)
  sw ra, 20(sp)

  mv s0, a0
  mv s1, a1
  mv s2, a2
  mv s3, a3

  #Alloc more space on stack such that we do not overwrite the orignal s2,s3
  #that hold values from caller
  sw s2, 24(sp)
  sw s3, 28(sp)

  # set a1 to be filename for calling fopen
  mv a1, s0
  # set a2 = w
  addi a2, x0, 1
  jal fopen
  #ebreak

  addi t0, x0, -1
  bne a0, t0, write_rows_cols
  li a1, 112
  jal exit2

write_rows_cols:
  #save file descriptor returned by fopen into s4
  mv s4, a0
  mv a1, s4
  # a2 needs an address so we need to save numRows 
  # and numCols on the stack and use stack pointer as mem address
  # NOTE: We are writing both numRows and numCols together bc on the stack we store them as sp -24 and sp -28
  addi a2, sp, 24
  addi a3, x0, 2
  addi a4, x0, 4
  jal fwrite
  #ebreak

  addi t0, x0, -1
  bne a0, t0, write_content
  li a1, 113
  jal exit2
  

write_content:
  # num elements
  mul t5, s2, s3
  mv a1, s4
  add a2, x0, s1
  add a3, x0, t5
  addi a4, x0, 4
  jal fwrite
  #ebreak

  addi t0, x0, -1
  bne a0, t0, close_file
  li a1, 113
  jal exit2

close_file:
  mv a1, s4
  jal fclose
  #ebreak

  beq a0, x0, end_write_matrix
  li a1, 114
  jal exit2
  

end_write_matrix:
  # Epilogue

  lw s0, 0(sp)
  lw s1, 4(sp)
  lw s2, 8(sp)
  lw s3, 12(sp)
  lw s4, 16(sp)
  lw ra, 20(sp)

  addi sp, sp, 32

  ret
