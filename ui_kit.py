"""
ui_kit.py - presentation layer for the RBAC & Trigger Visualizer.

Replaces the former frontend_utils module. Everything visual lives here:
design tokens, Streamlit chrome overrides, and the HTML components that
app.py, visualizer.py and exam_lab.py rely on. No database or business
logic is in this file.
"""
import html
import streamlit as st

# =============================================================================
# STYLESHEET
# =============================================================================
_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,300;6..72,400;6..72,500&family=Hanken+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
  --bg: #10252A;
  --bg-deep: #0B1C20;
  --panel: #16323A;
  --panel-2: #1B3840;
  --line: #2B4A52;
  --line-soft: #213F47;
  --text: #E8ECE6;
  --text-strong: #F1F4EF;
  --muted: #9DB0B0;
  --brass: #CDA85A;
  --brass-soft: #E0C27F;
  --pass: #86C5A0;
  --pass-bg: #1C4034;
  --block: #E2745C;
  --block-bg: #4A2620;
  --mist: #A7BFCF;
  --serif: 'Newsreader', Georgia, 'Times New Roman', serif;
  --sans: 'Hanken Grotesk', system-ui, -apple-system, 'Segoe UI', sans-serif;
  --mono: 'JetBrains Mono', ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace;
}

/* ---------- Streamlit chrome ---------- */
html, body, [data-testid="stAppViewContainer"], .stApp {
  background: var(--bg) !important;
  color: var(--text);
  font-family: var(--sans);
}
[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stToolbar"], [data-testid="stDecoration"], #MainMenu, footer { display: none !important; }
.block-container { max-width: 1180px; padding: 2.2rem 2rem 5rem !important; }
h1, h2, h3, h4 { font-family: var(--serif); font-weight: 400; color: var(--text-strong); letter-spacing: -0.01em; }
h3 { font-size: 1.55rem !important; margin-top: 0.4rem; }
h4 { font-size: 1.15rem !important; }
p, li, label, .stMarkdown { font-family: var(--sans); }
p, li { line-height: 1.6; }
a { color: var(--brass-soft); }
code { font-family: var(--mono) !important; font-size: 0.86em; color: var(--brass-soft); background: rgba(205,168,90,0.1); padding: 0.1em 0.35em; border-radius: 3px; }
hr { border-color: var(--line-soft) !important; margin: 2rem 0 !important; }
:focus-visible { outline: 2px solid var(--brass) !important; outline-offset: 2px; }

/* ---------- Tabs ---------- */
.stTabs [data-baseweb="tab-list"] { gap: 1.6rem; border-bottom: 1px solid var(--line); overflow-x: auto; }
.stTabs [data-baseweb="tab"] { height: auto; padding: 0.8rem 0; background: transparent; color: var(--muted); font-family: var(--sans); font-size: 0.98rem; font-weight: 500; white-space: nowrap; }
.stTabs [data-baseweb="tab"]:hover { color: var(--text); }
.stTabs [aria-selected="true"] { color: var(--text-strong) !important; }
.stTabs [data-baseweb="tab-highlight"] { background: var(--brass) !important; height: 2px; }
.stTabs [data-baseweb="tab-border"] { display: none; }
.stTabs [data-baseweb="tab-panel"] { padding-top: 1.8rem; }

/* ---------- Controls ---------- */
.stButton > button, [data-testid^="stBaseButton"] {
  border-radius: 4px; font-family: var(--sans); font-weight: 600; font-size: 0.92rem;
  border: 1px solid var(--line); background: transparent; color: var(--text);
  transition: background 0.15s ease, border-color 0.15s ease;
}
.stButton > button:hover { border-color: var(--brass); color: var(--text-strong); background: rgba(205,168,90,0.08); }
.stButton > button[kind="primary"], [data-testid="stBaseButton-primary"] { background: var(--brass); color: #1A1A14; border-color: var(--brass); }
.stButton > button[kind="primary"]:hover, [data-testid="stBaseButton-primary"]:hover { background: var(--brass-soft); border-color: var(--brass-soft); color: #14140F; }
[data-baseweb="input"], [data-baseweb="select"] > div, [data-baseweb="textarea"], .stTextArea textarea, .stNumberInput input, .stTextInput input {
  background: var(--bg-deep) !important; border-color: var(--line) !important; border-radius: 4px !important; color: var(--text);
}
.stTextArea textarea { font-family: var(--mono); font-size: 0.86rem; line-height: 1.55; }
[data-testid="stWidgetLabel"] p, .stSelectbox label p, .stRadio label p { color: var(--muted); font-size: 0.88rem; font-weight: 500; }
[data-testid="stExpander"] { border: 1px solid var(--line-soft) !important; border-radius: 4px !important; background: transparent; }
[data-testid="stExpander"] summary { font-weight: 600; color: var(--text); }
[data-testid="stAlert"] { background: var(--panel) !important; border: 1px solid var(--line); border-radius: 4px; color: var(--text); }
[data-testid="stCode"] pre, .stCodeBlock pre { background: var(--bg-deep) !important; border: 1px solid var(--line-soft); border-radius: 4px; font-family: var(--mono) !important; font-size: 0.82rem; }
[data-testid="stDataFrame"] { border: 1px solid var(--line-soft); border-radius: 4px; }
[data-testid="stCaptionContainer"] { color: var(--muted); }

/* ---------- Sidebar ---------- */
[data-testid="stSidebar"] { background: var(--bg-deep) !important; border-right: 1px solid var(--line-soft); }
[data-testid="stSidebar"] .block-container, [data-testid="stSidebarUserContent"] { padding-top: 1.4rem; }
[data-testid="stSidebar"] [data-testid="stRadio"] label { padding: 0.32rem 0.6rem; margin: 0 -0.6rem; border-radius: 4px; width: calc(100% + 1.2rem); }
[data-testid="stSidebar"] [data-testid="stRadio"] label:hover { background: rgba(255,255,255,0.04); }
[data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked) { background: rgba(205,168,90,0.12); box-shadow: inset 2px 0 0 var(--brass); }
[data-testid="stSidebar"] [data-testid="stRadio"] label:has(input:checked) p { color: var(--text-strong); font-weight: 600; }
.sb-label { font-size: 0.82rem; color: var(--muted); font-weight: 500; margin: 0.2rem 0 0.3rem; }
.sb-role { border-top: 1px solid var(--line); margin-top: 1.1rem; padding-top: 1rem; }
.sb-role-name { font-family: var(--serif); font-size: 1.5rem; color: var(--text-strong); line-height: 1.15; }
.sb-role-desc { color: var(--muted); font-size: 0.88rem; margin-top: 0.4rem; line-height: 1.55; }
.acct-table { width: 100%; border-collapse: collapse; font-size: 0.82rem; }
.acct-table td { padding: 0.4rem 0; border-bottom: 1px solid var(--line-soft); vertical-align: top; }
.acct-table td:first-child { font-family: var(--mono); color: var(--brass-soft); width: 2.6rem; }
.acct-table .flag { color: var(--muted); display: block; }

/* ---------- Masthead ---------- */
.mast-bar { display: flex; justify-content: space-between; align-items: center; gap: 1rem; flex-wrap: wrap; padding-bottom: 0.9rem; border-bottom: 1px solid var(--line); }
.mast-mark { font-weight: 600; font-size: 0.95rem; color: var(--text-strong); }
.mast-status { display: inline-flex; align-items: center; gap: 0.5rem; font-size: 0.86rem; color: var(--muted); }
.mast-dot { width: 8px; height: 8px; border-radius: 50%; background: var(--pass); }
.mast-dot.off { background: transparent; border: 1.5px solid var(--muted); }
.mast-head { font-family: var(--serif); font-weight: 300; font-size: clamp(2.6rem, 6.4vw, 5.4rem); line-height: 1.02; letter-spacing: -0.025em; color: var(--text-strong); margin: 2.6rem 0 0; max-width: 14ch; }
.mast-sub { color: #C3D0CD; font-size: 1.12rem; line-height: 1.6; max-width: 60ch; margin: 1.4rem 0 0; }
.notice { border-left: 3px solid var(--brass); background: var(--panel); padding: 0.9rem 1.1rem; margin: 1.6rem 0 0; border-radius: 0 4px 4px 0; font-size: 0.93rem; line-height: 1.55; color: var(--text); max-width: 78ch; }
.notice b { color: var(--text-strong); }

/* ---------- Gate rail (the memorable element) ---------- */
.rail-wrap { margin: 2.6rem 0 0.4rem; padding: 1.6rem 1.8rem 1.5rem; background: var(--panel); border: 1px solid var(--line); border-radius: 4px; }
.rail-top { display: flex; justify-content: space-between; align-items: baseline; gap: 1rem; flex-wrap: wrap; margin-bottom: 1.5rem; }
.rail-title { font-family: var(--serif); font-size: 1.35rem; color: var(--text-strong); }
.rail-title span { color: var(--muted); font-size: 1rem; }
.rail-follow { font-size: 0.82rem; color: var(--muted); }
.rail { display: grid; grid-template-columns: repeat(4, 1fr); gap: 0; }
.station { position: relative; padding: 36px 1.1rem 0 0; }
.station .mk { position: absolute; top: 0; left: 0; width: 24px; height: 24px; border-radius: 50%; border: 2px solid var(--line); background: var(--panel); display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700; line-height: 1; color: transparent; z-index: 2; }
.station .seg { position: absolute; top: 11px; left: 24px; right: 0; height: 2px; background: var(--line); transform-origin: left center; z-index: 1; }
.station:last-child .seg { display: none; }
.station.passed .mk { background: var(--pass); border-color: var(--pass); color: #0F2A1E; }
.station.passed .seg { background: var(--pass); }
.station.refused .mk { background: var(--block); border-color: var(--block); color: #2B0F09; }
.station.na .mk { border-style: dashed; border-color: var(--muted); }
.station.na .seg { background: repeating-linear-gradient(90deg, var(--line) 0 6px, transparent 6px 12px); }
.station.idle .mk { border-color: var(--mist); }
.st-name { font-weight: 600; font-size: 1rem; color: var(--text-strong); }
.st-detail { font-family: var(--mono); font-size: 0.76rem; color: var(--muted); margin-top: 0.35rem; line-height: 1.5; word-break: break-word; }
.st-state { font-size: 0.86rem; font-weight: 600; margin-top: 0.55rem; color: var(--muted); }
.station.passed .st-state { color: var(--pass); }
.station.refused .st-state { color: var(--block); }
.station.idle .st-state { color: var(--mist); }
.rail-verdict { margin-top: 1.5rem; padding-top: 1.1rem; border-top: 1px solid var(--line); font-size: 1rem; line-height: 1.55; color: var(--text); max-width: 80ch; }
.rail-verdict b { color: var(--text-strong); }
.rail-verdict.refused { border-top-color: var(--block); }
.rail-verdict.passed { border-top-color: var(--pass); }
.rail-wrap.animate .seg { animation: draw 0.5s ease-out both; animation-delay: calc(var(--i) * 0.28s); }
.rail-wrap.animate .station .mk { animation: land 0.35s ease-out both; animation-delay: calc(var(--i) * 0.28s); }
@keyframes draw { from { transform: scaleX(0); } to { transform: scaleX(1); } }
@keyframes land { from { transform: scale(0.6); opacity: 0.2; } to { transform: scale(1); opacity: 1; } }

@media (max-width: 760px) {
  .block-container { padding: 1.2rem 1rem 4rem !important; }
  .rail-wrap { padding: 1.2rem 1.1rem; }
  .rail { grid-template-columns: 1fr; }
  .station { padding: 0 0 1.5rem 42px; min-height: 48px; }
  .station .seg { top: 24px; left: 11px; right: auto; width: 2px; height: calc(100% - 24px); transform-origin: center top; }
  .station:last-child { padding-bottom: 0; }
  @keyframes draw { from { transform: scaleY(0); } to { transform: scaleY(1); } }
  .station.na .seg { background: repeating-linear-gradient(180deg, var(--line) 0 6px, transparent 6px 12px); }
}

/* ---------- Section headers & dossier ---------- */
.sec-head { margin: 0 0 1.2rem; }
.sec-title { font-family: var(--serif); font-size: 1.75rem; color: var(--text-strong); line-height: 1.15; letter-spacing: -0.01em; }
.sec-body { color: #B9C8C5; font-size: 1rem; line-height: 1.6; max-width: 68ch; margin-top: 0.5rem; }
.dossier-name { font-family: var(--serif); font-size: 1.9rem; line-height: 1.1; color: var(--text-strong); }
.dossier-desc { color: #B9C8C5; margin: 0.6rem 0 1.2rem; line-height: 1.55; font-size: 0.97rem; }
.dossier-count { font-size: 0.9rem; color: var(--muted); margin-bottom: 0.7rem; }
.dossier-count b { color: var(--text-strong); font-weight: 600; }
.ledger { list-style: none; margin: 0; padding: 0; font-size: 0.9rem; }
.ledger li { display: flex; gap: 0.6rem; padding: 0.38rem 0; border-bottom: 1px solid var(--line-soft); line-height: 1.35; color: var(--text); }
.ledger li .g { width: 1rem; flex: none; font-weight: 700; }
.ledger li.ok .g { color: var(--pass); }
.ledger li.no { color: var(--muted); }
.ledger li.no .g { color: var(--block); }
.grant { border-left: 3px solid var(--pass); background: var(--panel); padding: 0.8rem 1rem; border-radius: 0 4px 4px 0; font-size: 0.95rem; margin: 0.4rem 0 1rem; line-height: 1.5; }
.grant.no { border-left-color: var(--block); }
.grant b { color: var(--text-strong); }

/* ---------- Outcome banner ---------- */
.outcome { border: 1px solid var(--line); border-left-width: 4px; border-radius: 4px; background: var(--panel); padding: 1rem 1.2rem; margin: 1.6rem 0 1rem; }
.outcome.passed { border-left-color: var(--pass); }
.outcome.refused { border-left-color: var(--block); }
.outcome-title { font-family: var(--serif); font-size: 1.45rem; color: var(--text-strong); }
.outcome-body { color: #C3D0CD; margin-top: 0.3rem; line-height: 1.55; font-size: 0.97rem; }

/* ---------- Architecture ---------- */
.tiers { display: grid; grid-template-columns: repeat(3, 1fr); border-top: 1px solid var(--line); }
.tier { padding: 1.3rem 1.6rem 0.6rem 0; }
.tier + .tier { padding-left: 1.6rem; border-left: 1px solid var(--line-soft); }
.tier-name { font-family: var(--serif); font-size: 1.4rem; color: var(--text-strong); line-height: 1.2; }
.tier-who { font-size: 0.86rem; color: var(--brass-soft); margin: 0.3rem 0 0.7rem; font-weight: 600; }
.tier p { color: #B9C8C5; font-size: 0.95rem; margin: 0 0 0.8rem; }
@media (max-width: 860px) { .tiers { grid-template-columns: 1fr; } .tier, .tier + .tier { padding: 1.1rem 0 0.3rem; border-left: 0; border-top: 1px solid var(--line-soft); } }
.rules { width: 100%; border-collapse: collapse; }
.rules td { padding: 1rem 1rem 1rem 0; border-top: 1px solid var(--line-soft); vertical-align: top; font-size: 0.93rem; }
.rules td:first-child { width: 30%; }
.rules .fn { font-family: var(--mono); color: var(--brass-soft); font-size: 0.9rem; }
.rules .when { color: var(--muted); font-size: 0.82rem; margin-top: 0.3rem; line-height: 1.45; }
.sig { display: flex; gap: 0.8rem; margin-bottom: 0.45rem; line-height: 1.45; }
.sig code { flex: none; }
.sig span { color: #C3D0CD; }
@media (max-width: 760px) { .rules td { display: block; width: 100% !important; padding: 0.8rem 0 0.2rem; } .sig { flex-direction: column; gap: 0.1rem; } }
.matrix-scroll { overflow-x: auto; border: 1px solid var(--line-soft); border-radius: 4px; }
.matrix { border-collapse: collapse; width: 100%; min-width: 760px; font-size: 0.84rem; }
.matrix th { font-weight: 600; color: var(--muted); padding: 0.7rem 0.5rem; text-align: center; border-bottom: 1px solid var(--line); vertical-align: bottom; line-height: 1.25; }
.matrix th:first-child, .matrix td:first-child { text-align: left; padding-left: 1rem; min-width: 15rem; }
.matrix td { padding: 0.5rem; text-align: center; border-bottom: 1px solid var(--line-soft); color: var(--muted); }
.matrix td:first-child { color: var(--text); }
.matrix .y { color: var(--pass); font-weight: 700; }
.matrix .n { color: var(--line); }
.matrix .cur { background: rgba(205,168,90,0.1); }
.matrix th.cur { color: var(--brass-soft); }
.build-list { margin: 0; padding-left: 1.1rem; color: #C3D0CD; }
.build-list li { margin-bottom: 0.5rem; }

/* ---------- Trigger source tab ---------- */
.sync-chip { font-size: 0.82rem; color: var(--muted); border: 1px solid var(--line); border-radius: 4px; padding: 0.5rem 0.7rem; line-height: 1.4; }
.sync-chip b.ok { color: var(--pass); }
.sync-chip b.no { color: var(--block); }
.trigger-hero-card { border-top: 1px solid var(--line); padding: 1.3rem 0 0.2rem; }
.trigger-hero-header { display: flex; justify-content: space-between; gap: 1rem; flex-wrap: wrap; }
.trigger-hero-label { color: var(--muted); font-size: 0.86rem; }
.trigger-hero-title { margin: 0.2rem 0 0 !important; font-size: 1.9rem !important; }
.trigger-hero-title code { background: none; color: var(--brass-soft); font-size: 0.85em; padding: 0; }
.trigger-timing-badge { font-family: var(--mono); font-size: 0.78rem; color: var(--brass-soft); border: 1px solid var(--line); padding: 0.3rem 0.6rem; border-radius: 4px; display: inline-block; }
.trigger-hero-summary { color: #C3D0CD; line-height: 1.65; max-width: 78ch; margin-top: 0.9rem; }
.role-context-banner { background: var(--panel); border-left: 3px solid var(--brass); padding: 0.9rem 1.1rem; margin: 1.3rem 0; border-radius: 0 4px 4px 0; }
.role-context-title { font-weight: 600; font-size: 0.9rem; color: var(--brass-soft); }
.role-context-desc { color: var(--text); margin-top: 0.3rem; line-height: 1.6; font-size: 0.95rem; }
.firewall-card { border-top: 2px solid var(--block); padding: 0.9rem 0 0.4rem; height: 100%; }
.firewall-title { font-weight: 600; color: var(--text-strong); margin-bottom: 0.5rem; }
.firewall-badge { font-family: var(--mono); font-size: 0.74rem; color: var(--block); background: var(--block-bg); padding: 0.2rem 0.5rem; border-radius: 3px; display: inline-block; word-break: break-all; }
.firewall-desc { color: #B9C8C5; font-size: 0.9rem; line-height: 1.55; margin-top: 0.6rem; }
.tier1-notice-card { border-top: 1px solid var(--line); padding: 1.3rem 0 0.3rem; }
.tier1-notice-header { display: flex; justify-content: space-between; gap: 1rem; flex-wrap: wrap; }
.tier1-notice-pretitle { color: var(--muted); font-size: 0.86rem; }
.tier1-notice-title { margin: 0.2rem 0 0 !important; }
.tier1-badge { font-size: 0.78rem; color: var(--mist); border: 1px solid var(--line); padding: 0.3rem 0.6rem; border-radius: 4px; display: inline-block; }
.tier1-notice-content { color: #C3D0CD; line-height: 1.65; max-width: 78ch; margin-top: 0.8rem; }

/* ---------- ECA tab ---------- */
.eca-hero-container { border-top: 1px solid var(--line); padding: 1.2rem 0 0.4rem; margin-bottom: 1.2rem; }
.eca-hero-pretitle { color: var(--brass-soft); font-size: 0.9rem; font-weight: 600; }
.eca-hero-title { font-family: var(--serif); font-size: 1.9rem; color: var(--text-strong); margin: 0.2rem 0 0.5rem; }
.eca-hero-desc { color: #C3D0CD; line-height: 1.65; max-width: 78ch; }
.eca-col-card { border-top: 1px solid var(--line); padding: 1rem 0.2rem 1rem 0; height: 100%; }
.eca-col-header { font-weight: 600; font-size: 0.9rem; color: var(--brass-soft); }
.eca-col-title { font-family: var(--serif); font-size: 1.3rem; color: var(--text-strong); margin: 0.3rem 0 0.6rem; line-height: 1.2; }
.eca-col-content { color: #C3D0CD; font-size: 0.9rem; line-height: 1.6; }
.eca-col-content div { margin-bottom: 0.4rem; }
.eca-col-footer { margin-top: 0.9rem; padding-top: 0.7rem; border-top: 1px solid var(--line-soft); font-size: 0.82rem; color: var(--muted); }
.buffer-inspector-box { border-left: 3px solid var(--mist); background: var(--panel); padding: 0.9rem 1.1rem; margin: 0.6rem 0 1rem; border-radius: 0 4px 4px 0; }
.buffer-inspector-box.denied { border-left-color: var(--block); }
.buffer-inspector-box.select { border-left-color: var(--pass); }
.buffer-inspector-title { font-weight: 600; color: var(--text-strong); }
.buffer-inspector-desc { color: #C3D0CD; font-size: 0.92rem; line-height: 1.6; margin-top: 0.3rem; }

/* ---------- Trace & diff ---------- */
.trace-container { margin: 1.4rem 0 1rem; }
.trace-header { margin-bottom: 0.9rem; }
.trace-title { font-family: var(--serif); font-size: 1.35rem; color: var(--text-strong); }
.trace-subtitle { color: var(--muted); font-size: 0.86rem; margin-top: 0.15rem; }
.trace-step { display: flex; justify-content: space-between; align-items: center; gap: 1rem; padding: 0.6rem 0.9rem; border: 1px solid var(--line-soft); border-radius: 4px; background: var(--panel); }
.trace-step-content { display: flex; align-items: center; gap: 0.8rem; min-width: 0; }
.trace-icon { width: 22px; height: 22px; flex: none; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700; border: 1.5px solid var(--line); color: var(--muted); }
.trace-step-text { font-size: 0.93rem; color: var(--text); line-height: 1.4; }
.trace-badge { font-size: 0.78rem; font-weight: 600; color: var(--muted); white-space: nowrap; }
.trace-step.passed .trace-icon { background: var(--pass); border-color: var(--pass); color: #0F2A1E; }
.trace-step.passed .trace-badge { color: var(--pass); }
.trace-step.failed { border-color: var(--block); }
.trace-step.failed .trace-icon { background: var(--block); border-color: var(--block); color: #2B0F09; }
.trace-step.failed .trace-badge { color: var(--block); }
.trace-step.blocked { background: transparent; }
.trace-step.blocked .trace-step-text { color: var(--muted); }
.trace-arrow { height: 12px; margin-left: 1.55rem; border-left: 2px solid var(--line); }
.trace-arrow span { display: none; }
.trace-arrow.passed { border-left-color: var(--pass); }
.diff-section-title { font-family: var(--serif); font-size: 1.35rem; color: var(--text-strong); margin: 1.6rem 0 0.8rem; }
.diff-column-header { font-size: 0.86rem; font-weight: 600; color: var(--muted); padding-bottom: 0.5rem; border-bottom: 1px solid var(--line); margin-bottom: 0.7rem; }
.diff-column-header.post { color: var(--pass); border-bottom-color: var(--pass); }
.diff-column-header.rollback { color: var(--block); border-bottom-color: var(--block); }
.diff-card { background: var(--panel); border: 1px solid var(--line-soft); border-radius: 4px; padding: 0.8rem 1rem; margin-bottom: 0.6rem; }
.diff-card.updated { border-left: 3px solid var(--pass); }
.diff-card.rollback { border-left: 3px solid var(--block); }
.diff-card-header { display: flex; justify-content: space-between; align-items: baseline; gap: 0.6rem; }
.diff-card-title { font-weight: 600; color: var(--text-strong); }
.diff-card-type { color: var(--muted); font-size: 0.85rem; }
.diff-card-body { display: flex; justify-content: space-between; align-items: center; margin-top: 0.5rem; gap: 0.6rem; flex-wrap: wrap; }
.diff-card-balance { font-family: var(--mono); font-size: 1.05rem; color: var(--text-strong); }
.diff-status-badge { font-size: 0.78rem; font-weight: 600; color: var(--pass); background: rgba(134,197,160,0.14); padding: 0.15rem 0.55rem; border-radius: 3px; }
.diff-rollback-title { font-family: var(--serif); font-size: 1.25rem; color: var(--block); }
.diff-rollback-desc { color: #C3D0CD; margin-top: 0.3rem; line-height: 1.55; font-size: 0.93rem; }

/* ---------- Practice lab ---------- */
.exam-question-card { border-top: 1px solid var(--line); padding: 1.1rem 0 0.4rem; }
.exam-prompt-box { margin-top: 1rem; color: var(--text); line-height: 1.7; font-size: 1rem; max-width: 80ch; white-space: pre-wrap; }
.exam-hint-box { border-left: 3px solid var(--brass); background: var(--panel); padding: 0.85rem 1.1rem; margin: 1rem 0; border-radius: 0 4px 4px 0; }
.exam-challenge-box { border-left: 3px solid var(--mist); background: var(--panel); padding: 0.85rem 1.1rem; margin: 1.4rem 0 0.8rem; border-radius: 0 4px 4px 0; }

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation: none !important; transition: none !important; }
}
"""


def load_css():
    """Injects the stylesheet. Call once, right after st.set_page_config."""
    st.markdown(f"<style>{_CSS}</style>", unsafe_allow_html=True)


# =============================================================================
# HELPERS
# =============================================================================
def _e(value):
    return html.escape(str(value))


def section_head(title, body=None):
    body_html = f'<div class="sec-body">{body}</div>' if body else ""
    st.html(f'<div class="sec-head"><div class="sec-title">{_e(title)}</div>{body_html}</div>')


# =============================================================================
# MASTHEAD
# =============================================================================
def render_masthead(is_connected):
    status = (
        '<span class="mast-dot"></span>Database connected'
        if is_connected
        else '<span class="mast-dot off"></span>Database offline, simulator mode'
    )
    st.html(
        f"""
        <div class="mast-bar">
          <div class="mast-mark">RBAC &amp; Trigger Visualizer</div>
          <div class="mast-status">{status}</div>
        </div>
        <h1 class="mast-head">Watch PostgreSQL say no.</h1>
        <p class="mast-sub">Choose a role, run a banking operation, and follow it through the privilege
        catalog, the triggers and the audit log. Every refusal comes from the database itself, and the
        rail below shows which gate made the call.</p>
        """
    )
    if not is_connected:
        st.html(
            """
            <div class="notice"><b>Running offline.</b> You can still read the trigger source, step through the
            Event-Condition-Action model, view the execution paths and use the practice lab. To run live
            operations, add your PostgreSQL credentials to <code>.streamlit/secrets.toml</code>.</div>
            """
        )


# =============================================================================
# GATE RAIL
# =============================================================================
_STATE_LABEL = {
    "passed": "Passed",
    "refused": "Refused here",
    "notreached": "Not reached",
    "na": "Not applicable",
    "idle": "Ready",
}


def compute_stations(job_details, trigger_meta, has_access, result):
    """
    Derives the four gate states for one operation from facts the app already
    knows: the privilege required, the trigger map, and the real result.
    Returns (stations, verdict_class, verdict_html).
    """
    priv = job_details["privilege"]
    table = job_details["table"]
    cols = job_details.get("columns") or []
    is_read = priv == "SELECT"

    timing = (trigger_meta or {}).get("timing", "")
    has_before = bool(trigger_meta) and timing.startswith("BEFORE")
    has_after = bool(trigger_meta) and (
        trigger_meta.get("trigger_key") == "log_audit_event"
        or "log_audit_event" in trigger_meta.get("cascades", "")
    )
    before_name = trigger_meta["title"] if has_before else None
    after_name = "log_audit_event()" if has_after else None

    grant = f"GRANT {priv} on {table}" + (f" ({', '.join(cols)})" if cols else "")
    d1 = grant
    d2 = before_name or "No BEFORE trigger mapped to this operation"
    d3 = "Rows returned to the client" if is_read else "Row change commits atomically"
    d4 = after_name or "No audit trigger mapped to this operation"
    n3 = "Read" if is_read else "Write and commit"

    status = result.get("status") if isinstance(result, dict) else None

    if status is None:
        if not has_access:
            states = ["refused", "notreached", "notreached", "notreached"]
            s_override = {0: "Would be refused"}
            verdict_cls = "refused"
            verdict = (f"The active role holds no <b>{_e(priv)}</b> grant on <b>{_e(table)}</b>. "
                       "PostgreSQL would refuse this at the first gate.")
        else:
            states = ["idle", "idle" if has_before else "na", "idle", "idle" if has_after else "na"]
            s_override = {}
            verdict_cls = ""
            verdict = "Ready. Run the operation to see where each gate lands."
    elif status == "denied":
        states = ["refused", "notreached", "notreached", "notreached"]
        s_override = {}
        verdict_cls = "refused"
        msg = _e(str(result.get("message", ""))[:180])
        verdict = f"Refused at the privilege check. {msg}"
    elif status == "success":
        states = ["passed", "passed" if has_before else "na", "passed", "passed" if has_after else "na"]
        s_override = {}
        verdict_cls = "passed"
        verdict = "Committed. Every gate that applies to this operation passed."
    else:  # trigger or constraint exception
        clean = _e(result.get("clean_message", "Exception raised."))
        if has_before:
            states = ["passed", "refused", "notreached", "notreached"]
            verdict = f"Stopped by <b>{_e(before_name)}</b> and rolled back with no partial writes. {clean}"
        else:
            states = ["passed", "na", "refused", "notreached"]
            s_override = {2: "Write failed"}
            verdict = f"The write failed and was rolled back with no partial writes. {clean}"
        s_override = s_override if not has_before else {}
        verdict_cls = "refused"

    stations = []
    names = ["Privilege check", "BEFORE trigger", n3, "AFTER audit trigger"]
    details = [d1, d2, d3, d4]
    for i, (n, d, s) in enumerate(zip(names, details, states)):
        label = s_override.get(i, _STATE_LABEL[s]) if status != "success" or True else _STATE_LABEL[s]
        stations.append({"name": n, "detail": d, "state": s, "label": label})
    return stations, verdict_cls, verdict


def render_gate_rail(slot, op_name, role_name, stations, verdict_cls, verdict, animate=False):
    glyph = {"passed": "&#10003;", "refused": "&#10005;"}
    cells = []
    for i, st_ in enumerate(stations):
        css = "notreached" if st_["state"] == "notreached" else st_["state"]
        css_cls = "" if css == "notreached" else css
        cells.append(
            f'<div class="station {css_cls}" style="--i:{i}">'
            f'<span class="seg"></span><span class="mk">{glyph.get(st_["state"], "")}</span>'
            f'<div class="st-name">{_e(st_["name"])}</div>'
            f'<div class="st-detail">{_e(st_["detail"])}</div>'
            f'<div class="st-state">{_e(st_["label"])}</div></div>'
        )
    anim = " animate" if animate else ""
    slot.html(
        f"""
        <div class="rail-wrap{anim}">
          <div class="rail-top">
            <div class="rail-title">{_e(op_name)} <span>as {_e(role_name)}</span></div>
            <div class="rail-follow">Follows the operation selected in the Simulator</div>
          </div>
          <div class="rail">{''.join(cells)}</div>
          <div class="rail-verdict {verdict_cls}">{verdict}</div>
        </div>
        """
    )


# =============================================================================
# SIDEBAR
# =============================================================================
def render_sidebar_role_card(role_name, role_desc):
    st.sidebar.html(
        f'<div class="sb-role"><div class="sb-role-name">{_e(role_name)}</div>'
        f'<div class="sb-role-desc">{_e(role_desc)}</div></div>'
    )


def render_demo_accounts():
    rows = [
        ("101", "Alice Smith", "Active, KYC approved, $10,000"),
        ("102", "Bob Jones", "Active, KYC approved, $5,000"),
        ("103", "Charlie", "KYC pending, $3,000"),
        ("104", "Diana", "Frozen, $7,500"),
        ("105", "Edward", "Open fraud alert, $4,200"),
        ("106", "Fiona", "Active, loan already SUBMITTED"),
    ]
    body = "".join(
        f'<tr><td>{a}</td><td>{_e(n)}<span class="flag">{_e(f)}</span></td></tr>' for a, n, f in rows
    )
    st.html(f'<table class="acct-table">{body}</table>')


def render_sidebar_bio():
    """Keeps the project's own bio block if the legacy module is still present."""
    try:
        from frontend_utils import render_sidebar_bio as _legacy_bio
    except Exception:
        return
    try:
        _legacy_bio()
    except Exception:
        return


# =============================================================================
# SIMULATOR TAB
# =============================================================================
def render_role_dossier(role_name, role_desc, allowed, refused):
    total = len(allowed) + len(refused)
    ok = "".join(f'<li class="ok"><span class="g">&#10003;</span>{_e(j)}</li>' for j in allowed)
    no = "".join(f'<li class="no"><span class="g">&#10005;</span>{_e(j)}</li>' for j in refused)
    st.html(
        f"""
        <div class="dossier-name">{_e(role_name)}</div>
        <div class="dossier-desc">{_e(role_desc)}</div>
        <div class="dossier-count">Can run <b>{len(allowed)}</b> of {total} operations</div>
        <ul class="ledger">{ok}{no}</ul>
        """
    )


def render_grant_line(has_access, role_name, privilege, table):
    if has_access:
        st.html(f'<div class="grant"><b>{_e(role_name)}</b> holds <code>{_e(privilege)}</code> on <code>{_e(table)}</code>. The statement can reach PostgreSQL.</div>')
    else:
        st.html(f'<div class="grant no"><b>{_e(role_name)}</b> has no <code>{_e(privilege)}</code> grant on <code>{_e(table)}</code>. Select another role in the sidebar, or run it anyway in the trace below to see the refusal.</div>')


def render_outcome(result, privilege):
    status = result.get("status")
    if status == "success":
        title = "Query returned" if privilege == "SELECT" else "Committed"
        body = "The statement ran inside PostgreSQL and the result is shown below."
        cls = "passed"
    elif status == "denied":
        title = "Refused by the privilege catalog"
        body = _e(result.get("message", "Insufficient privileges."))
        cls = "refused"
    else:
        title = "Stopped by a trigger"
        body = _e(result.get("clean_message", "Trigger exception raised."))
        cls = "refused"
    st.html(f'<div class="outcome {cls}"><div class="outcome-title">{title}</div><div class="outcome-body">{body}</div></div>')


# =============================================================================
# SHARED
# =============================================================================
def render_sync_chip(job, current_job, has_access):
    synced = "Matches the Simulator" if job == current_job else "Free inspection"
    verdict = '<b class="ok">Authorized</b>' if has_access else '<b class="no">Refused by RBAC</b>'
    st.html(f'<div class="sync-chip">{synced}<br>{verdict}</div>')


def render_defense_depth_grid():
    st.html(
        """
        <div class="tiers">
          <div class="tier">
            <div class="tier-name">Privilege catalog</div>
            <div class="tier-who">Decides who may touch what</div>
            <p>GRANT statements control which role can SELECT, INSERT or UPDATE each table, down to named columns.
            A refusal here is SQLSTATE 42501, raised before any trigger runs. Nothing is allocated and nothing is written.</p>
          </div>
          <div class="tier">
            <div class="tier-name">BEFORE triggers</div>
            <div class="tier-who">Decide whether the row is acceptable</div>
            <p>PL/pgSQL functions inspect the incoming row against business rules: verified KYC, frozen accounts,
            open fraud alerts, sufficient balance, loan stage and who is acting. RAISE EXCEPTION cancels the statement.</p>
          </div>
          <div class="tier">
            <div class="tier-name">Atomic commit and audit</div>
            <div class="tier-who">Decide what is kept and recorded</div>
            <p>A failed statement rolls back with zero partial writes. AFTER triggers append the acting role, the old value
            and the new value to <code>audit_log</code>, which non-admin roles cannot modify or delete.</p>
          </div>
        </div>
        """
    )


def render_trigger_rules(trigger_map):
    """One row per distinct trigger, with its real error signatures."""
    seen, rows = set(), []
    for meta in trigger_map.values():
        key = meta["trigger_key"]
        if key in seen:
            continue
        seen.add(key)
        sigs = "".join(
            f'<div class="sig"><code>{_e(code)}</code><span>{_e(desc)}</span></div>'
            for _label, code, desc in meta["exceptions"]
        ) or '<div class="sig"><span>Raises no business exception. Records what happened.</span></div>'
        rows.append(
            f'<tr><td><div class="fn">{_e(meta["title"])}</div><div class="when">{_e(meta["timing"])}</div></td>'
            f'<td><div style="color:#C3D0CD;margin-bottom:0.8rem;line-height:1.55">{_e(meta["summary"])}</div>{sigs}</td></tr>'
        )
    st.html(f'<table class="rules">{"".join(rows)}</table>')


def render_access_matrix(roles, jobs, perms, active_role, fmt):
    head = "".join(
        f'<th class="{"cur" if r == active_role else ""}">{_e(fmt(r))}</th>' for r in roles
    )
    body = []
    for j in jobs:
        cells = []
        for r in roles:
            v = perms.get((r, j))
            mark = '<span class="y">&#10003;</span>' if v else ('<span class="n">&ndash;</span>')
            cells.append(f'<td class="{"cur" if r == active_role else ""}">{mark}</td>')
        body.append(f"<tr><td>{_e(j)}</td>{''.join(cells)}</tr>")
    st.html(
        f'<div class="matrix-scroll"><table class="matrix"><thead><tr><th>Operation</th>{head}</tr></thead>'
        f'<tbody>{"".join(body)}</tbody></table></div>'
    )


def render_build_notes():
    st.html(
        """
        <ul class="build-list">
          <li><b>Schema:</b> 6 interconnected core banking tables on Neon serverless PostgreSQL.</li>
          <li><b>RBAC matrix:</b> table and column-level GRANT privileges across the simulated roles.</li>
          <li><b>Trigger engine:</b> 4 PL/pgSQL triggers with deterministic exception signatures.</li>
          <li><b>Observability:</b> live trace and a before and after state diff viewer.</li>
          <li><b>Tests:</b> a 12-scenario automated suite, recorded by the author as fully passing.</li>
          <li><b>Stack:</b> PostgreSQL 16, Neon, PL/pgSQL, Python 3.13, Streamlit, Graphviz, psycopg2.</li>
        </ul>
        """
    )
