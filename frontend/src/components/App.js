import { useState } from "react";
import { analyzeBudget } from "./api";
import BudgetForm from "./components/BudgetForm";
import Dashboard from "./components/Dashboard";

export default function App() {
  const [data, setData] = useState(null);

  return (
    <div>
      <h1>Secure Budget Advisor</h1>
      <BudgetForm onSubmit={async payload => setData(await analyzeBudget(payload))} />
      <Dashboard data={data} />
    </div>
  );
}
