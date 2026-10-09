# DBMS RBAC Simulator & Trigger Visualizer - Frontend Export

This directory contains the exact frontend files extracted from the application.

---

## Structure

```
frontend/
├── index.html                   # Clean, standalone HTML matching your live dashboard UI
├── styles.css                   # Complete design system (Inter, JetBrains Mono, glassmorphism)
├── app.js                       # Interactive JavaScript (Role switching, tabs, live trace stepper)
└── streamlit_static_bundle/     # Raw compiled React / Vite assets from DevTools (index.html, JS chunks)
```

---

## 1. Clean Standalone Frontend (`index.html`, `styles.css`, `app.js`)

- **Zero dependencies**: No Python, no Node.js, and no Streamlit required.
- **How to view**: Simply double-click [`frontend/index.html`](./index.html) or open it in any web browser (Chrome, Edge, Firefox, Safari).
- **Features included**:
  - **Dynamic Sidebar**: Live role switching across all 9 banking roles with active badges and descriptions.
  - **Top Branding Ribbon**: Gradient typography and dynamic status badge (`● POSTGRESQL ONLINE`).
  - **5 Interactive Navigation Tabs**:
    1. *Banking Operations & Simulator* (KPI ribbon, Operation dropdown, Red/Green RBAC alert, Stepper pipeline)
    2. *Trigger Code for Selected Operation* (Interactive code tabs for all 4 procedural triggers)
    3. *In-Engine Trigger Theory & Buffers* (3-Tier Defense-in-Depth cards)
    4. *Role-Specific Execution Flowchart* (Vector flowchart diagram)
    5. *Exam Lab & AI Evaluator* (Practice questions and SQL code editor)
  - **Deployable Anywhere**: Can be uploaded directly to GitHub Pages, Vercel, Netlify, Apache, or Nginx.

---

## 2. Raw Streamlit Static Bundle (`streamlit_static_bundle/`)

- Contains the exact compiled build files inspected in your browser's DevTools:
  - `index.html` (the root HTML template with module preloads)
  - `static/js/` (compiled React / Rolldown / Emotion runtime chunks)
  - `static/media/` (custom fonts and icons)
