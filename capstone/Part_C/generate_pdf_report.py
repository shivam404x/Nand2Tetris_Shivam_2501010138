#!/usr/bin/env python3
"""
Generate publication-quality HTML and compile to PDF for Capstone Project Report.
Student: Shivam Kumar Roy | Roll No: 2501010138 | K = 38
"""

import os
import base64
import subprocess

def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as f:
            return "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")
    return ""

def create_report_html(output_html_path="capstone/report.html"):
    box_img_b64 = get_base64_image("capstone/screenshot_box.png")
    test_img_b64 = get_base64_image("capstone/screenshot_tests.png")

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Capstone Project Report - Shivam Kumar Roy (2501010138)</title>
<style>
  @page {{
    size: A4 portrait;
    margin: 16mm 14mm 16mm 14mm;
    @bottom-right {{
      content: counter(page);
    }}
  }}
  * {{
    box-sizing: border-box;
  }}
  body {{
    font-family: 'Segoe UI', Helvetica, Arial, sans-serif;
    color: #1f2937;
    line-height: 1.45;
    font-size: 10pt;
    margin: 0;
    padding: 0;
    background: #ffffff;
  }}
  .header-card {{
    border-bottom: 2px solid #1e3a8a;
    padding-bottom: 10px;
    margin-bottom: 14px;
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
  }}
  .university-title {{
    font-size: 15pt;
    font-weight: 700;
    color: #1e3a8a;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin: 0;
  }}
  .sub-title {{
    font-size: 11pt;
    font-weight: 600;
    color: #4b5563;
    margin-top: 3px;
    margin-bottom: 0;
  }}
  .course-badge {{
    display: inline-block;
    background: #e0e7ff;
    color: #3730a3;
    font-weight: 600;
    font-size: 8.5pt;
    padding: 2px 8px;
    border-radius: 4px;
    margin-top: 4px;
  }}
  .meta-grid {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 8px 12px;
    margin-bottom: 14px;
    gap: 8px;
  }}
  .meta-item {{
    font-size: 8.5pt;
  }}
  .meta-label {{
    color: #64748b;
    font-weight: 500;
    text-transform: uppercase;
    font-size: 7.5pt;
  }}
  .meta-val {{
    font-weight: 700;
    color: #0f172a;
    font-size: 9.5pt;
    margin-top: 2px;
  }}
  .highlight-k {{
    color: #2563eb;
  }}
  h2 {{
    font-size: 11.5pt;
    color: #1e3a8a;
    border-left: 4px solid #2563eb;
    padding-left: 8px;
    margin-top: 14px;
    margin-bottom: 6px;
    text-transform: uppercase;
    letter-spacing: 0.3px;
  }}
  h3 {{
    font-size: 9.5pt;
    color: #0f172a;
    margin-top: 8px;
    margin-bottom: 4px;
  }}
  p {{
    margin: 4px 0 6px 0;
    text-align: justify;
  }}
  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 6px 0 10px 0;
    font-size: 8.5pt;
  }}
  th, td {{
    border: 1px solid #cbd5e1;
    padding: 4.5px 8px;
    text-align: left;
  }}
  th {{
    background-color: #f1f5f9;
    color: #1e293b;
    font-weight: 600;
  }}
  tr:nth-child(even) {{
    background-color: #f8fafc;
  }}
  .badge-pass {{
    background: #dcfce7;
    color: #166534;
    font-weight: 700;
    padding: 1px 6px;
    border-radius: 3px;
    display: inline-block;
  }}
  .code-box {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 6px 10px;
    font-family: Consolas, 'Courier New', monospace;
    font-size: 8pt;
    line-height: 1.35;
    margin: 6px 0;
  }}
  .img-container {{
    text-align: center;
    margin: 8px 0;
  }}
  .img-container img {{
    max-width: 95%;
    max-height: 220px;
    border: 1px solid #94a3b8;
    border-radius: 4px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
  }}
  .img-caption {{
    font-size: 7.5pt;
    color: #64748b;
    margin-top: 3px;
    font-style: italic;
  }}
  .callout {{
    background: #eff6ff;
    border-left: 3px solid #3b82f6;
    padding: 6px 10px;
    margin: 6px 0;
    border-radius: 0 4px 4px 0;
    font-size: 8.5pt;
  }}
  .page-break {{
    page-break-before: always;
  }}
</style>
</head>
<body>

  <!-- HEADER -->
  <div class="header-card">
    <div>
      <h1 class="university-title">K.R. Mangalam University</h1>
      <p class="sub-title">School of Engineering & Technology — Nand to Tetris – I (ETCCNT301)</p>
      <span class="course-badge">Capstone Project Report: Make the Computer Draw a Box</span>
    </div>
    <div style="text-align: right;">
      <div style="font-size: 8pt; color: #64748b;">Max Marks: 10</div>
      <div style="font-size: 8.5pt; font-weight: 700; color: #1e3a8a;">CO1–CO4 Competency</div>
    </div>
  </div>

  <!-- STUDENT METADATA -->
  <div class="meta-grid">
    <div class="meta-item">
      <div class="meta-label">Student Name</div>
      <div class="meta-val">Shivam Kumar Roy</div>
    </div>
    <div class="meta-item">
      <div class="meta-label">Roll Number</div>
      <div class="meta-val">2501010138</div>
    </div>
    <div class="meta-item">
      <div class="meta-label">Personal Number (K)</div>
      <div class="meta-val highlight-k">K = 38</div>
    </div>
    <div class="meta-item">
      <div class="meta-label">Box Specifications</div>
      <div class="meta-val">Row 38 | 48px &times; 20 rows</div>
    </div>
  </div>

  <!-- SECTION 1 -->
  <h2>1. Executive Summary & Parameter Derivation</h2>
  <p>
    This capstone project validates the end-to-end realization of the Hack computer system stack, spanning gate-level microarchitecture construction, system-level software translation via a Python-based assembler, and real-time firmware graphics synthesis. All parameters are rigorously bound to the candidate's personal number <strong>K = 38</strong> (derived from the terminal two digits of University Roll No. <code>2501010138</code>).
  </p>

  <table>
    <thead>
      <tr>
        <th>Parameter</th>
        <th>Governing Formula</th>
        <th>Calculated Value</th>
        <th>Architectural Impact</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Personal Number (K)</strong></td>
        <td>Last 2 digits of Roll No.</td>
        <td><strong>K = 38</strong></td>
        <td>Universal seed for hardware/software parameters</td>
      </tr>
      <tr>
        <td><strong>Assembler Feature</strong></td>
        <td>K mod 3</td>
        <td><strong>38 mod 3 = 2</strong></td>
        <td>Non-fatal warning on duplicate label definitions</td>
      </tr>
      <tr>
        <td><strong>Box Vertical Origin</strong></td>
        <td>Row K</td>
        <td><strong>Row 38</strong></td>
        <td>Base Address = SCREEN + 32 &times; 38 = <strong>17600 (0x44C0)</strong></td>
      </tr>
      <tr>
        <td><strong>Box Height</strong></td>
        <td>Constant Specification</td>
        <td><strong>20 rows</strong></td>
        <td>Spans screen rows 38 to 57 inclusive</td>
      </tr>
      <tr>
        <td><strong>Box Width</strong></td>
        <td>16 &times; ((K mod 4) + 1) px</td>
        <td><strong>16 &times; (2 + 1) = 48 px</strong></td>
        <td>Exactly 3 consecutive 16-bit screen words per row</td>
      </tr>
    </tbody>
  </table>

  <!-- SECTION 2 -->
  <h2>2. Part A: Computer Microarchitecture Construction</h2>
  <p>
    The Hack computer architecture was assembled using three foundational HDL modules adhering to the Von Neumann structural model:
  </p>
  <ul>
    <li><strong>Memory.hdl:</strong> Dispatches the 32K address space across data RAM (0x0000–0x3FFF via <code>RAM16K</code>), screen memory map (0x4000–0x5FFF via <code>Screen</code>), and the keyboard memory-mapped register (0x6000 via <code>Keyboard</code>). Demultiplexing of write signals and multiplexing of output bus lines is governed by address bits <code>address[13..14]</code>.</li>
    <li><strong>CPU.hdl:</strong> Features an ALU, two internal registers (<code>A</code> and <code>D</code>), and a Program Counter (<code>PC</code>). Implements 16-bit instruction decoding: MSB = 0 dictates an A-instruction (immediate data / address load), while MSB = 1 governs C-instructions (ALU computation, destination routing, and conditional branching based on ALU status flags <code>zr</code> and <code>ng</code>).</li>
    <li><strong>Computer.hdl:</strong> Top-level integrated chip wiring <code>ROM32K</code> instruction fetch with <code>CPU</code> processing datapath and <code>Memory</code> read/write infrastructure.</li>
  </ul>

  <div class="img-container">
    <img src="{test_img_b64}" alt="Hardware Simulator Verification">
    <div class="img-caption">Figure 1: Official Hardware Simulator test execution verification (All 5 test scripts PASSED).</div>
  </div>

  <table>
    <thead>
      <tr>
        <th>Test Script</th>
        <th>Target Chip</th>
        <th>Validation Focus</th>
        <th>Status</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>CPU.tst</code></td>
        <td>CPU.hdl</td>
        <td>Instruction decode, ALU execution, A/D register loading, conditional branching</td>
        <td><span class="badge-pass">PASS</span> Comparison ended successfully</td>
      </tr>
      <tr>
        <td><code>Memory.tst</code></td>
        <td>Memory.hdl</td>
        <td>Address partition routing (RAM16K vs Screen vs Keyboard) and load assertions</td>
        <td><span class="badge-pass">PASS</span> Comparison ended successfully</td>
      </tr>
      <tr>
        <td><code>ComputerAdd.tst</code></td>
        <td>Computer.hdl</td>
        <td>End-to-end execution of Add.hack arithmetic routine on top-level computer</td>
        <td><span class="badge-pass">PASS</span> Comparison ended successfully</td>
      </tr>
      <tr>
        <td><code>ComputerMax.tst</code></td>
        <td>Computer.hdl</td>
        <td>Conditional jump execution and dynamic branch evaluation</td>
        <td><span class="badge-pass">PASS</span> Comparison ended successfully</td>
      </tr>
      <tr>
        <td><code>ComputerRect.tst</code></td>
        <td>Computer.hdl</td>
        <td>Screen memory manipulation loop running Rect.hack</td>
        <td><span class="badge-pass">PASS</span> Comparison ended successfully</td>
      </tr>
    </tbody>
  </table>

  <!-- PAGE BREAK FOR CLEAN FORMATTING -->
  <div class="page-break"></div>

  <!-- SECTION 3 -->
  <h2>3. Part B: Python Assembler Design & Extra Feature (K mod 3 = 2)</h2>
  <p>
    A custom two-pass assembler was engineered in Python (<code>assembler.py</code>) to translate symbolic Hack assembly language into binary machine instructions:
  </p>
  <ul>
    <li><strong>Pass 1 (Lexical Stripping & Symbol Table Generation):</strong> Eliminates line comments (<code>//</code>) and whitespace. Tracks ROM instruction address indexing. Encounters of pseudo-instructions such as <code>(LABEL)</code> record the label mapping in the symbol table.
    <div class="callout">
      <strong>Special Feature (K mod 3 = 2): Duplicate Label Warning</strong><br>
      The parser records the first declaration line of every label. If an identical label re-appears, the assembler logs a non-fatal warning without crashing:<br>
      <code>Warning (Line 7): Duplicate label '(LOOP)' defined! First defined at line 4.</code>
    </div>
    </li>
    <li><strong>Pass 2 (Code Generation):</strong> Resolves numerical and symbolic A-instructions (allocating user variables sequentially to RAM 16 onward: <code>color=16</code>, <code>addr=17</code>, <code>rows_left=18</code>). Translates C-instructions into <code>111 + comp(7b) + dest(3b) + jump(3b)</code>. Exports full symbol table to <code>symbols.txt</code>.</li>
  </ul>

  <p><strong>Verification Suite:</strong> Successfully verified against all standard benchmark test programs: <code>Add.asm</code> (6 lines), <code>Max.asm</code> (16 lines), <code>Rect.asm</code> (25 lines), and <code>Pong.asm</code> (27,483 lines). Binary outputs matched the official Nand to Tetris reference assembler bit-for-bit.</p>

  <!-- SECTION 4 -->
  <h2>4. Part C: The Box Assembly Program (Box.asm)</h2>
  <p>
    <code>Box.asm</code> creates an interactive graphics driver that continuously monitors keyboard input (<code>RAM[24576] / KBD</code>). When any key is pressed (<code>KBD != 0</code>), a solid black box is drawn at Row 38. When released (<code>KBD == 0</code>), the box is erased to white.
  </p>

  <div class="img-container">
    <img src="{box_img_b64}" alt="CPU Emulator Box Rendering">
    <div class="img-caption">Figure 2: Pixel-accurate CPU Emulator simulation displaying the 48&times;20 box at Row 38 during active keypress.</div>
  </div>

  <div class="code-box">
// High-efficiency core rendering loop from Box.asm
(ROW_LOOP)
    @rows_left
    D=M
    @MAIN_LOOP
    D;JEQ          // Loop back to poll keyboard once 20 rows are rendered
    @color
    D=M
    @addr          // Word 0 (pixels 0-15)
    A=M
    M=D
    @addr          // Word 1 (pixels 16-31)
    M=M+1
    @color
    D=M
    @addr
    A=M
    M=D
    @addr          // Word 2 (pixels 32-47)
    M=M+1
    @color
    D=M
    @addr
    A=M
    M=D
    @30            // Advance addr to next screen row (2 already moved + 30 = 32 words)
    D=A
    @addr
    M=D+M
    @rows_left
    M=M-1
    @ROW_LOOP
    0;JMP
  </div>

  <!-- SECTION 5 -->
  <h2>5. Critical Engineering Mistake Encountered & Resolved</h2>
  <p>
    During initial testing of <code>Box.asm</code> with the Python assembler, an arithmetic syntax error occurred at the row stride computation:
  </p>
  <div class="callout">
    <strong>Encountered Failure:</strong> <code>Error: Line 97: invalid comp expression 'M+D' in instruction 'M=M+D'</code>
  </div>
  <p>
    <strong>Root Cause:</strong> Although addition is commutative mathematically, the Hack ALU microarchitecture physically hardwires input X to the <code>D</code> register and input Y to memory operand <code>M</code> (with control bits <code>c1..c6 = 000010</code>). Consequently, the official Hack hardware specification strictly defines canonical addition as <code>D+M</code>. Writing <code>M+D</code> caused the parser to reject the computation string.
  </p>
  <p>
    <strong>Corrective Action:</strong> In <code>Box.asm</code>, the instruction was updated to <code>M=D+M</code>. Additionally, <code>assembler.py</code> was updated to incorporate symmetric aliases (<code>M+D</code>, <code>A+D</code>, <code>M&amp;D</code>, <code>M|D</code>) into its internal computation table, making the assembler fault-tolerant and backward-compatible.
  </p>

  <!-- SECTION 6 -->
  <h2>6. Viva Voce & Practical Defense Reference</h2>
  <table>
    <thead>
      <tr>
        <th>Spot-Modification Scenario</th>
        <th>Exact Code Modification in Box.asm</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Move Box Down by N Rows</strong></td>
        <td>At <code>(DRAW_INIT)</code>, update start address from <code>@17600</code> to <code>@(17600 + 32 &times; N)</code> (e.g. 5 rows down = <code>@17760</code>).</td>
      </tr>
      <tr>
        <td><strong>Modify Box Height</strong></td>
        <td>At <code>(DRAW_INIT)</code>, change row counter from <code>@20</code> to desired value (e.g., <code>@30</code> for 30 rows tall).</td>
      </tr>
      <tr>
        <td><strong>Invert Display Trigger</strong></td>
        <td>In <code>(MAIN_LOOP)</code>, toggle jump condition from <code>D;JNE</code> to <code>D;JEQ</code> (renders black by default, clears on press).</td>
      </tr>
    </tbody>
  </table>

</body>
</html>
"""

    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Report HTML written to: {output_html_path}")
    return output_html_path

def compile_html_to_pdf(html_path, output_pdf_path="capstone/Capstone_Project_Report_2501010138.pdf"):
    browser_paths = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        os.path.expandvars(r"%LOCALAPPDATA%\BraveSoftware\Brave-Browser\Application\brave.exe")
    ]

    selected_browser = None
    for bp in browser_paths:
        if os.path.exists(bp):
            selected_browser = bp
            break

    if not selected_browser:
        print("Error: No browser found to render PDF.")
        return False

    abs_html = os.path.abspath(html_path)
    abs_pdf = os.path.abspath(output_pdf_path)

    cmd = [
        selected_browser,
        "--headless",
        "--disable-gpu",
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={abs_pdf}",
        f"file:///{abs_html.replace(os.sep, '/')}"
    ]

    print(f"Compiling PDF using {os.path.basename(selected_browser)}...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(abs_pdf) and os.path.getsize(abs_pdf) > 0:
        print(f"SUCCESS: PDF generated successfully at: {abs_pdf} ({os.path.getsize(abs_pdf)} bytes)")
        return True
    else:
        print("Failed to generate PDF. Subprocess output:", res.stdout, res.stderr)
        return False

if __name__ == "__main__":
    html_file = create_report_html()
    compile_html_to_pdf(html_file)
