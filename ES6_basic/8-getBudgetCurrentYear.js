export default function getBudgetForCurrentYear(year, income, gdp, capita) {
  const budget = {};

  budget[year + '-income'] = income;
  budget[year + '-gdp'] = gdp;
  budget[year + '-capita'] = capita;

  return budget;
}
