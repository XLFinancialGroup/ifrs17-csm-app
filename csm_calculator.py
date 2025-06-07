# csm_calculator.py

def present_value(cash_flows, discount_rate):
    return sum(cf / ((1 + discount_rate) ** t) for t, cf in enumerate(cash_flows, start=1))

def calculate_ifrs17_csm(premium_inflows, benefit_outflows, expense_outflows,
                         discount_rate=0.03, risk_adj_percentage=0.1):
    pv_inflows = present_value(premium_inflows, discount_rate)
    pv_outflows = present_value(benefit_outflows, discount_rate) + present_value(expense_outflows, discount_rate)
    risk_adjustment = risk_adj_percentage * pv_outflows
    csm = pv_inflows - pv_outflows - risk_adjustment
    return {
        "PV of Inflows": round(pv_inflows, 2),
        "PV of Outflows": round(pv_outflows, 2),
        "Risk Adjustment": round(risk_adjustment, 2),
        "CSM at Initial Recognition": round(csm, 2)
    }
