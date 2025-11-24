# Exercise 3: Risk Assessment and IL Analysis

⏰ Time Investment: 45-60 minutes
🎯 Goal: Master impermanent loss calculations and risk assessment

📚 Required Reading Integration
📖 Primary: Lesson 3: Impermanent Loss and Risk Fundamentals
📖 Supporting: Lesson 2: The Mathematics of Liquidity Provision

## 🔍 Phase 1: IL Calculation Practice (20 minutes)



![Risk Assessment Matrix](images/exercises/exercise_03/ex03_03_risk_assessment_matrix.png)



![IL vs Fees Break-Even Chart](images/exercises/exercise_03/ex03_02_il_vs_fees_break-even_chart.png)



![IL Calculation Worksheet](images/exercises/exercise_03/ex03_01_il_calculation_worksheet.png)

### Basic IL Scenarios

**Scenario**: You deposit 1 ETH + 2,000 USDC when ETH = $2,000
- Total value: $4,000
- Pool ratio: 50/50

**Exercise 1**: Calculate IL for different price movements

**Price Change: +25% (ETH → $2,500)**

**Step 1**: Calculate new pool ratio
- New price ratio: _____
- Your new position: _____ ETH + _____ USDC

**Step 2**: Calculate values
- LP position value: $_____
- Holding value: $_____
- IL: $_____ (_____%)

**Price Change: +50% (ETH → $3,000)**
- LP value: $_____
- Holding value: $_____
- IL: $_____ (_____%)

**Price Change: +100% (ETH → $4,000)**
- LP value: $_____
- Holding value: $_____
- IL: $_____ (_____%)

**Price Change: -50% (ETH → $1,000)**
- LP value: $_____
- Holding value: $_____
- IL: $_____ (_____%)

### IL Formula Application

**Exercise 2**: Use IL formula for price ratio r

**Formula**: IL% = 2 × (√r / (1 + r)) - 1

**Calculate for r = 1.5 (50% increase)**:
- IL% = 2 × (√1.5 / (1 + 1.5)) - 1
- IL% = 2 × (_____ / _____) - 1
- IL% = _____%

**Calculate for r = 2.0 (100% increase)**:
- IL% = _____

**Calculate for r = 0.5 (50% decrease)**:
- IL% = _____

## 📊 Phase 2: IL vs. Fees Analysis (15 minutes)

### Break-Even Analysis

**Scenario**: ETH/USDC pool
- Your capital: $10,000
- Daily volume: $100,000
- Fee rate: 0.3%
- Your share: 1%

**Calculate**:

**Daily Fees**:
- Daily fees = $100,000 × 0.003 × 0.01 = $_____

**Annual Fees** (before IL):
- Annual = $_____ × 365 = $_____

**IL Scenarios**:

**If ETH moves ±25%**:
- IL = 2% = $_____
- Net return = $_____ - $_____ = $_____
- Profitable? _____ (Yes/No)

**If ETH moves ±50%**:
- IL = 5.7% = $_____
- Net return = $_____ - $_____ = $_____
- Profitable? _____ (Yes/No)

**If ETH moves ±100%**:
- IL = 20% = $_____
- Net return = $_____ - $_____ = $_____
- Profitable? _____ (Yes/No)

**Conclusion**: This position is profitable only if ETH moves <_____%.

### Risk Assessment Matrix

**Exercise 3**: Assess risk for different pairs

| Pair | Volatility | Expected IL | Fees | Net Return | Risk Level |
|------|-----------|-------------|------|------------|------------|
| USDC/USDT | Low | _____% | _____% | _____% | _____ |
| wstETH/ETH | Medium | _____% | _____% | _____% | _____ |
| ETH/USDC | High | _____% | _____% | _____% | _____ |
| MEME/USDC | Very High | _____% | _____% | _____% | _____ |

## 💡 Phase 3: LVR Understanding (10 minutes)

### LVR vs. IL Comparison

**Key Differences**:

**Impermanent Loss**:
- Reversible? _____ (Yes/No)
- When does it occur? _____
- How to minimize? _____

**Loss Versus Rebalancing**:
- Reversible? _____ (Yes/No)
- When does it occur? _____
- How to minimize? _____

### LVR Impact Analysis

**Scenario**: High volatility pair (σ = 50% annual)

**LVR Formula**: LVR = σ² / 8

**Calculate**:
- LVR = (0.5)² / 8 = _____ / 8 = _____%

**Annual Impact**:
- On $10,000 position: $_____ lost to LVR
- This is _____ (reversible/irreversible)

**Conclusion**: In high volatility, LVR can exceed fees, making LPing unprofitable.

## 🎯 Phase 4: Risk Management Framework (15 minutes)

### Position Risk Assessment

**Your Portfolio**: $50,000 total

**Current Positions**:
- Position 1: $10,000 ETH/USDC (volatile)
- Position 2: $15,000 USDC/USDT (stable)
- Position 3: $10,000 wstETH/ETH (correlated)
- Position 4: $15,000 MEME/USDC (very volatile)

**Risk Analysis**:

**Position 1**:
- % of portfolio: _____%
- Risk level: _____
- Expected IL: _____%
- Within limits? _____ (Yes/No)

**Position 2**:
- % of portfolio: _____%
- Risk level: _____
- Expected IL: _____%
- Within limits? _____ (Yes/No)

**Position 3**:
- % of portfolio: _____%
- Risk level: _____
- Expected IL: _____%
- Within limits? _____ (Yes/No)

**Position 4**:
- % of portfolio: _____%
- Risk level: _____
- Expected IL: _____%
- Within limits? _____ (Yes/No)

**Portfolio Risk**:
- Total at risk: $_____
- % of portfolio: _____%
- Diversified? _____ (Yes/No)
- Risk limits met? _____ (Yes/No)

### Risk Mitigation Plan

**Identify your highest risk position**: Position _____

**Mitigation strategies**:
1. _________________________________
2. _________________________________
3. _________________________________

**Action items**:
- [ ] Reduce position size to _____%
- [ ] Switch to lower volatility pair
- [ ] Implement hedging strategy
- [ ] Set IL alert at _____%

## 📚 Next Steps

- [ ] Calculate IL for your actual positions
- [ ] Set up IL monitoring (APY.vision recommended)
- [ ] Review risk limits monthly
- [ ] Practice IL calculations with different scenarios

---

[← Back to Lesson 3](../lessons/lesson-03-impermanent-loss-and-risk-fundamentals.md) | [Next: Exercise 4 →](exercise-04-first-position-setup-and-management.md)

