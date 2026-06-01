type Candidate = {
  id: string;
  title: string;
  compression_level: string;
  retrieval_weight: number;
  injection_weight: number;
  distance: number;
};

type Props = {
  blocks: any[];
};

export default function CompositionRationale({
  blocks,
}: Props) {

  const candidates =
    blocks.flatMap(
      (block) => block.candidates || []
    );

  return (
    <div className="bg-white rounded-xl shadow p-6 mb-8">

      <h2 className="text-xl font-bold mb-4">
        Composition Rationale
      </h2>

      <div className="space-y-4">

        {candidates.map((candidate: Candidate) => {

          let reason = "";

          if (
            candidate.compression_level === "FULL"
          ) {
            reason =
              `Included because retrieval score (${candidate.retrieval_weight}) and injection score (${candidate.injection_weight}) are high.`;
          }

          else if (
            candidate.compression_level === "COMPRESSED"
          ) {
            reason =
              `Compressed due to medium relevance and budget optimization.`;
          }

          else if (
            candidate.compression_level ===
            "CONSTRAINT_ONLY"
          ) {
            reason =
              `Reduced to constraints-only to save tokens while preserving critical rules.`;
          }

          else {
            reason =
              `Omitted because relevance was low relative to budget.`;
          }

          return (
            <div
              key={candidate.id}
              className="border rounded-lg p-4"
            >
              <h4 className="font-semibold">
                {candidate.title}
              </h4>

              <p className="text-sm text-gray-600 mt-2">
                {reason}
              </p>
            </div>
          );
        })}

      </div>

    </div>
  );
}