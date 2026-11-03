# Capstone Project Report: Make the Computer Draw a Box
**Course:** Nand to Tetris – I (ETCCNT301)  
**Department:** School of Engineering & Technology, K.R. Mangalam University  
**Marks:** 10 | **Individual Work** | **Course Outcomes:** CO1–CO4  

---

### Student Details
- **Student Name:** Shivam Kumar Roy
- **Roll Number:** 2501010138
- **Personal Number \(K\):** `38` *(Last two digits of Roll Number: 2501010138)*
- **Calculations based on \(K = 38\):**
  - **\(K \pmod 3\):** \(38 \pmod 3 = 2\)  
    **Assigned Assembler Extra Feature:** *Print a warning if the same label is written twice.*
  - **\(K \pmod 4\):** \(38 \pmod 4 = 2\)  
  - **Box Position & Size:**
    - **Starting Row:** Row \(K = 38\)
    - **Height:** 20 rows (Rows 38 to 57 inclusive)
    - **Width:** \(16 \times ((K \pmod 4) + 1) = 16 \times (2 + 1) = 48\) pixels from the left edge.
    - **Screen Memory Words:** Hack display has 16 pixels per word. 48 pixels = 3 consecutive words (Word 0, Word 1, Word 2) at the start of each row.
    - **Base Address:** \(\text{SCREEN} + (32 \times 38) = 16384 + 1216 = \mathbf{17600}\).

---

## 1. Project Overview & System Architecture
The objective of this capstone project is to demonstrate mastery of the bottom-up computer system stack developed in Nand to Tetris (Part I):
1. **Part A (Hardware Layer):** Completing the 16-bit Von Neumann architecture by assembling `CPU.hdl`, `Memory.hdl`, and `Computer.hdl`.
2. **Part B (Software Translation Layer):** Developing an assembler in Python (`assembler.py`) that translates Hack assembly (`.asm`) into binary machine language (`.hack`), featuring symbol table resolution and duplicate label collision detection for \(K \pmod 3 = 2\).
3. **Part C (Application / Firmware Layer):** Writing an interactive graphics driver program (`Box.asm`) that responds in real-time to keyboard input, rendering a \(48 \times 20\) pixel black rectangle at Row 38 when a key is pressed, and clearing it when released.

---

## 2. Part A: Computer Construction & Hardware Verification

### 2.1 Memory Architecture (`Memory.hdl`)
The complete Hack memory space spans 32K 16-bit words (addresses `0x0000` to `0x7FFF`). `Memory.hdl` demultiplexes read and write operations across three physical regions:
- **Data RAM (`0x0000` – `0x3FFF`, 16,384 words):** Addressed when `address[14] == 0`. Implemented via `RAM16K(address=address[0..13])`.
- **Screen Memory Map (`0x4000` – `0x5FFF`, 8,192 words):** Addressed when `address[14..13] == 2'b10`. Maps directly to the 512×256 monochrome display. Implemented via `Screen(address=address[0..12])`.
- **Keyboard Register (`0x6000`, 1 word at address 24576):** Addressed when `address[14..13] == 2'b11`. Holds the ASCII code of the currently pressed key. Implemented via `Keyboard(out=outKbd)`.

Routing is performed using a `DMux4Way` on the `load` input controlled by `address[13..14]`, and a `Mux4Way16` selects the corresponding output.

### 2.2 CPU Implementation (`CPU.hdl`)
The Hack CPU incorporates an Arithmetic Logic Unit (ALU), two programmer-visible registers (`A` and `D`), and a Program Counter (`PC`):
- **Instruction Decoding:** Bit 15 differentiates between an A-instruction (`@value`, bit 15 = 0) and a C-instruction (`dest=comp;jump`, bit 15 = 1).
- **A-Register Logic:** Fed by a multiplexer selecting either the incoming raw instruction (for A-instructions) or the ALU computation output (for C-instructions with `d1 == 1`).
- **D-Register Logic:** Enabled strictly during C-instructions when destination bit `d2 == 1` (`instruction[4]`).
- **ALU Operation:** Operates on `D` as input X, and either `A` or `inM` (selected by the `a`-bit `instruction[12]`) as input Y, controlled by the six ALU control bits `instruction[6..11]`.
- **Branching / Program Counter:** Evaluates ALU output status flags `zr` (zero) and `ng` (negative) against jump bits `j1, j2, j3` (`instruction[0..2]`). If the condition is met and it is a C-instruction, `PC` asserts its `load` signal with the value of register `A`; otherwise, it increments sequentially.

### 2.3 Computer Integration (`Computer.hdl`)
Integrates the `CPU`, `Memory`, and `ROM32K` program storage:
- `ROM32K(address=pc, out=instruction)`
- `CPU(inM=inM, instruction=instruction, reset=reset, outM=outM, writeM=writeM, addressM=addressM, pc=pc)`
- `Memory(in=outM, load=writeM, address=addressM, out=inM)`

### 2.4 Official Test Results
All chips were tested using the official Nand to Tetris test scripts and comparison files:
1. `CPU.tst` / `CPU.cmp`: **PASS** (End of script - Comparison ended successfully)
2. `Memory.tst` / `Memory.cmp`: **PASS** (End of script - Comparison ended successfully)
3. `ComputerAdd.tst` / `ComputerAdd.cmp`: **PASS** (End of script - Comparison ended successfully)
4. `ComputerMax.tst` / `ComputerMax.cmp`: **PASS** (End of script - Comparison ended successfully)
5. `ComputerRect.tst` / `ComputerRect.cmp`: **PASS** (End of script - Comparison ended successfully)

*(Refer to `screenshot_tests.png` for hardware simulation test verification).*

---

## 3. Part B: Python Assembler Design & Extra Feature

### 3.1 Two-Pass Translation Algorithm
The assembler (`assembler.py`) performs two passes over the input Hack assembly source:
- **Pass 1 (Symbol Definition & Label Stripping):**
  - Strips inline comments (`//`) and whitespace.
  - Maintains a `rom_address` counter.
  - Identifies label definitions `(LABEL)` and records their mapping in the symbol table to `rom_address`.
  - **Extra Feature Implementation (\(K \pmod 3 = 2\)):** Tracks line occurrences of all labels. If a label is defined more than once, it emits a non-fatal warning indicating the line number of the duplicate definition and the line number of the original definition.
- **Pass 2 (Machine Code Generation):**
  - Translates A-instructions (`@val` / `@sym`): If numerical, encodes as `0` + 15-bit binary. If symbolic and not pre-existing, dynamically assigns memory in data RAM starting at address 16 onward (`R16`, `R17`, ...).
  - Translates C-instructions (`dest=comp;jump`): Looks up canonical binary encodings for computation (7 bits), destination (3 bits), and jump condition (3 bits), producing a full 16-bit binary word: `111 + comp + dest + jump`.
  - Exported symbol table to `symbols.txt` for transparent auditing.

### 3.2 Assembler Validation
The assembler was rigorously verified by compiling `Add.asm`, `Max.asm`, `Rect.asm`, and `Pong.asm`. The generated `.hack` output was verified byte-for-byte against the official Nand to Tetris assembler.

---

## 4. Part C: The Box Program (`Box.asm`)

### 4.1 Specification and Coordinate Mapping
The Hack screen consists of a \(512 \times 256\) monochrome pixel display mapped to RAM addresses `16384` to `24575`.
- Each row contains 512 pixels \(= 32\) 16-bit words (\(32 \times 16 = 512\)).
- Row \(r\) starts at memory address:  
  \[
  \text{RowStart}(r) = \text{SCREEN} + 32 \times r = 16384 + 32r
  \]
- For Roll Number ending in 38 (\(K = 38\)):
  - **Start Row:** 38 \(\implies \text{Address} = 16384 + (32 \times 38) = 17600\).
  - **Height:** 20 rows (Rows 38 to 57).
  - **Width:** \(16 \times ((38 \pmod 4) + 1) = 48\) pixels \(= 3\) consecutive words from the left edge (columns 0, 1, 2).
  - Each word written is `-1` (`0xFFFF`, all 16 pixels black) when a key is pressed, or `0` (`0x0000`, white) when released.

### 4.2 Control Flow & Memory Access
```
               +---------------------------+
               |         MAIN_LOOP         |
               | Poll Keyboard (RAM[KBD])  |
               +-------------+-------------+
                             |
             +---------------+---------------+
             |                               |
       [KBD != 0]                        [KBD == 0]
             |                               |
    +--------v--------+             +--------v--------+
    |  KEY_PRESSED    |             |  KEY_RELEASED   |
    | color = -1 (BLK)|             | color = 0 (WHT) |
    +--------+--------+             +--------+--------+
             |                               |
             +---------------+---------------+
                             |
                             v
               +---------------------------+
               |         DRAW_INIT         |
               | addr = 17600 (Row 38)     |
               | rows_left = 20            |
               +-------------+-------------+
                             |
                             v
               +---------------------------+
       +------>|         ROW_LOOP          |
       |       | Check: rows_left == 0?    |--[YES]--> (Return to MAIN_LOOP)
       |       +-------------+-------------+
       |                     | [NO]
       |       +-------------v-------------+
       |       | RAM[addr]   = color (W0)  |
       |       | RAM[addr+1] = color (W1)  |
       |       | RAM[addr+2] = color (W2)  |
       |       | addr = addr + 30 (NextRow)|
       |       | rows_left = rows_left - 1 |
       |       +-------------+-------------+
       +---------------------+
```

*(Refer to `screenshot_box.png` for CPU Emulator execution showing the rendered box).*

---

## 5. One Mistake I Encountered and How I Fixed It
During the development and testing of `Box.asm` and `assembler.py`, a subtle syntax error occurred in the row-stride address update step:
```asm
    @30
    D=A
    @addr
    M=M+D    // Syntax Error
```
When running the assembler, it failed with the message:  
`Error: Line 97: invalid comp expression 'M+D' in instruction 'M=M+D'`.

**Root Cause:**  
In the official Hack ALU instruction specification, addition between the `D` register and a memory operand `M` is formally encoded as `D+M` (`c1..c6 = 000010` with `a = 1`). While mathematically addition is commutative (\(M + D = D + M\)), the standard Hack ALU hardware specifically decodes input X as `D` and input Y as `M`, making `D+M` the canonical assembly syntax.

**Fix Applied:**
1. In `Box.asm`, the instruction was corrected to `M=D+M`, which strictly complies with the standard Hack instruction set.
2. Furthermore, in `assembler.py`, commutative comp mappings (e.g. `M+D`, `A+D`, `M&D`, `A&D`, `M|D`, `A|D`) were added to the internal lookup dictionary. This ensures that the assembler is robust, tolerant to alternate operand ordering, and conforms to both strict and lenient assembly conventions.

---

## 6. Conclusion
The complete system—from transistor logic gates and CPU datapath up to a custom two-pass Python assembler and interactive graphics firmware—was successfully designed, built, and validated. The final program executes correctly in the CPU Emulator, meeting all criteria for \(K = 38\).
