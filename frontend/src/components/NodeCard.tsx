type NodeCardProps = {
  title: string;
  type: string;
  compressionLevel: string;
  retrievalWeight: number;
  injectionWeight: number;
  distance: number;
};

export default function NodeCard({
  title,
  type,
  compressionLevel,
  retrievalWeight,
  injectionWeight,
  distance,
}: NodeCardProps) {

  const getCompressionColor = () => {
    switch (compressionLevel) {
      case "FULL":
        return "bg-green-100 text-green-700";

      case "COMPRESSED":
        return "bg-yellow-100 text-yellow-700";

      case "CONSTRAINT_ONLY":
        return "bg-orange-100 text-orange-700";

      case "OMIT":
        return "bg-red-100 text-red-700";

      default:
        return "bg-gray-100 text-gray-700";
    }
  };

  return (
    <div className="border rounded-lg p-4 bg-white shadow-sm hover:shadow-md transition">

      <div className="flex justify-between items-start mb-3">

        <h4 className="font-semibold text-gray-900">
          {title}
        </h4>

        <span
          className={`px-2 py-1 text-xs rounded-full font-medium ${getCompressionColor()}`}
        >
          {compressionLevel}
        </span>

      </div>

      <div className="grid grid-cols-2 gap-y-2 text-sm">

        <div>
          <span className="text-gray-500">
            Type:
          </span>{" "}
          {type}
        </div>

        <div>
          <span className="text-gray-500">
            Distance:
          </span>{" "}
          {distance}
        </div>

        <div>
          <span className="text-gray-500">
            Retrieval:
          </span>{" "}
          {retrievalWeight}
        </div>

        <div>
          <span className="text-gray-500">
            Injection:
          </span>{" "}
          {injectionWeight}
        </div>

      </div>

    </div>
  );
}