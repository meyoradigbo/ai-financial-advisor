import { useState } from "react";

export default function BudgetForm({ onSubmit }) {
  const [form, setForm] = useState({ income: "", expenses: "", goals: "" });

  return (
    <form onSubmit={e => { e.preventDefault(); onSubmit(form); }}>
      <input placeholder="Income" onChange={e => setForm({...form, income: Number(e.target.value)})} />
      <input placeholder="Expenses" onChange={e => setForm({...form, expenses: Number(e.target.value)})} />
      <input placeholder="Goals" onChange={e => setForm({...form, goals: Number(e.target.value)})} />
      <button>Analyse</button>
    </form>
  );
}
