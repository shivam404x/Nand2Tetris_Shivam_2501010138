# Part B – Python Assembler
**Nand to Tetris – I (ETCCNT301) Capstone Project**  
School of Engineering & Technology, K.R. Mangalam University  
**Student:** Shivam Kumar Roy | **Roll No:** 2501010138 | **K = 38**  

---

## Overview
Part B implements a two-pass assembler in Python (`assembler.py`) that translates symbolic Hack assembly programs (`.asm`) into binary machine language (`.hack`).

### Personal Number & Extra Feature:
- Roll Number: `2501010138` \(\rightarrow\) **K = 38**
- **K mod 3:** \(38 \pmod 3 = 2\)
- **Assigned Feature:** **Print a warning if the same label is written twice.**
  - If a label like `(LOOP)` is declared more than once in the source file, the assembler prints a non-fatal warning indicating the line number:
    ```text
    Warning (Line 7): Duplicate label '(LOOP)' defined! First defined at line 4.
    ```

---

## Files in this Directory
- `assembler.py` – Complete two-pass Python assembler
- `symbols.txt` – Exported symbol table

### Official Benchmark Programs:
- `Add.asm` / `Add.hack` (Arithmetic addition)
- `Max.asm` / `Max.hack` (Conditional branching)
- `Rect.asm` / `Rect.hack` (Screen memory loop)
- `Pong.asm` / `Pong.hack` (27,483 lines complex game)

---

## How to Run
```bash
python assembler.py Add.asm
python assembler.py Max.asm
python assembler.py Rect.asm
python assembler.py Pong.asm
```
Output matches the official Nand to Tetris assembler bit-for-bit.
