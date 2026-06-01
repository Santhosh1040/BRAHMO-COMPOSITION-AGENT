type Props = {
  open: boolean;
  onClose: () => void;
  context: string;
};

export default function ContextModal({
  open,
  onClose,
  context,
}: Props) {

  if (!open) return null;

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">

      <div className="bg-white w-[90%] max-w-5xl rounded-xl p-6">

        <div className="flex justify-between mb-4">

          <h2 className="text-xl font-bold">
            Final Context
          </h2>

          <button
            onClick={onClose}
            className="cursor-pointer"
          >
            ✕
          </button>

        </div>

        <textarea
          value={context}
          readOnly
          className="w-full h-[500px] border rounded p-3 font-mono text-sm"
        />

      </div>

    </div>
  );
}