#!/usr/bin/env python3
"""Build the Nooks BDR platform slide as an editable 16:9 PowerPoint."""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn

# ---- palette ----
BLUE      = RGBColor(0x2F, 0x63, 0xB4)
BLUE_DK   = RGBColor(0x1F, 0x3A, 0x66)
BLUE_DEEP = RGBColor(0x16, 0x29, 0x4A)
TEAL      = RGBColor(0x43, 0xC0, 0xA8)
TEAL_DK   = RGBColor(0x2F, 0x8F, 0xB4)
INK       = RGBColor(0x1F, 0x2A, 0x37)
SLATE     = RGBColor(0x55, 0x65, 0x7A)
LINE      = RGBColor(0xE4, 0xE8, 0xEF)
CARD      = RGBColor(0xF4, 0xF6, 0xFA)
GREEN     = RGBColor(0x2F, 0x9E, 0x6E)
WHITE     = RGBColor(0xFF, 0xFF, 0xFF)
MUTE      = RGBColor(0xAA, 0xB3, 0xC0)

prs = Presentation()
prs.slide_width  = Inches(13.333)
prs.slide_height = Inches(7.5)
slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank
shapes = slide.shapes

def rect(x, y, w, h, fill, line=None, shape=MSO_SHAPE.RECTANGLE, radius=None):
    sp = shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    sp.fill.solid(); sp.fill.fore_color.rgb = fill
    if line is None:
        sp.line.fill.background()
    else:
        sp.line.color.rgb = line; sp.line.width = Pt(1)
    sp.shadow.inherit = False
    if radius is not None and shape == MSO_SHAPE.ROUNDED_RECTANGLE:
        try:
            sp.adjustments[0] = radius
        except Exception:
            pass
    return sp

def text(x, y, w, h, runs, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP,
         space_after=2, line_spacing=1.0):
    """runs: list of paragraphs; each paragraph is list of (txt,size,bold,color,italic)."""
    tb = shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = 0; tf.margin_right = 0; tf.margin_top = 0; tf.margin_bottom = 0
    for i, para in enumerate(runs):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.space_before = Pt(0); p.space_after = Pt(space_after)
        p.line_spacing = line_spacing
        for (txt, size, bold, color, *rest) in para:
            italic = rest[0] if rest else False
            r = p.add_run(); r.text = txt
            r.font.size = Pt(size); r.font.bold = bold
            r.font.color.rgb = color; r.font.italic = italic
            r.font.name = "Arial"
    return tb

# ================= HEADER =================
rect(0, 0, 13.333, 1.5, BLUE)
text(0.49, 0.22, 12.3, 0.3, [[("TIGERCONNECT   ·   BDR TOOL INVESTMENT", 11, True, WHITE)]])
text(0.49, 0.5, 12.4, 0.55,
     [[("One AI platform for the BDR team — not a stack of tools", 27, True, WHITE)]])
text(0.49, 1.07, 12.3, 0.35,
     [[("Consolidate prospecting, dialing, sequencing, and AI coaching into Nooks — the platform our reps already work in every day.",
        13, False, WHITE)]])

# ================= LEFT COLUMN =================
LX, LW = 0.49, 4.25

def card(x, y, w, h, accent):
    rect(x, y, w, h, CARD, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.06)
    rect(x, y + 0.04, 0.07, h - 0.08, accent)  # accent bar

# --- THE PLAY ---
card(LX, 1.62, LW, 1.46, BLUE)
text(LX + 0.28, 1.78, LW - 0.5, 1.2, [
    [("THE PLAY", 10, True, BLUE)],
    [("Give 5 BDRs one place to do all their work", 14.5, True, BLUE_DK)],
    [("Reps find accounts, dial, sequence, and get coached ", 11, False, SLATE),
     ("in a single tool", 11, True, INK),
     (". No tab-hopping, no copy-paste, no lost context — more time actually selling.", 11, False, SLATE)],
], space_after=5, line_spacing=1.05)

# --- ALREADY INVESTED ---
card(LX, 3.2, LW, 1.66, TEAL)
text(LX + 0.28, 3.34, LW - 0.5, 1.4, [
    [("✦ ALREADY INVESTED", 10, True, GREEN)],
    [("We're not starting from scratch", 14.5, True, BLUE_DK)],
    [("The team already runs on ", 11, False, SLATE),
     ("AI Dialer + Nooks numbers + AI Prospector", 11, True, INK),
     (" today, with live workflows built around it.", 11, False, SLATE)],
    [("→ Nooks is merging ", 11, False, SLATE),
     ("Prospector into its Sequencing product", 11, True, INK),
     (" — adopting Sequencing is the natural next step, not a new vendor.", 11, False, SLATE)],
], space_after=5, line_spacing=1.05)

# --- WHY IT LANDS ---
text(LX, 5.0, LW, 0.3, [[("WHY IT LANDS FOR BDRs", 10, True, BLUE)]])
why = [
    ("1", BLUE,    "All-in-one workflow", "Find, call, and follow up in one place — less admin, more conversations."),
    ("2", TEAL_DK, "AI that compounds",   "Surfaces the right accounts, powers the dialer, coaches reps on live calls."),
    ("3", TEAL,    "Feeds Gong",          "Plugs into the GTM-wide conversation layer — one source of truth."),
]
wy = 5.34
for num, col, head, body in why:
    o = shapes.add_shape(MSO_SHAPE.OVAL, Inches(LX), Inches(wy), Inches(0.42), Inches(0.42))
    o.fill.solid(); o.fill.fore_color.rgb = col; o.line.fill.background(); o.shadow.inherit = False
    tf = o.text_frame; tf.word_wrap = False
    tf.margin_top = 0; tf.margin_bottom = 0; tf.margin_left = 0; tf.margin_right = 0
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = num; r.font.size = Pt(13); r.font.bold = True
    r.font.color.rgb = WHITE; r.font.name = "Arial"
    text(LX + 0.56, wy - 0.04, LW - 0.56, 0.6, [
        [(head, 12.5, True, BLUE_DK)],
        [(body, 10.5, False, SLATE)],
    ], space_after=1, line_spacing=1.0)
    wy += 0.62

# ================= RIGHT COLUMN =================
RX, RW = 4.95, 7.88
text(RX, 1.6, RW, 0.3,
     [[("THE FULL PLATFORM COST   ·   ORDER ORD-XHY110Y   ·   SEP 2026 – SEP 2027", 10.5, True, BLUE)]])
rect(RX, 1.95, RW, 4.84, CARD, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.04)

# ---- table ----
rows_data = [
    ("AI Dialer — Standard Seat", "The dialer reps live in", "5", "$3,600", "$18,000", False),
    ("AI Sequencing — User Seats", "Outreach for all 5 reps", "5", "$1,440", "$7,200", False),
    ("AI Sequencing — Admin Seats", "Build & manage sequences", "3", "$300", "$900", False),
    ("AI Coaching", "Live-call coaching for all 5 reps", "5", "$600", "$3,000", False),
    ("AI Action Credits", "Research, enrichment & automation fuel", "1.4M", "$0.02", "$28,000", False),
    ("Sequencing Implementation Fee", "One-time setup", "1", "$0", "WAIVED", True),
]
tx, ty, tw = RX + 0.28, 2.18, RW - 0.56
n_rows = len(rows_data) + 1
gt = shapes.add_table(n_rows, 4, Inches(tx), Inches(ty), Inches(tw), Inches(2.95)).table
gt.first_row = False; gt.horz_banding = False
# kill default table style background
tbl = gt._tbl
for tc in tbl.iter(qn('a:tc')):
    pass
gt.columns[0].width = Inches(tw - 3.2)
gt.columns[1].width = Inches(0.9)
gt.columns[2].width = Inches(1.15)
gt.columns[3].width = Inches(1.15)

def style_cell(cell, paras, align, vanch=MSO_ANCHOR.MIDDLE, fill=WHITE):
    cell.fill.solid(); cell.fill.fore_color.rgb = fill
    cell.vertical_anchor = vanch
    cell.margin_left = Inches(0.05); cell.margin_right = Inches(0.05)
    cell.margin_top = Inches(0.03); cell.margin_bottom = Inches(0.03)
    tf = cell.text_frame; tf.word_wrap = True
    for i, para in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align; p.space_before = Pt(0); p.space_after = Pt(0); p.line_spacing = 1.0
        for (txt, size, bold, color) in para:
            r = p.add_run(); r.text = txt; r.font.size = Pt(size)
            r.font.bold = bold; r.font.color.rgb = color; r.font.name = "Arial"

# header row
hdr = ["LINE ITEM", "QTY", "UNIT / YR", "ANNUAL"]
aligns = [PP_ALIGN.LEFT, PP_ALIGN.RIGHT, PP_ALIGN.RIGHT, PP_ALIGN.RIGHT]
for c, (h, a) in enumerate(zip(hdr, aligns)):
    style_cell(gt.cell(0, c), [[(h, 9.5, True, SLATE)]], a, fill=CARD)

# data rows
for ri, (name, desc, qty, unit, annual, waived) in enumerate(rows_data, start=1):
    name_col = GREEN if waived else INK
    name_paras = [[(name, 11.5, True, name_col)], [(desc, 9, False, SLATE)]]
    style_cell(gt.cell(ri, 0), name_paras, PP_ALIGN.LEFT, fill=CARD)
    style_cell(gt.cell(ri, 1), [[(qty, 11.5, False, name_col)]], PP_ALIGN.RIGHT, fill=CARD)
    style_cell(gt.cell(ri, 2), [[(unit, 11.5, False, name_col)]], PP_ALIGN.RIGHT, fill=CARD)
    annual_col = GREEN if waived else INK
    style_cell(gt.cell(ri, 3), [[(annual, 11.5, (True if waived else False), annual_col)]], PP_ALIGN.RIGHT, fill=CARD)

# row heights
gt.rows[0].height = Inches(0.32)
for ri in range(1, n_rows):
    gt.rows[ri].height = Inches(0.44)

# ---- totals ----
yt = 5.28
text(RX + 0.28, yt, RW - 0.56, 0.28, [[("List price subtotal", 11, False, SLATE)]])
text(RX + 0.28, yt, RW - 0.56, 0.28, [[("$67,100", 11, True, SLATE)]], align=PP_ALIGN.RIGHT)
text(RX + 0.28, yt + 0.3, RW - 0.56, 0.28, [[("Negotiated discount (implementation waived, 14.9%)", 11, True, GREEN)]])
text(RX + 0.28, yt + 0.3, RW - 0.56, 0.28, [[("– $10,000", 11, True, GREEN)]], align=PP_ALIGN.RIGHT)

# grand total bar
gy = 5.92
rect(RX + 0.28, gy, RW - 0.56, 0.72, BLUE_DK, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.12)
text(RX + 0.55, gy + 0.1, 4.5, 0.55, [
    [("Grand total — all-in", 14, True, WHITE)],
    [("5 BDR seats · billed yearly · Net 30", 9.5, False, RGBColor(0xC9, 0xD4, 0xE6))],
], anchor=MSO_ANCHOR.MIDDLE, space_after=1)
text(RX + RW - 3.3, gy + 0.06, 2.95, 0.6,
     [[("$57,100", 26, True, WHITE), (" / yr", 13, True, RGBColor(0xC9, 0xD4, 0xE6))]],
     align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)

# ================= FOOTER =================
rect(0, 6.88, 13.333, 0.62, BLUE_DEEP)
text(0.49, 6.88, 9.5, 0.62, [[
    ("INVESTMENT   ", 12, True, TEAL),
    ("5 BDR seats   •   $57.1K / year all-in   •   $10K implementation waived   •   live Sep 2026",
     12, False, WHITE)]], anchor=MSO_ANCHOR.MIDDLE)
text(9.0, 6.88, 3.84, 0.62, [[("Proprietary & Confidential · Draft ORD-XHY110Y", 9.5, False, RGBColor(0x9D, 0xAC, 0xC4))]],
     align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)

prs.save("nooks-slide.pptx")
print("saved nooks-slide.pptx")
