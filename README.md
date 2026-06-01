<h1 align="center">Brahmo Composition Agent</h1>

<p align="center">
An AI-driven Context Composition Engine that intelligently selects, prioritizes, compresses, and assembles contextual information within a constrained token budget while preserving critical safety and policy constraints.
</p>

---

<h2>Live Demo</h2>

<p>
<strong>Frontend:</strong><br>
<a href="YOUR_VERCEL_URL" target="_blank">
YOUR_VERCEL_URL
</a>
</p>

<p>
<strong>Backend API:</strong><br>
<a href="https://brahmo-composition-agent-production.up.railway.app" target="_blank">
https://brahmo-composition-agent-production.up.railway.app
</a>
</p>

---

<h2>Project Overview</h2>

<p>
Large Language Models operate within limited context windows and token budgets. In real-world systems, especially healthcare environments, contextual information often exceeds what can be provided to the model.
</p>

<p>
Brahmo Composition Agent solves this problem by retrieving candidate context nodes, scoring their importance, compressing lower-value content, preserving critical constraints, and assembling a final context optimized for LLM consumption.
</p>

---

<h2>Features</h2>

<h3>Context Composition Pipeline</h3>

<ul>
  <li>Candidate node retrieval</li>
  <li>Importance scoring engine</li>
  <li>Token counting and estimation</li>
  <li>Context compression</li>
  <li>Budget fitting</li>
  <li>Structured block assembly</li>
  <li>Final context generation</li>
</ul>

---

<h3>Token Budget Management</h3>

<ul>
  <li>Adjustable token budgets</li>
  <li>Real-time budget breakdown</li>
  <li>Context budget calculation</li>
  <li>Token usage visualization</li>
  <li>Compression tracking</li>
</ul>

---

<h3>Intelligent Prioritization</h3>

<ul>
  <li>Retrieval weight scoring</li>
  <li>Injection weight scoring</li>
  <li>Distance-based ranking</li>
  <li>Importance-based selection</li>
  <li>Priority-driven context inclusion</li>
</ul>

---

<h3>Constraint Preservation</h3>

<ul>
  <li>Protection of critical context nodes</li>
  <li>Safety-first composition strategy</li>
  <li>Clinical policy preservation</li>
  <li>Constraint-aware budget fitting</li>
  <li>Controlled omission of low-value content</li>
</ul>

---

<h3>Explainability & Transparency</h3>

<ul>
  <li>Included node tracking</li>
  <li>Omitted node tracking</li>
  <li>Compression timeline visualization</li>
  <li>Composition rationale viewer</li>
  <li>Final context inspection</li>
</ul>

---

<h2>Tech Stack</h2>

<h3>Frontend</h3>

<ul>
  <li>Next.js</li>
  <li>React</li>
  <li>TypeScript</li>
  <li>CSS</li>
</ul>

---

<h3>Backend</h3>

<ul>
  <li>FastAPI</li>
  <li>Python</li>
</ul>

---

<h3>Database</h3>

<ul>
  <li>Supabase</li>
</ul>

---

<h2>Deployment</h2>

<table>
  <tr>
    <th>Service</th>
    <th>Platform</th>
  </tr>

  <tr>
    <td>Frontend</td>
    <td>Vercel</td>
  </tr>

  <tr>
    <td>Backend</td>
    <td>Railway</td>
  </tr>

  <tr>
    <td>Database</td>
    <td>Supabase</td>
  </tr>
</table>

---

<h2>System Architecture</h2>

<pre>
Frontend (Next.js)
        │
        ▼
FastAPI Backend
        │
        ▼
Composition Pipeline
        │
 ┌──────┼──────┐
 ▼      ▼      ▼
Scoring Compression Budget Fitting
        │
        ▼
Context Assembly
        │
        ▼
Final Context
        │
        ▼
Supabase Database
</pre>

---

<h2>Project Structure</h2>

<pre>
BRAHMO-COMPOSITION-AGENT/
│
├── backend/
│   ├── composition/
│   ├── models/
│   ├── tests/
│   ├── composition_pipeline.py
│   ├── data_loader.py
│   ├── database.py
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   └── components/
│   ├── public/
│   └── package.json
│
└── README.md
</pre>

---

<h2>Installation & Setup</h2>

<h3>1️⃣ Clone Repository</h3>

<pre>
git clone https://github.com/Santhosh1040/BRAHMO-COMPOSITION-AGENT.git
</pre>

---

<h3>2️⃣ Backend Setup</h3>

<pre>
cd backend
pip install -r requirements.txt
</pre>

<h4>Create .env</h4>

<pre>
TOKEN_BUDGET=4000
SYSTEM_PROMPT_RESERVE=800
USER_MESSAGE_RESERVE=200

SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
</pre>

<h4>Run Backend</h4>

<pre>
uvicorn main:app --reload
</pre>

---

<h3>3️⃣ Frontend Setup</h3>

<pre>
cd frontend
npm install
</pre>

<h4>Create .env.local</h4>

<pre>
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
</pre>

<h4>Run Frontend</h4>

<pre>
npm run dev
</pre>

---

<h2>Budget Fitting Strategy</h2>

<p>
The composition engine prioritizes preservation of high-importance and constraint-protected nodes over strict budget compliance.
</p>

<p>
During context assembly, low-value content is aggressively compressed or omitted. However, critical safety constraints, policy requirements, and high-importance context are protected from removal.
</p>

<p>
As a result, the final context may occasionally exceed the target token budget when retaining critical information is deemed more important than achieving an exact budget threshold.
</p>

<p>
This design reflects a practical tradeoff commonly required in real-world healthcare systems where omission of critical context can be more harmful than a modest increase in token consumption.
</p>

---

<h2>Demo Highlights</h2>

<ul>
  <li>Context composition workflow</li>
  <li>Token-aware budget management</li>
  <li>Context compression engine</li>
  <li>Importance-based ranking</li>
  <li>Constraint preservation strategy</li>
  <li>Compression timeline visualization</li>
  <li>Composition rationale viewer</li>
  <li>Full-stack cloud deployment</li>
</ul>

---

<h2>Future Improvements</h2>

<ul>
  <li>Semantic embedding-based retrieval</li>
  <li>Adaptive compression using LLMs</li>
  <li>Advanced explainability metrics</li>
  <li>Multi-user workflow support</li>
  <li>Audit trail and decision logging</li>
</ul>

---

<h2>Conclusion</h2>

<p>
Brahmo Composition Agent demonstrates practical AI engineering concepts including context composition, token budget optimization, intelligent prioritization, constraint-aware reasoning, explainable AI workflows, cloud deployment, and full-stack system integration. The project showcases how critical contextual information can be preserved and efficiently delivered to Large Language Models operating under limited context windows.
</p>
