# Exercise 7: Fee Tier Selection and Gas Optimization

⏰ Time Investment: 45 minutes
🎯 Goal: Optimize fee tiers and minimize gas costs for maximum profitability

📚 Required Reading Integration
📖 Primary: Lesson 7: Fee Optimization and Gas Economics
📖 Supporting: Lesson 4: Building Your First LP Position

## 💰 Phase 1: Fee Tier Analysis (15 minutes)



![Gas Cost Comparison and Optimization](images/exercises/exercise_07/ex07_02_gas_cost_comparison_and_optimization.png)



![Fee Tier Selection Guide](images/exercises/exercise_07/ex07_01_fee_tier_selection_guide.png)

### Fee Tier Selection Exercise

**Exercise 1**: Choose appropriate fee tier for each pair

**Pair 1: USDC/USDT**
- Volatility: Very Low
- Recommended tier: _____%
- Why? _________________________________

**Pair 2: ETH/USDC**
- Volatility: High
- Recommended tier: _____%
- Why? _________________________________

**Pair 3: wstETH/ETH**
- Volatility: Low (correlated)
- Recommended tier: _____%
- Why? _________________________________

**Pair 4: MEME/USDC**
- Volatility: Very High
- Recommended tier: _____%
- Why? _________________________________

### Volume/TVL Ratio Calculation

**Exercise 2**: Calculate and compare pools

**Pool A: ETH/USDC 0.05%**
- TVL: $10,000,000
- Daily Volume: $2,000,000
- Ratio: $2M ÷ $10M = _____

**Pool B: ETH/USDC 0.3%**
- TVL: $50,000,000
- Daily Volume: $1,000,000
- Ratio: $1M ÷ $50M = _____

**Which pool generates more fees per dollar?** Pool _____
**Why?** _________________________________

## ⛽ Phase 2: Gas Economics (20 minutes)

### Gas Cost Analysis

**Exercise 3**: Calculate total gas costs

**Scenario**: $10,000 position on different networks

**Ethereum L1**:
- Add liquidity: $_____
- Collect fees (monthly): $_____ × 4 = $_____
- Remove liquidity: $_____
- **Total monthly: $_____**

**Arbitrum L2**:
- Add liquidity: $_____
- Collect fees (monthly): $_____ × 4 = $_____
- Remove liquidity: $_____
- **Total monthly: $_____**

**Base L2**:
- Add liquidity: $_____
- Collect fees (monthly): $_____ × 4 = $_____
- Remove liquidity: $_____
- **Total monthly: $_____**

### Break-Even Analysis

**Exercise 4**: Calculate minimum viable position

**Network: Ethereum L1**
- Monthly gas: $_____
- Expected fee rate: _____% APY
- Minimum position: $_____ ÷ (_____% ÷ 12) = $_____

**Network: Arbitrum**
- Monthly gas: $_____
- Expected fee rate: _____% APY
- Minimum position: $_____ ÷ (_____% ÷ 12) = $_____

**Network: Base**
- Monthly gas: $_____
- Expected fee rate: _____% APY
- Minimum position: $_____ ÷ (_____% ÷ 12) = $_____

**Conclusion**: For your $_____ position, use network _____.

## 📊 Phase 3: Fee Optimization Strategy (10 minutes)

### Complete Fee Analysis

**Your Position**: $25,000 ETH/USDC

**Option A: Uniswap V3 0.05% (Arbitrum)**
- TVL: $50M
- Daily Volume: $10M
- Your share: _____%
- Daily fees: $_____
- Monthly fees: $_____
- Gas: $_____
- Net: $_____

**Option B: Uniswap V3 0.3% (Arbitrum)**
- TVL: $20M
- Daily Volume: $5M
- Your share: _____%
- Daily fees: $_____
- Monthly fees: $_____
- Gas: $_____
- Net: $_____

**Option C: Aerodrome (Base)**
- TVL: $5M
- Daily Volume: $2M
- Fee: 0.05%
- Emissions: 1,000 AERO/week to pool
- Your share: _____%
- Daily fees: $_____
- Weekly emissions: _____ AERO = $_____
- Monthly total: $_____
- Gas: $_____
- Net: $_____

**Best Option**: Option _____
**Expected Monthly Return**: $_____
**APY**: _____%

## 🎯 Phase 4: Optimization Action Plan (10 minutes)

### Your Optimization Strategy

**Current Setup**:
- Positions: _________________________________
- Networks: _________________________________
- Fee tiers: _________________________________

**Optimization Opportunities**:
1. _________________________________
2. _________________________________
3. _________________________________

**Action Items**:
- [ ] Switch to L2 (if on L1 with <$25k)
- [ ] Optimize fee tiers (match to volatility)
- [ ] Improve Volume/TVL ratios
- [ ] Reduce gas costs (batch operations)
- [ ] Compare cross-protocol opportunities

### Gas Optimization Checklist

- [ ] Using L2 for positions <$25k
- [ ] Batching approvals and deposits
- [ ] Timing transactions (lower gas periods)
- [ ] Setting appropriate gas limits
- [ ] Collecting fees efficiently (not too frequent)

## 📚 Next Steps

- [ ] Analyze your actual positions for optimization
- [ ] Calculate gas costs for all operations
- [ ] Compare fee tiers across your positions
- [ ] Review Lesson 8 for risk management

---

[← Back to Lesson 7](../lessons/lesson-07-fee-optimization-and-gas-economics.md) | [Next: Exercise 8 →](exercise-08-advanced-risk-management-framework.md)

