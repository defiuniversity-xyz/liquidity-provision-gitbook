# Exercise 2: Mathematical Calculations and Analysis

⏰ Time Investment: 45-60 minutes
🎯 Goal: Master the mathematical foundations of AMMs through hands-on calculations

📚 Required Reading Integration
📖 Primary: Lesson 2: The Mathematics of Liquidity Provision
📖 Supporting: Lesson 1: Understanding AMM Fundamentals

## 🔢 Phase 1: Formula Mastery (15 minutes)



![Fee vs Gas Break-Even Calculator](https://storage.googleapis.com/liquidity-provision-gitbook-images/exercises/exercise_02/ex02_02_fee_vs_gas_break-even_calculator.png)



![Formula Mastery Checklist](https://storage.googleapis.com/liquidity-provision-gitbook-images/exercises/exercise_02/ex02_01_formula_mastery_checklist.png)

### Constant Product Formula Practice

**Exercise 1**: Complete the table

| ETH Reserves | USDC Reserves | k (constant) | Price (USDC/ETH) |
|--------------|---------------|--------------|-------------------|
| 10           | 20,000        | _____        | _____             |
| 11           | _____         | 200,000      | _____             |
| _____        | 18,181.82     | 200,000      | 2,000             |
| 9            | _____         | 200,000      | _____             |

### Price Impact Calculation

**Exercise 2**: Calculate price impact for different trade sizes

**Pool**: 100 ETH, 200,000 USDC (k = 20,000,000)

**Trade 1**: Buy 0.1 ETH
- New ETH: _____
- New USDC: _____
- Price impact: _____%

**Trade 2**: Buy 1 ETH
- New ETH: _____
- New USDC: _____
- Price impact: _____%

**Trade 3**: Buy 10 ETH
- New ETH: _____
- New USDC: _____
- Price impact: _____%

**Observation**: As trade size increases, price impact _____ (increases/decreases).

## 📊 Phase 2: Fee Mathematics (15 minutes)

### Fee Distribution Exercise

**Scenario**: 
- Pool TVL: $1,000,000
- Daily Volume: $500,000
- Fee Rate: 0.3%
- Your Capital: $10,000

**Calculate**:

**Step 1**: Your pool share
- Share = $10,000 ÷ $1,000,000 = _____%

**Step 2**: Daily fees generated
- Daily fees = $500,000 × 0.003 = $_____

**Step 3**: Your daily fee share
- Your fees = $_____ × _____% = $_____

**Step 4**: Monthly fees
- Monthly = $_____ × 30 = $_____

**Step 5**: Annual fees (before IL)
- Annual = $_____ × 12 = $_____

**Step 6**: APY calculation
- APY = ($_____ ÷ $10,000) × 100% = _____%

### Fee vs. Gas Analysis

**Scenario**: You're considering providing liquidity on Ethereum L1

**Setup**:
- Position: $5,000
- Expected monthly fees: $50
- Gas costs: $30 (deposit) + $20 (withdraw) = $50 total

**Analysis**:
- Net monthly return: $50 - $50 = $_____
- Is this profitable? _____ (Yes/No)
- Minimum position size for profitability: $_____ (assuming same fees)

**Conclusion**: For L1, you need positions >$_____ to be profitable.

## 🧮 Phase 3: Advanced Calculations (20 minutes)

### Liquidity Depth Comparison

**Exercise 3**: Compare three pools

**Pool A**: 20 ETH, 40,000 USDC
**Pool B**: 100 ETH, 200,000 USDC  
**Pool C**: 500 ETH, 1,000,000 USDC

**Calculate depth**:
- Depth_A = √(20 × 40,000) = √(_____) = _____
- Depth_B = √(_____ × _____) = √(_____) = _____
- Depth_C = √(_____ × _____) = √(_____) = _____

**Which pool can handle a $100,000 trade with least impact?**
- Answer: Pool _____

### Multi-Trade Analysis

**Exercise 4**: Calculate cumulative price impact

**Pool**: 100 ETH, 200,000 USDC (k = 20,000,000)
**Starting Price**: 2,000 USDC/ETH

**Trade Sequence**:
1. Buy 1 ETH → New price: _____
2. Buy 1 ETH → New price: _____
3. Buy 1 ETH → New price: _____

**Compare to single 3 ETH trade**:
- Single trade price: _____
- Cumulative price: _____
- Difference: _____

**Observation**: Splitting trades _____ (reduces/increases) price impact.

## 📈 Phase 4: Real-World Scenario (10 minutes)

### Complete Pool Analysis

**Scenario**: You're analyzing an ETH/USDC pool on Arbitrum

**Pool Data**:
- TVL: $5,000,000
- Daily Volume: $1,000,000
- Fee Rate: 0.05%
- Your Capital: $25,000
- Network: Arbitrum (L2)

**Calculate Expected Returns**:

**Daily Analysis**:
- Your share: _____%
- Daily fees: $_____
- Daily gas (amortized): $_____
- Net daily: $_____

**Monthly Analysis**:
- Monthly fees: $_____
- Monthly gas: $_____
- Net monthly: $_____

**Annual Analysis**:
- Annual fees: $_____
- Annual gas: $_____
- **Net annual: $_____**
- **APY: _____%** (before IL)

**Risk Assessment**:
- Minimum viable position: $_____ (based on gas costs)
- Your position is _____ (viable/not viable) for active management

## 🎯 Phase 5: Mastery Check (10 minutes)

### Self-Evaluation

**Rate your confidence (1-10)**:
- Calculating swap amounts: _____/10
- Understanding price impact: _____/10
- Fee distribution math: _____/10
- Liquidity depth concepts: _____/10
- Gas economics: _____/10

**Total**: _____/50

### Key Formulas Mastered

**Write from memory**:

**Constant Product Formula**:
- Formula: _____
- What does k represent? _____

**Price Calculation**:
- Formula: _____
- How does it change with trades? _____

**Fee Share**:
- Formula: _____
- What factors affect your share? _____

## 📚 Next Steps

- [ ] Practice calculations with different pool sizes
- [ ] Use online calculators to verify your work
- [ ] Explore Uniswap interface to see real calculations
- [ ] Move to Lesson 3 to understand IL (the hidden cost)

---

[← Back to Lesson 2](../lessons/lesson-02-mathematics-of-liquidity-provision.md) | [Next: Exercise 3 →](exercise-03-risk-assessment-and-il-analysis.md)

