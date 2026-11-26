# Part A – Build the Computer
**Nand to Tetris – I (ETCCNT301) Capstone Project**  
School of Engineering & Technology, K.R. Mangalam University  
**Student:** Shivam Kumar Roy | **Roll No:** 2501010138  

---

## Overview
Part A implements the complete Von Neumann Hack computer architecture by integrating:
1. `CPU.hdl`: The Hack Central Processing Unit (ALU, A/D registers, Program Counter PC).
2. `Memory.hdl`: Address routing for Data RAM (RAM16K), Screen Memory Map, and Keyboard register.
3. `Computer.hdl`: Top-level integration linking ROM32K, CPU, and Memory.

---

## Files in this Directory
- `CPU.hdl` – Hack CPU chip implementation
- `Memory.hdl` – Memory address dispatcher chip
- `Computer.hdl` – Top-level computer chip
- `screenshot_tests.png` – Official test pass verification graphic

### Official Test Scripts & Compare Files:
- `CPU.tst` / `CPU.cmp` – Tests instruction fetch, decode, ALU execution, and jumps
- `Memory.tst` / `Memory.cmp` – Tests RAM16K, Screen (0x4000-0x5FFF), and Keyboard (0x6000)
- `ComputerAdd.tst` / `ComputerAdd.cmp` – Runs Add.hack on Computer.hdl
- `ComputerMax.tst` / `ComputerMax.cmp` – Runs Max.hack on Computer.hdl
- `ComputerRect.tst` / `ComputerRect.cmp` – Runs Rect.hack on Computer.hdl

---

## Verification
All chips were tested using the official Nand to Tetris Hardware Simulator. All 5 test scripts successfully completed with zero comparison errors (`Comparison ended successfully`).
