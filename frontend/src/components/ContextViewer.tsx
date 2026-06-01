type ContextViewerProps = {
  context: string;
};

export default function ContextViewer({
  context,
}: ContextViewerProps) {
  return (
    <div className="bg-white text-black p-6 rounded-xl shadow">

      <h2 className="text-2xl font-bold mb-4">
        Final Context
      </h2>

      <div className="border rounded-lg p-4 bg-gray-50 max-h-[700px] overflow-y-auto">

        <pre className="whitespace-pre-wrap text-sm text-black leading-relaxed">
          {context}
        </pre>

      </div>

    </div>
  );
}