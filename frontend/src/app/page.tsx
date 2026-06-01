"use client";

import { useEffect, useState } from "react";

import Header from "../components/Header";
import StatsCards from "../components/StatsCards";
import CompressionTimeline from "../components/CompressionTimeline";
import ContextViewer from "../components/ContextViewer";
import BlockViewer from "../components/BlockViewer";
import BudgetBreakdown from "../components/BudgetBreakdown";
import ContextModal from "../components/ContextModal";
import RationaleModal from "../components/RationaleModal";

export default function Home() {
  const API_URL = process.env.NEXT_PUBLIC_API_URL!;
  const [users, setUsers] = useState<any[]>([]);
  const [patients, setPatients] = useState<any[]>([]);

  const [selectedUser, setSelectedUser] = useState("");
  const [selectedPatient, setSelectedPatient] = useState("");

  const [budget, setBudget] = useState(4000);

  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [showContextModal, setShowContextModal] =
  useState(false);
  const [showRationaleModal, setShowRationaleModal] =
  useState(false);

  useEffect(() => {
    loadUsers();
    loadPatients();
  }, []);

  const loadUsers = async () => {
    const res = await fetch(`${API_URL}/users`)
    const data = await res.json();

    setUsers(data);

    if (data.length > 0) {
      setSelectedUser(data[0].id);
    }
  };

  const loadPatients = async () => {
    const res = await fetch(`${API_URL}/patients`)
    const data = await res.json();

    setPatients(data);

    if (data.length > 0) {
      setSelectedPatient(data[0].id);
    }
  };
const composeContext = async () => {
  setLoading(true);

  try {
    const res = await fetch(
      `${API_URL}/compose/${budget}`,
      {
        method: "POST",
      }
    );

    const data = await res.json();

    setResult(data);
  } catch (error) {
    console.error("Compose failed:", error);
  } finally {
    setLoading(false);
  }
};

  return (
    <main className="min-h-screen bg-slate-100 text-black p-8">
      <div className="max-w-7xl mx-auto">

        <Header />

        {/* Controls */}
        <div className="bg-white text-black p-6 rounded-xl shadow-md mb-8">

          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">

            {/* User Selector */}
            <div>
              <label className="block mb-2 font-semibold">
                User
              </label>

              <select
                className="w-full border border-gray-300 rounded-lg p-3"
                value={selectedUser}
                onChange={(e) =>
                  setSelectedUser(e.target.value)
                }
              >
                {users.map((user) => (
                  <option
                    key={user.id}
                    value={user.id}
                  >
                    {user.name}
                  </option>
                ))}
              </select>
            </div>

            {/* Patient Selector */}
            <div>
              <label className="block mb-2 font-semibold">
                Patient
              </label>

              <select
                className="w-full border border-gray-300 rounded-lg p-3"
                value={selectedPatient}
                onChange={(e) =>
                  setSelectedPatient(e.target.value)
                }
              >
                {patients.map((patient) => (
                  <option
                    key={patient.id}
                    value={patient.id}
                  >
                    {patient.name}
                  </option>
                ))}
              </select>
            </div>
            {/* Token Budget */}
<div>
  <label className="block mb-2 font-semibold">
    Token Budget
  </label>

  <input
    type="range"
    min={2000}
    max={4000}
    step={100}
    value={budget}
    onChange={(e) => {
      setBudget(Number(e.target.value));
      setResult(null);
    }}
    className="w-full cursor-pointer"
  />

  <input
    type="number"
    min={2000}
    max={4000}
    step={100}
    value={budget}
    onChange={(e) => {
      setBudget(Number(e.target.value));
      setResult(null);
    }}
    className="w-full mt-3 border border-gray-300 rounded-lg p-3"
  />

  <p className="text-sm text-gray-500 mt-2">
    Range: 2000 - 4000 tokens
  </p>
</div>

          </div>

          <button
            onClick={composeContext}
            disabled={loading}
            className="mt-6 bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-lg font-medium cursor-pointer disabled:opacity-50"
          >
            {loading ? "Composing..." : "Compose Context"}
          </button>

        </div>

       {result && (
  <>
    <BudgetBreakdown
      budget={budget}
      contextTokens={result.total_tokens}
    />

    <BlockViewer
      blocks={result.blocks || []}
    />

    

    <StatsCards
      totalTokens={result.total_tokens}
      includedNodes={result.nodes_included}
      omittedNodes={result.nodes_omitted}
      compressionPasses={result.compression_passes}
    />

    <div className="flex gap-4 mb-6">

  <button
    onClick={() =>
      setShowContextModal(true)
    }
    className="bg-indigo-600 hover:bg-indigo-700 text-white px-4 py-2 rounded-lg cursor-pointer"
  >
    View Final Context
  </button>

  <button
    onClick={() =>
      setShowRationaleModal(true)
    }
    className="bg-purple-600 hover:bg-purple-700 text-white px-4 py-2 rounded-lg cursor-pointer"
  >
    View Composition Rationale
  </button>

</div>

    <div className="grid grid-cols-1 xl:grid-cols-2 gap-6">

      <ContextViewer
        context={result.context}
      />

      <CompressionTimeline
        compressionLog={
          result.compression_log || []
        }
      />

    </div>

    <ContextModal
      open={showContextModal}
      onClose={() =>
        setShowContextModal(false)
      }
      context={result.context}
    />
    <RationaleModal
  open={showRationaleModal}
  onClose={() =>
    setShowRationaleModal(false)
  }
  blocks={result.blocks || []}
/>
  </>
)}

      </div>
    </main>
  );
}