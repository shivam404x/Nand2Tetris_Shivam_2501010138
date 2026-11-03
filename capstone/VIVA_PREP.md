# Capstone Viva Preparation Guide (5 Minutes Viva)
**Subject:** Nand to Tetris – I (ETCCNT301)  
**Student:** Shivam Kumar Roy | **Roll No:** 2501010138 | **K = 38**

---

## 1. The "On-The-Spot" Code Change Questions

### Question 1: "Make a change to move the box down by 5 rows (or N rows)."
**Answer & Quick Change:**
- In `Box.asm`, find line where start address is defined:
  ```asm
  (DRAW_INIT)
      @17600      // Starting address for row 38
      D=A
      @addr
      M=D
  ```
- **Calculation:** Each row on screen has 32 words.
  - Moving down by 5 rows means adding \(5 \times 32 = 160\) words.
  - New start address = \(17600 + 160 = \mathbf{17760}\).
- **Exact modification:** Simply change `@17600` to `@17760`!
  Then re-run:
  ```bash
  python assembler.py Box.asm
  ```
  Load the new `Box.hack` in CPU Emulator and run. The box now appears 5 rows lower (Row 43).

---

### Question 2: "Make the box taller (e.g., 30 rows instead of 20)."
**Answer & Quick Change:**
- In `Box.asm`, find the row counter in `DRAW_INIT`:
  ```asm
      @20         // Height: 20 rows
      D=A
      @rows_left
      M=D
  ```
- **Exact modification:** Change `@20` to `@30` (or whatever height requested).

---

### Question 3: "Make the box wider (e.g., 4 words / 64 pixels instead of 3 words / 48 pixels)."
**Answer & Quick Change:**
- In `ROW_LOOP`, add one more word write:
  ```asm
      // Word 3
      @addr
      M=M+1
      @color
      D=M
      @addr
      A=M
      M=D
  ```
- And adjust the row stride offset to reach the next row:
  - Previously we advanced by 2 words, so stride was `@30` (\(2 + 30 = 32\)).
  - Now we advance by 3 words, so stride becomes `@29` (\(3 + 29 = 32\)).

---

### Question 4: "Make the box appear by default, and disappear when a key is pressed (inverted behavior)."
**Answer & Quick Change:**
- In `MAIN_LOOP`:
  - Change `@KEY_PRESSED; D;JNE` to `D;JEQ` (or swap `-1` and `0` in `color`).

---

## 2. Fundamental Technical Viva Questions & Answers

### Q1: How does Hack CPU handle instructions?
- **A-instruction (`@value`):** Has MSB `0`. The 15 remaining bits are a constant loaded into the A register. It can represent a data constant, a RAM address, or a ROM jump address.
- **C-instruction (`dest=comp;jump`):** Has MSB `1`. Format is `111 a cccccc ddd jjj`.
  - `a` + 6 `c`-bits dictate the ALU operation (whether Y input is `A` or `M`).
  - 3 `d`-bits determine destination registers: `d1` -> A, `d2` -> D, `d3` -> M (`writeM`).
  - 3 `j`-bits test ALU flags `zr` and `ng` to trigger conditional branch (`PC = A`).

### Q2: What is Memory-Mapped I/O in Hack?
- Hack does not use specialized I/O instructions like `IN`/`OUT`. Instead, I/O devices are mapped directly into the RAM address space:
  - **Screen:** RAM addresses `16384` to `24575` (`0x4000` to `0x5FFF`, 8K words). Writing `-1` turns 16 pixels black; writing `0` turns them white.
  - **Keyboard:** RAM address `24576` (`0x6000`, 1 word). Reads the ASCII code of whichever key is pressed (or `0` if idle).

### Q3: How does the two-pass assembler work?
- **Pass 1:** Scans the code line-by-line ignoring comments and whitespace, keeping track of the ROM instruction index. When a pseudo-instruction label like `(LOOP)` is encountered, it records `LOOP -> current_rom_address` in the symbol table. It also checks if the label was already recorded to fire the duplicate warning (for \(K \pmod 3 = 2\)).
- **Pass 2:** Re-scans the code. Numerical `@values` are translated to binary. Symbolic variables (like `@color`, `@addr`) not previously encountered are assigned sequential RAM addresses starting at `16`. C-instructions are decomposed into `dest`, `comp`, and `jump` substrings and mapped to 16-bit binary codes.

### Q4: Why did we advance by 30 words in `Box.asm` instead of 32?
- Each screen line is 32 words wide.
- In each row of our box, we write Word 0, increment `addr` by 1 to write Word 1, and increment `addr` by 1 to write Word 2.
- At that point, `addr` is already advanced by 2 from the start of the row.
- To reach the start of the next row (offset +32), we add \(32 - 2 = 30\) words.

### Q5: What is the purpose of `writeM` in `CPU.hdl`?
- `writeM` is the load/enable signal sent from the CPU to the RAM.
- It is asserted (`1`) only when executing a C-instruction where destination includes `M` (`instruction[3] == 1` and `instruction[15] == 1`).
