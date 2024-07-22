export default function getBudgetForCurrentYear(year,income, gdp, capita) {
  const budget = {
  [`${year}-income`]: income,
  [`${year}-gdp`]: gdp,
  [`${year}-capita`]: capita
  };
  return budget;
}
