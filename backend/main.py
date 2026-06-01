from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import (
    get_candidate_nodes,
    get_patients,
    get_patient,
    get_users
)

from composition_pipeline import run_composition


app = FastAPI(
    title="Brahmo Composition Agent",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "Brahmo Composition Agent Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/candidate-nodes")
def candidate_nodes():

    rows = get_candidate_nodes()

    return [
        {
            "id": row["id"],
            "title": row["title"],
            "type": row["type"],
            "status": row["status"]
        }
        for row in rows
    ]


@app.get("/patients")
def patients():

    return get_patients()


@app.get("/patients/{patient_id}")
def patient(patient_id: str):

    return get_patient(patient_id)


@app.get("/users")
def users():

    return get_users()


@app.post("/compose")
def compose():

    result = run_composition()

    return {
        "total_tokens": result.total_tokens,
        "nodes_included": result.nodes_included,
        "nodes_omitted": result.nodes_omitted,
        "compression_passes": result.compression_passes,
        "compression_log": result.compression_log,
        "context": result.context_string
    }


@app.post("/compose/{budget}")
def compose_with_budget(budget: int):

    result = run_composition(budget)

    return {
        "budget": budget,
        "total_tokens": result.total_tokens,
        "nodes_included": result.nodes_included,
        "nodes_omitted": result.nodes_omitted,
        "compression_passes": result.compression_passes,
        "compression_log": result.compression_log,
        "context": result.context_string,
"blocks": [
    {
        "id": block.id,
        "name": block.name,
        "candidate_count": len(block.candidates),
        "token_count": block.token_count,

        "candidates": [
            {
                "id": c.id,
                "title": c.title,
                "type": c.type,
                "compression_level": c.compression_level,
                "retrieval_weight": c.retrieval_weight,
                "injection_weight": c.injection_weight,
                "distance": c.distance_from_entry,
            }
            for c in block.candidates
        ]
    }
    for block in result.blocks
]
    }