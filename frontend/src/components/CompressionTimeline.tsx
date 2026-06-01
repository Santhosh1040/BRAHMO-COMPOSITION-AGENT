type CompressionTimelineProps = {
  compressionLog: string[];
};

export default function CompressionTimeline({
  compressionLog,
}: CompressionTimelineProps) {
  return (
    <div className="bg-white text-black p-6 rounded-xl shadow">

      <h2 className="text-2xl font-bold mb-4">
        Compression Timeline
      </h2>

      <div className="border rounded-lg p-4 bg-gray-50 max-h-[700px] overflow-y-auto">

        {compressionLog?.length > 0 ? (

          <div className="space-y-3">

            {compressionLog.map(
              (entry, index) => (

                <div
                  key={index}
                  className="border-l-4 border-blue-500 pl-4 py-2 bg-white rounded"
                >
                  <p className="text-sm text-gray-800">
                    {entry}
                  </p>
                </div>

              )
            )}

          </div>

        ) : (

          <p className="text-gray-500">
            No compression was required.
          </p>

        )}

      </div>

    </div>
  );
}