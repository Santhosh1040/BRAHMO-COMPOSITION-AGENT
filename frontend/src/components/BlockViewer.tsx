"use client";

import { useState } from "react";
import NodeCard from "./NodeCard";

type Candidate = {
  id: string;
  title: string;
  type: string;
  compression_level: string;
  retrieval_weight: number;
  injection_weight: number;
  distance: number;
};

type Block = {
  id: number;
  name: string;
  token_count: number;
  candidate_count: number;
  candidates: Candidate[];
};

type Props = {
  blocks: Block[];
};

export default function BlockViewer({
  blocks,
}: Props) {
  const [openBlock, setOpenBlock] =
    useState<number | null>(null);

  return (
    <div className="bg-white rounded-xl shadow p-6 mb-8">

      <h2 className="text-xl font-bold mb-4">
        Context Blocks
      </h2>

      <div className="space-y-3">

        {blocks.map((block) => (
          <div
            key={block.id}
            className="border border-gray-200 rounded-lg overflow-hidden"
          >

            <button
              onClick={() =>
                setOpenBlock(
                  openBlock === block.id
                    ? null
                    : block.id
                )
              }
              className="w-full flex items-center justify-between p-4 font-semibold hover:bg-gray-50 transition cursor-pointer"
            >

              <div className="flex items-center gap-2">

                <span className="text-lg">
                  {openBlock === block.id
                    ? "▼"
                    : "▶"}
                </span>

                <span>
                  Block {block.id} — {block.name}
                </span>

              </div>

              <div className="text-right text-sm text-gray-600">
  <div>
    {block.candidate_count} nodes
  </div>

  <div>
    {block.token_count} tokens
  </div>
</div>

            </button>

            {openBlock === block.id && (

              <div className="border-t bg-gray-50 p-4">

                {block.candidates.length === 0 ? (

                  <p className="text-gray-500 text-sm">
                    No candidates in this block.
                  </p>

                ) : (

                  <div className="space-y-3">

                    {block.candidates.map(
                      (candidate) => (
                        <NodeCard
                          key={candidate.id}
                          title={candidate.title}
                          type={candidate.type}
                          compressionLevel={
                            candidate.compression_level
                          }
                          retrievalWeight={
                            candidate.retrieval_weight
                          }
                          injectionWeight={
                            candidate.injection_weight
                          }
                          distance={
                            candidate.distance
                          }
                        />
                      )
                    )}

                  </div>

                )}

              </div>

            )}

          </div>
        ))}

      </div>

    </div>
  );
}