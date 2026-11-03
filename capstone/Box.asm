// Box.asm
// Capstone Project: Make the Computer Draw a Box
// Nand to Tetris - I (ETCCNT301)
// School of Engineering & Technology, K.R. Mangalam University
//
// Student Name: Shivam Kumar Roy
// Roll Number:  2501010138
// Personal Number K: 38 (last two digits of roll number)
//
// Box Specifications for K = 38:
// - Start Row: K = 38
// - Height: 20 rows (Row 38 to Row 57)
// - Width: 16 * ((38 mod 4) + 1) = 16 * (2 + 1) = 48 pixels
//   (which equals 3 words of 16 bits each per row, starting from left edge)
// - Start Address in Screen Memory:
//     SCREEN + 32 * K = 16384 + (32 * 38) = 16384 + 1216 = 17600
//
// Operation:
// - Continuously checks keyboard input (RAM[24576] / KBD).
// - If any key is pressed (KBD != 0): fills the 48x20 box with black (-1).
// - If no key is pressed (KBD == 0): clears the 48x20 box to white (0).

(MAIN_LOOP)
    // Read the keyboard register
    @KBD
    D=M

    // If D != 0, a key is pressed -> set color to black (-1)
    @KEY_PRESSED
    D;JNE

    // Otherwise, key is released -> set color to white (0)
    @color
    M=0
    @DRAW_INIT
    0;JMP

(KEY_PRESSED)
    // Set color to -1 (16 bits of 1s = black)
    @color
    M=-1

(DRAW_INIT)
    // Initialize addr pointer to start of box: SCREEN + 32 * 38 = 17600
    @17600
    D=A
    @addr
    M=D

    // Initialize row counter: 20 rows to draw
    @20
    D=A
    @rows_left
    M=D

(ROW_LOOP)
    // Check if all 20 rows are completed
    @rows_left
    D=M
    @MAIN_LOOP
    D;JEQ          // If rows_left == 0, go back to main loop to poll keyboard

    // Fetch the current fill color (-1 or 0)
    @color
    D=M

    // Word 0 of current row (pixels 0-15)
    @addr
    A=M
    M=D

    // Move to Word 1 of current row (pixels 16-31)
    @addr
    M=M+1
    @color
    D=M
    @addr
    A=M
    M=D

    // Move to Word 2 of current row (pixels 32-47)
    @addr
    M=M+1
    @color
    D=M
    @addr
    A=M
    M=D

    // Advance addr to the start of the next row.
    // Screen width is 32 words per row.
    // We already moved addr forward by 2 words (from word 0 to word 2).
    // Therefore, adding 30 words moves addr to word 0 of the next row (2 + 30 = 32).
    @30
    D=A
    @addr
    M=D+M

    // Decrement the row counter
    @rows_left
    M=M-1

    // Repeat for the next row
    @ROW_LOOP
    0;JMP
