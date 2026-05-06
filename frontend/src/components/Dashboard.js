export default function Dashboard({ data }) {
  if (!data) return null;

  return (
    <div>
      <h3>Budget</h3>
      <p>Remaining: £{data.monthly_remaining}</p>

      <h3>Recommendation</h3>
      <p>{data.recommendation}</p>

      <h3>Risk</h3>
      <p>{data.risk}</p>
    </div>
  );
}
