type BudgetBreakdownProps = {
  budget: number;
  contextTokens: number;
};

export default function BudgetBreakdown({
  budget,
  contextTokens,
}: BudgetBreakdownProps) {
  const systemTokens = 800;
  const userTokens = 200;

  const availableContext =
    budget - systemTokens - userTokens;

  return (
    <div className="bg-white p-6 rounded-xl shadow mb-8">

      <h2 className="text-xl font-bold mb-4">
        Budget Breakdown
      </h2>

      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">

        <div>
          <p className="text-gray-500 text-sm">
            Total Budget
          </p>

          <p className="text-2xl font-bold">
            {budget}
          </p>
        </div>

        <div>
          <p className="text-gray-500 text-sm">
            System Prompt
          </p>

          <p className="text-2xl font-bold">
            {systemTokens}
          </p>
        </div>

        <div>
          <p className="text-gray-500 text-sm">
            User Message
          </p>

          <p className="text-2xl font-bold">
            {userTokens}
          </p>
        </div>

        <div>
          <p className="text-gray-500 text-sm">
            Context Budget
          </p>

          <p className="text-2xl font-bold">
            {availableContext}
          </p>
        </div>

      </div>

      <div className="mt-6">

        <div className="flex justify-between text-sm mb-2">
          <span>Actual Context</span>
          <span>{contextTokens} tokens</span>
        </div>

        <div className="w-full h-4 bg-gray-200 rounded">

          <div
            className={`h-4 rounded ${
              contextTokens <= availableContext
                ? "bg-green-500"
                : "bg-red-500"
            }`}
            style={{
              width: `${Math.min(
                (contextTokens /
                  Math.max(availableContext, 1)) *
                  100,
                100
              )}%`,
            }}
          />

        </div>

      </div>

    </div>
  );
}