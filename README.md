<!DOCTYPE html>
<html>
<head>
    <title>Brahmo Composition Agent</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 1100px;
            margin: auto;
            padding: 20px;
            line-height: 1.6;
        }

        h1, h2, h3 {
            color: #1e40af;
        }

        code {
            background: #f4f4f4;
            padding: 2px 5px;
            border-radius: 4px;
        }

        pre {
            background: #f4f4f4;
            padding: 15px;
            overflow-x: auto;
            border-radius: 6px;
        }

        .section {
            margin-bottom: 30px;
        }
    </style>
</head>
<body>

<h1>Brahmo Composition Agent</h1>

<p>
An AI-driven context composition engine that intelligently selects,
compresses, prioritizes, and assembles contextual information within a
limited token budget while preserving critical safety constraints.
</p>

<div class="section">
    <h2>Project Overview</h2>

    <p>
        Large Language Models have limited context windows.
        The Brahmo Composition Agent addresses this problem by constructing
        high-quality contextual prompts from large collections of candidate nodes.
    </p>

    <p>
        The system prioritizes important information, compresses low-value
        content, preserves safety-critical constraints, and produces a
        final context suitable for LLM consumption.
    </p>
</div>

<div class="section">
    <h2>Key Features</h2>

    <ul>
        <li>Importance-based candidate ranking</li>
        <li>Token-aware context assembly</li>
        <li>Compression pipeline</li>
        <li>Budget fitting engine</li>
        <li>Constraint preservation</li>
        <li>Context block generation</li>
        <li>Compression timeline visualization</li>
        <li>Composition rationale viewer</li>
        <li>Supabase integration</li>
        <li>Real-time frontend dashboard</li>
    </ul>
</div>

<div class="section">
    <h2>Architecture</h2>

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

</div>

<div class="section">
    <h2>Technology Stack</h2>

    <h3>Frontend</h3>
    <ul>
        <li>Next.js</li>
        <li>React</li>
        <li>TypeScript</li>
    </ul>

    <h3>Backend</h3>
    <ul>
        <li>FastAPI</li>
        <li>Python</li>
    </ul>

    <h3>Database</h3>
    <ul>
        <li>Supabase</li>
    </ul>

    <h3>Deployment</h3>
    <ul>
        <li>Railway (Backend)</li>
        <li>Vercel (Frontend)</li>
    </ul>
</div>

<div class="section">
    <h2>Composition Pipeline</h2>

    <ol>
        <li>Retrieve candidate nodes from Supabase.</li>
        <li>Calculate importance scores.</li>
        <li>Estimate token usage.</li>
        <li>Compress low-value nodes.</li>
        <li>Remove low-priority content when required.</li>
        <li>Preserve critical constraints.</li>
        <li>Assemble context blocks.</li>
        <li>Generate final context.</li>
    </ol>
</div>

<div class="section">
    <h2>Budget Fitting Strategy</h2>

    <p>
        The composition engine prioritizes preservation of
        high-importance and constraint-protected nodes over
        strict budget compliance.
    </p>

    <p>
        During context assembly, low-value content is aggressively
        compressed or omitted. However, critical safety constraints,
        policy requirements, and high-importance context are protected
        from removal.
    </p>

    <p>
        As a result, the final context may occasionally exceed the
        target token budget when retaining critical information is
        deemed more important than achieving an exact token threshold.
    </p>

    <p>
        This design reflects a practical tradeoff commonly required in
        real-world healthcare systems, where omission of critical
        information can be more harmful than a modest increase in token usage.
    </p>
</div>

<div class="section">
    <h2>Deployment URLs</h2>

    <p><strong>Frontend:</strong> [Add your Vercel URL]</p>
    <p><strong>Backend:</strong> https://brahmo-composition-agent-production.up.railway.app</p>
</div>

<div class="section">
    <h2>Future Improvements</h2>

    <ul>
        <li>Advanced semantic ranking</li>
        <li>Dynamic compression policies</li>
        <li>Multi-user support</li>
        <li>Audit trail and explainability enhancements</li>
        <li>LLM integration for adaptive compression</li>
    </ul>
</div>

</body>
</html>
