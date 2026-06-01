from models.candidate import Candidate
from composition.budget_fitter import fit_to_budget

candidates = [

    Candidate(
        id="C-01",
        title="Warfarin Rule",
        type="CONSTRAINT",

        content_full="full",
        content_compressed="compressed",
        content_constraint_only="constraint",

        retrieval_weight=0.95,
        injection_weight=0.95,

        distance_from_entry=1,

        tokens_full=80,
        tokens_compressed=20,
        tokens_constraint_only=5
    ),

    Candidate(
        id="F-01",
        title="Bed Capacity",
        type="FACT",

        content_full="full",
        content_compressed="compressed",
        content_constraint_only="constraint",

        retrieval_weight=0.20,
        injection_weight=0.20,

        distance_from_entry=4,

        tokens_full=120,
        tokens_compressed=40,
        tokens_constraint_only=10
    ),

    Candidate(
        id="F-02",
        title="Nurse Ratio",
        type="FACT",

        content_full="full",
        content_compressed="compressed",
        content_constraint_only="constraint",

        retrieval_weight=0.25,
        injection_weight=0.25,

        distance_from_entry=4,

        tokens_full=100,
        tokens_compressed=30,
        tokens_constraint_only=5
    )
]

result = fit_to_budget(
    candidates=candidates,
    current_tokens=4200,
    budget=3000
)

print("Final Tokens:", result["tokens"])
print("Passes:", result["passes"])

print("\nCompression Log:\n")

for item in result["log"]:
    print(item)