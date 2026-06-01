type StatsCardsProps = {
  totalTokens: number;
  includedNodes: number;
  omittedNodes: number;
  compressionPasses: number;
};

export default function StatsCards({
  totalTokens,
  includedNodes,
  omittedNodes,
  compressionPasses,
}: StatsCardsProps) {
  return (
    <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">

      <div className="bg-white p-5 rounded-xl shadow">
        <h3 className="text-gray-500 text-sm">
          Total Tokens
        </h3>

        <p className="text-3xl font-bold mt-2">
          {totalTokens}
        </p>
      </div>

      <div className="bg-white p-5 rounded-xl shadow">
        <h3 className="text-gray-500 text-sm">
          Included Nodes
        </h3>

        <p className="text-3xl font-bold mt-2">
          {includedNodes}
        </p>
      </div>

      <div className="bg-white p-5 rounded-xl shadow">
        <h3 className="text-gray-500 text-sm">
          Omitted Nodes
        </h3>

        <p className="text-3xl font-bold mt-2">
          {omittedNodes}
        </p>
      </div>

      <div className="bg-white p-5 rounded-xl shadow">
        <h3 className="text-gray-500 text-sm">
          Compression Passes
        </h3>

        <p className="text-3xl font-bold mt-2">
          {compressionPasses}
        </p>
      </div>

    </div>
  );
}