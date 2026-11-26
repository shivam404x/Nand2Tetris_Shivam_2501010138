# Capstone Project: Make the Computer Draw a Box
**Course:** Nand to Tetris – I (ETCCNT301)  
**School:** School of Engineering & Technology, K.R. Mangalam University  

**Student Name:** Shivam Kumar Roy  
**Roll Number:** 2501010138  
**Personal Number (K):** 38  

---

## 📁 Repository Structure (Organized by Parts)

The project has been separated into clean, modular directories for each assignment phase:

```text
capstone/
│
├── 📂 Part_A/                         # Part A: Hardware / Computer Architecture (2.5 Marks)
│   ├── CPU.hdl                        # Hack Central Processing Unit
│   ├── Memory.hdl                     # Memory address space router
│   ├── Computer.hdl                   # Top-level Hack Computer
│   ├── CPU.tst, CPU.cmp               # Official CPU validation scripts
│   ├── Memory.tst, Memory.cmp         # Official Memory validation scripts
│   ├── ComputerAdd.tst, .cmp          # Official ComputerAdd test
│   ├── ComputerMax.tst, .cmp          # Official ComputerMax test
│   ├── ComputerRect.tst, .cmp         # Official ComputerRect test
│   ├── screenshot_tests.png           # Hardware simulation pass screenshot
│   └── README.md                      # Part A Documentation
│
├── 📂 Part_B/                         # Part B: Python Assembler (3.0 Marks)
│   ├── assembler.py                   # Two-pass Hack Assembler in Python
│   ├── symbols.txt                    # Symbol Table
│   ├── Add.asm, Add.hack              # Benchmark arithmetic test
│   ├── Max.asm, Max.hack              # Benchmark branching test
│   ├── Rect.asm, Rect.hack            # Benchmark drawing test
│   ├── Pong.asm, Pong.hack            # Benchmark complex game (27K lines)
│   └── README.md                      # Part B Documentation (K mod 3 = 2 feature)
│
├── 📂 Part_C/                         # Part C: Box Assembly Program (2.5 Marks)
│   ├── Box.asm                        # Hack assembly program for Row 38, 48x20 box
│   ├── Box.hack                       # Binary machine code from assembler.py
│   ├── emulator.html                  # Interactive live web-based Hack CRT emulator
│   ├── run_test.py                    # Terminal execution visualizer
│   ├── screenshot_box.png             # CPU Emulator output screenshot
│   └── README.md                      # Part C Documentation & Instructions
│
├── 📄 Capstone_Project_Report_2501010138.pdf  # Official 4-page PDF Report for ZOSIMA
├── 📄 REPORT.md                       # Markdown Report source
├── 📄 VIVA_PREP.md                    # 5-minute Viva questions & on-the-spot changes
└── 📄 README.md                       # This file
```

---

## ⚡ Quick Start: How to Run

### 1. Test the Box Program in Browser (Part C)
```powershell
cd Part_C
start emulator.html
```
*Press and hold any key to draw the solid black box at Row 38. Release to clear.*

### 2. Run the Terminal Simulator (Part C)
```powershell
cd Part_C
python run_test.py
```

### 3. Assemble Hack Programs with Custom Assembler (Part B)
```powershell
cd Part_B
python assembler.py Add.asm
python assembler.py Max.asm
python assembler.py Rect.asm
python assembler.py Pong.asm
```

---

## 📑 Official Submissions
1. **GitHub Lab Repository:** `capstone/` folder with Part A, Part B, Part C.
2. **ZOSIMA Short Report:** `Capstone_Project_Report_2501010138.pdf` (Name, Roll No, K=38, Box Size, Hardware Tests Screenshot, Box Screenshot, One Mistake Fixed).
3. **Viva Voce Prep:** See `VIVA_PREP.md` for answers to "Make one small change on the spot (e.g., moving the box down)".
