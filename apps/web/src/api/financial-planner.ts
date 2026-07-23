export type TransactionType = 'income' | 'expense' | 'adjustment'

export interface PlanAnalysisRequest {
  start_date: string
  end_date: string
  opening_balance: string
  transactions: Array<{
    date: string
    amount: string
    type: TransactionType
    description: string
    category: string
  }>
}

export interface PlanAnalysisResponse {
  score: {
    overall: number
    liquidity: number
    reserve: number
    credit_dependency: number
    stability: number
    risk: number
  }
  liquidity: {
    minimum_balance: string
    maximum_balance: string
    ending_balance: string
    first_negative_day: string | null
    negative_days: number
    has_negative_balance: boolean
  }
  summary: string
  highlights: string[]
}

export async function analyzePlan(
  plan: PlanAnalysisRequest,
): Promise<PlanAnalysisResponse> {
  const response = await fetch('/api/v1/plans/analyze', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(plan),
  })

  if (!response.ok) {
    throw new Error('Não foi possível analisar o planejamento.')
  }

  return response.json() as Promise<PlanAnalysisResponse>
}
