.globl classify

.text
classify:
    # =====================================
    # COMMAND LINE ARGUMENTS
    # =====================================
    # Args:
    #   a0 (int)    argc
    #   a1 (char**) argv
    #   a2 (int)    print_classification, if this is zero, 
    #               you should print the classification. Otherwise,
    #               this function should not print ANYTHING.
    # Returns:
    #   a0 (int)    Classification
    # Exceptions:
    # - If there are an incorrect number of command line args,
    #   this function terminates the program with exit code 121.
    # - If malloc fails, this function terminats the program with exit code 122.
    #
    # Usage:
    #   main.s <M0_PATH> <M1_PATH> <INPUT_PATH> <OUTPUT_PATH>


      # Prologue
      ebreak
      addi sp, sp, -48
      sw s0, 0(sp)  #a0
      sw s1, 4(sp)  #a1
      sw s2, 8(sp)  #a2
      sw s3, 12(sp) #m0 address
      sw s4, 16(sp) #m1 address
      sw s5, 20(sp) #input address
      sw s6, 24(sp) #numRowColumn array address 
      sw s7, 28(sp) #output of m0*input
      sw s8, 32(sp) # holds scores matrix: m1*hidden_layer
      sw s9, 36(sp) # argmax output
      sw s10, 40(sp) # num elements in m0*input
      sw ra, 44(sp)

      mv s0, a0
      mv s1, a1
      mv s2, a2


      addi t5, x0, 5
      beq s0, t5, load_matrices
      li a1, 121
      jal exit2


	# =====================================
    # LOAD MATRICES
    # =====================================
load_matrices:
    #Alloc space for 3 matrices row,col values
    addi a0, x0, 24
    jal malloc
    #ebreak

    # s6 holds return address of malloc
    mv s6, a0
    #la s6 a0
    addi t0, x0, 0
    bne a0, t0, read_matrix_m0
    li a1, 122
    jal exit2

read_matrix_m0:
    # Load pretrained m0
    # Get filename of m0 matrix from argv
    lw a0, 4(s1)
    mv a1 s6
    addi t6, s6, 4
    mv a2 t6
    jal read_matrix
    mv s3, a0
    #ebreak
    
    # lw t0, 0(s6)
    # lw t1, 4(s6)

    # Load pretrained m1
    lw a0, 8(s1)
    addi t6, s6, 8
    mv a1, t6
    addi t6, s6, 12
    mv a2, t6
    jal read_matrix
    mv s4, a0
    #ebreak

    # lw t0, 8(s6)
    # lw t1, 12(s6)

    # Load input matrix
    lw a0, 12(s1)
    addi t6, s6, 16
    mv a1, t6
    addi t6, s6, 20
    mv a2, t6
    jal read_matrix
    mv s5, a0
    #ebreak

    # lw t0, 16(s6)
    # lw t1, 20(s6)


    # =====================================
    # RUN LAYERS
    # =====================================
    # 1. LINEAR LAYER:    m0 * input
    # 2. NONLINEAR LAYER: ReLU(m0 * input)
    # 3. LINEAR LAYER:    m1 * ReLU(m0 * input)
run_layers:

#hidden_layer = matmul(m0, input)
#API from matmul
#   a0 (int*)  is the pointer to the start of m0 
#   a1 (int)   is the # of rows (height) of m0
#   a2 (int)   is the # of columns (width) of m0
#   a3 (int*)  is the pointer to the start of m1
#   a4 (int)   is the # of rows (height) of m1
#   a5 (int)   is the # of columns (width) of m1
#   a6 (int*)  is the pointer to the the start of d

    # allocate space for a6
    # numRows of m0
    lw t5 0(s6)
    # numCols of input
    lw t6 20(s6)
    # num elements in m0 * input 
    mul s10, t5, t6
    li t4, 4
    mul t5, s10, t4
    mv a0, t5
    jal malloc
	#ebreak
    
    mv s7, a0
    addi t0, x0, 0
    bne a0, t0, matmul_m0_input
    li a1, 122
    jal exit2

matmul_m0_input:
    mv a0, s3
    lw a1, 0(s6)
    lw a2, 4(s6)

    mv a3, s5
    lw a4, 16(s6)
    lw a5, 20(s6)

    mv a6, s7
    jal matmul
    #ebreak

#relu(hidden_layer) # Recall that relu is performed in-place
relu_hidden_layer:
    mv a0, s7
    mv a1, s10
    jal relu
    #ebreak

#scores = matmul(m1, hidden_layer)
scores_matrix:
    # allocate space for a6
    # numRows of m1
    lw t5 8(s6)
    # numCols of input:hidden_layer
    lw t6 20(s6)
    # num elements in m1 * hidden_layer 
    mul s10, t5, t6
    li t4, 4
    mul t5, s10, t4
    mv a0, t5
    jal malloc
    #ebreak

    mv s8, a0
    addi t0, x0, 0
    bne a0, t0, matmul_m1_hidden_layer
    li a1, 122
    jal exit2

matmul_m1_hidden_layer:
    mv a0, s4
    lw a1, 8(s6)
    lw a2, 12(s6)

    mv a3, s7
    lw a4, 0(s6)
    lw a5, 20(s6)

    mv a6, s8
    jal matmul
    #ebreak
 


    # =====================================
    # WRITE OUTPUT
    # =====================================
    # Write output matrix
# write_matrix API
#   a0 (char*) is the pointer to string representing the filename
#   a1 (int*)  is the pointer to the start of the matrix in memory
#   a2 (int)   is the number of rows in the matrix
#   a3 (int)   is the number of columns in the matrix
    
    lw a0 16(s1)
    mv a1, s8
    lw a2 8(s6) 
    lw a3 20(s6)
    jal write_matrix
    #ebreak


    # =====================================
    # CALCULATE CLASSIFICATION/LABEL
    # =====================================
    # Call argmax
# Argmax API
#   a0 (int*) is the pointer to the start of the vector
#   a1 (int)  is the # of elements in the vector
# Returns:
#   a0 (int)  is the first index of the largest element

    mv a0, s8
    # num_elems : m1_rows * input_cols
    # numRows of m1
    lw t5 8(s6)
    # numCols of input:hidden_layer
    lw t6 20(s6)
    mul a1, t5, t6
    jal argmax
    #ebreak

    mv s9, a0


    # Print classification
    bne s2, x0, end_classify
    mv a1, s9
    jal print_int
    #ebreak

    # Print newline afterwards for clarity
    li a1, 10
    jal print_char
    #ebreak

end_classify:

    mv a0, s3
    jal free
    ebreak

    mv a0, s4
    jal free
    ebreak

    mv a0, s5
    jal free
    ebreak

    # Free allocated memory for rowColumn Array
    mv a0, s6
    jal free
    ebreak

    # la a1 dbgstr_nba
    # jal print_str
    # li a0, 0
    # jal num_alloc_blocks
    # jal print_num_alloc_blocks

    mv a0, s7
    jal free
    ebreak

    # la a1 dbgstr_nba
    # jal print_str
    # li a0, 0
    # jal num_alloc_blocks
    # jal print_num_alloc_blocks
    
    mv a0, s8
    jal free
    ebreak

    # Epilogue

    lw s0, 0(sp)
    lw s1, 4(sp)
    lw s2, 8(sp)
    lw s3, 12(sp)
    lw s4, 16(sp)
    lw s5, 20(sp)
    lw s6, 24(sp)
    lw s7, 28(sp) 
    lw s8, 32(sp) 
    lw s9, 36(sp)
    lw s10, 40(sp)
    lw ra, 44(sp)

    addi sp, sp, 48

    
    ret
