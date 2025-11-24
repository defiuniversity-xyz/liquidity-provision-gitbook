# Exercise 1: AMM Fundamentals Assessment

⏰ Time Investment: 30-45 minutes
🎯 Goal: Test your understanding of AMM basics and identify knowledge gaps

📚 Required Reading Integration
📖 Primary: Lesson 1: Understanding AMM Fundamentals
📖 Supporting: Lesson 2: The Mathematics of Liquidity Provision

## 🔍 Phase 1: Knowledge Check (10 minutes)

### Understanding Check

Answer these questions to assess your comprehension:

**1. What is the constant product formula?**
   - Your answer: _________________________________

**2. How does an AMM determine prices?**
   - Your answer: _________________________________

**3. What happens to pool reserves when someone buys ETH?**
   - Your answer: _________________________________

**4. Why are liquidity pools called "automated" market makers?**
   - Your answer: _________________________________

**5. What is the difference between marginal price and average price?**
   - Your answer: _________________________________

## 📊 Phase 2: Calculation Practice (15 minutes)

### Swap Calculation Exercise

**Scenario**: Pool has 100 ETH and 200,000 USDC
- Current price: 2,000 USDC per ETH
- k = 100 × 200,000 = 20,000,000
- Fee rate: 0.3%

**Exercise 1**: Calculate how much USDC is needed to buy 1 ETH

**Step 1**: New ETH reserves after trade
- ETH_new = 100 + 1 = _____ ETH



![Swap Calculation Template](images/exercises/exercise_01/ex01_02_swap_calculation_template.png)



![AMM Knowledge Assessment Chart](images/exercises/exercise_01/ex01_01_amm_knowledge_assessment_chart.png)

**Step 2**: Required USDC to maintain k
- USDC_new = 20,000,000 ÷ _____ = _____ USDC

**Step 3**: USDC needed (before fee)
- USDC_needed = 200,000 - _____ = _____ USDC

**Step 4**: Add 0.3% fee
- Fee = _____ × 0.003 = _____ USDC
- Total cost = _____ + _____ = _____ USDC

**Step 5**: Effective price
- Effective price = _____ USDC per ETH
- Price impact = (_____ - 2,000) ÷ 2,000 = _____%

### Pool Depth Exercise

**Scenario**: Two pools for ETH/USDC

**Pool A**: 50 ETH, 100,000 USDC (k = 5,000,000)
**Pool B**: 200 ETH, 400,000 USDC (k = 80,000,000)

**Exercise 2**: Which pool can handle larger trades with less price impact?

**Calculate depth for Pool A**:
- Depth_A = √(5,000,000) = _____

**Calculate depth for Pool B**:
- Depth_B = √(80,000,000) = _____

**Answer**: Pool _____ has more depth and can handle larger trades.

## 💡 Phase 3: Real-World Application (10 minutes)

### Pool Selection Exercise

You have $5,000 to provide liquidity. Analyze these pools:

**Pool 1**: ETH/USDC
- TVL: $10,000,000
- Daily Volume: $2,000,000
- Fee Rate: 0.05%

**Pool 2**: USDC/USDT
- TVL: $50,000,000
- Daily Volume: $1,000,000
- Fee Rate: 0.01%

**Pool 3**: MEME/USDC
- TVL: $500,000
- Daily Volume: $100,000
- Fee Rate: 1%

**Analysis**:

**Pool 1**:
- Your share: $5,000 ÷ $10,000,000 = _____%
- Daily fees: $2,000,000 × 0.0005 × _____ = $_____
- Volume/TVL ratio: $2,000,000 ÷ $10,000,000 = _____

**Pool 2**:
- Your share: $5,000 ÷ $50,000,000 = _____%
- Daily fees: $1,000,000 × 0.0001 × _____ = $_____
- Volume/TVL ratio: $1,000,000 ÷ $50,000,000 = _____

**Pool 3**:
- Your share: $5,000 ÷ $500,000 = _____%
- Daily fees: $100,000 × 0.01 × _____ = $_____
- Volume/TVL ratio: $100,000 ÷ $500,000 = _____

**Which pool would you choose and why?**
- Your choice: Pool _____
- Reasoning: _________________________________

## 🎯 Phase 4: Self-Assessment (10 minutes)

### Knowledge Score

Rate your understanding (1-10) on each topic:

**AMM Fundamentals**:
- Constant product formula: _____/10
- Price determination: _____/10
- Swap mechanics: _____/10
- Pool depth: _____/10
- Fee calculation: _____/10

**Total Score**: _____/50

### Gap Identification

**Topics I need to review**:
1. _________________________________
2. _________________________________
3. _________________________________

**Questions I still have**:
1. _________________________________
2. _________________________________
3. _________________________________

## 📚 Next Steps

- [ ] Review Lesson 1 sections where you scored <7/10
- [ ] Practice swap calculations with different scenarios
- [ ] Explore Uniswap interface (testnet recommended)
- [ ] Read Lesson 2 for deeper mathematical understanding

---

[← Back to Lesson 1](../lessons/lesson-01-understanding-amm-fundamentals.md) | [Next: Exercise 2 →](exercise-02-mathematical-calculations-and-analysis.md)

