#!/usr/bin/env python3
"""
Hack Assembler in Python
Nand to Tetris - I (ETCCNT301) - Capstone Project
School of Engineering & Technology, K.R. Mangalam University

Student: Shivam Kumar Roy
Roll Number: 2501010138
Personal Number: K = 38 (38 mod 3 = 2)
Extra Feature: Print a warning if the same label is written twice.
(Also supports symbols.txt export and clear line number syntax error reporting).
"""

import sys
import os

# Lookup tables for C-instructions
COMP_TABLE = {
    # a = 0 (using A)
    "0":   "0101010",
    "1":   "0111111",
    "-1":  "0111010",
    "D":   "0001100",
    "A":   "0110000",
    "!D":  "0001101",
    "!A":  "0110001",
    "-D":  "0001111",
    "-A":  "0110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "D+A": "0000010",
    "A+D": "0000010",
    "D-A": "0100011",
    "A-D": "0000111",
    "D&A": "0000000",
    "A&D": "0000000",
    "D|A": "0010101",
    "A|D": "0010101",
    # a = 1 (using M)
    "M":   "1110000",
    "!M":  "1110001",
    "-M":  "1110011",
    "M+1": "1110111",
    "M-1": "1110010",
    "D+M": "1000010",
    "M+D": "1000010",
    "D-M": "1010011",
    "M-D": "1000111",
    "D&M": "1000000",
    "M&D": "1000000",
    "D|M": "1010101",
    "M|D": "1010101",
}

DEST_TABLE = {
    "":    "000",
    "M":   "001",
    "D":   "010",
    "MD":  "011",
    "A":   "100",
    "AM":  "101",
    "AD":  "110",
    "AMD": "111",
}

JUMP_TABLE = {
    "":    "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111",
}

def get_predefined_symbols():
    symbols = {
        "SP": 0,
        "LCL": 1,
        "ARG": 2,
        "THIS": 3,
        "THAT": 4,
        "SCREEN": 16384,
        "KBD": 24576,
    }
    for i in range(16):
        symbols[f"R{i}"] = i
    return symbols


def clean_line(line):
    """Strip comments (//...) and surrounding whitespace."""
    comment_pos = line.find("//")
    if comment_pos != -1:
        line = line[:comment_pos]
    return line.strip().replace(" ", "")


class Assembler:
    def __init__(self, k=38):
        self.k = k
        self.symbol_table = get_predefined_symbols()
        self.next_var_addr = 16
        self.label_first_seen_line = {}  # For duplicate label warning (K mod 3 = 2)
        self.errors = []
        self.warnings = []

    def assemble(self, asm_filepath, hack_filepath=None, save_symbols=True):
        if not os.path.exists(asm_filepath):
            print(f"Error: File '{asm_filepath}' not found.")
            return False

        if hack_filepath is None:
            base, _ = os.path.splitext(asm_filepath)
            hack_filepath = base + ".hack"

        with open(asm_filepath, "r", encoding="utf-8") as f:
            raw_lines = f.readlines()

        # ----------------------------------------------------
        # PASS 1: Symbol resolution for labels (LOOP), track addresses
        # ----------------------------------------------------
        rom_address = 0
        instructions = []

        for line_no, raw_line in enumerate(raw_lines, start=1):
            line = clean_line(raw_line)
            if not line:
                continue

            if line.startswith("(") and line.endswith(")"):
                label = line[1:-1].strip()
                if not label:
                    self.errors.append(f"Line {line_no}: empty label '()'")
                    continue

                # Extra Feature (K mod 3 = 2): Warning on duplicate label definition
                if label in self.label_first_seen_line:
                    prev_line = self.label_first_seen_line[label]
                    warning_msg = (
                        f"Warning (Line {line_no}): Duplicate label '({label})' defined! "
                        f"First defined at line {prev_line}."
                    )
                    self.warnings.append(warning_msg)
                    print(warning_msg)
                else:
                    self.label_first_seen_line[label] = line_no
                    self.symbol_table[label] = rom_address
            else:
                instructions.append((line_no, line))
                rom_address += 1

        # ----------------------------------------------------
        # PASS 2: Code Generation (turn each instruction into 16 bits)
        # ----------------------------------------------------
        binary_code = []

        for line_no, line in instructions:
            if line.startswith("@"):
                # A-instruction: @value or @symbol
                symbol = line[1:]
                if symbol.isdigit():
                    value = int(symbol)
                else:
                    if symbol in self.symbol_table:
                        value = self.symbol_table[symbol]
                    else:
                        # New variable: allocate next RAM address starting from 16
                        value = self.next_var_addr
                        self.symbol_table[symbol] = value
                        self.next_var_addr += 1

                if value < 0 or value > 32767:
                    err = f"Line {line_no}: value {value} out of range (0-32767) in '{line}'"
                    self.errors.append(err)
                    print(f"Error: {err}")
                    continue

                # A-instruction format: 0 followed by 15-bit binary
                bin_instr = f"0{value:015b}"
                binary_code.append(bin_instr)

            else:
                # C-instruction: dest=comp;jump
                dest = ""
                comp = ""
                jump = ""

                rest = line
                if "=" in rest:
                    dest, rest = rest.split("=", 1)
                if ";" in rest:
                    comp, jump = rest.split(";", 1)
                else:
                    comp = rest

                # Validate
                if comp not in COMP_TABLE:
                    err = f"Line {line_no}: invalid comp expression '{comp}' in instruction '{line}'"
                    self.errors.append(err)
                    print(f"Error: {err}")
                    continue

                if dest not in DEST_TABLE:
                    err = f"Line {line_no}: invalid dest expression '{dest}' in instruction '{line}'"
                    self.errors.append(err)
                    print(f"Error: {err}")
                    continue

                if jump not in JUMP_TABLE:
                    err = f"Line {line_no}: invalid jump condition '{jump}' in instruction '{line}'"
                    self.errors.append(err)
                    print(f"Error: {err}")
                    continue

                comp_bits = COMP_TABLE[comp]
                dest_bits = DEST_TABLE[dest]
                jump_bits = JUMP_TABLE[jump]

                # C-instruction format: 111 + comp (7 bits) + dest (3 bits) + jump (3 bits)
                bin_instr = f"111{comp_bits}{dest_bits}{jump_bits}"
                binary_code.append(bin_instr)

        if self.errors:
            print(f"\nAssembly failed with {len(self.errors)} error(s).")
            return False

        # Write output .hack file
        with open(hack_filepath, "w", encoding="utf-8") as f:
            for b in binary_code:
                f.write(b + "\n")

        print(f"Assembly successful! Generated: {hack_filepath} ({len(binary_code)} instructions)")

        # Extra Feature (K mod 3 = 0 or general utility): Save symbols.txt
        if save_symbols or (self.k % 3 == 0):
            sym_filepath = os.path.join(os.path.dirname(hack_filepath) or ".", "symbols.txt")
            with open(sym_filepath, "w", encoding="utf-8") as f:
                f.write(f"// Symbol Table for {os.path.basename(asm_filepath)}\n")
                f.write(f"// Total symbols: {len(self.symbol_table)}\n\n")
                f.write(f"{'SYMBOL':<20} {'DEC':<10} {'HEX':<10}\n")
                f.write("-" * 40 + "\n")
                for s_name in sorted(self.symbol_table.keys()):
                    s_val = self.symbol_table[s_name]
                    f.write(f"{s_name:<20} {s_val:<10} 0x{s_val:04X}\n")
            print(f"Symbol table written to: {sym_filepath}")

        return True


def main():
    if len(sys.argv) < 2:
        print("Usage: python assembler.py <file.asm> [output.hack] [--k <number>]")
        sys.exit(1)

    asm_file = sys.argv[1]
    hack_file = None
    k = 38  # Default K for roll number ending in 38 (Roll No: 2501010138)

    args = sys.argv[2:]
    idx = 0
    while idx < len(args):
        if args[idx] == "--k" and idx + 1 < len(args):
            k = int(args[idx + 1])
            idx += 2
        elif not args[idx].startswith("--") and hack_file is None:
            hack_file = args[idx]
            idx += 1
        else:
            idx += 1

    assembler = Assembler(k=k)
    success = assembler.assemble(asm_file, hack_file)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
