# Exercise 5: V3 Range Selection and Management

⏰ Time Investment: 45-60 minutes
🎯 Goal: Master Uniswap V3 range selection and active position management

📚 Required Reading Integration
📖 Primary: Lesson 5: Concentrated Liquidity Mastery
📖 Supporting: Lesson 3: Impermanent Loss and Risk Fundamentals

## 🎯 Phase 1: Range Selection Strategy (20 minutes)



![Out-of-Range Decision Framework](https://storage.googleapis.com/liquidity-provision-gitbook-images/exercises/exercise_05/ex05_02_out-of-range_decision_framework.png)



![Range Selection Strategy Matrix](https://storage.googleapis.com/liquidity-provision-gitbook-images/exercises/exercise_05/ex05_01_range_selection_strategy_matrix.png)

### Range Width Decision Framework

**Scenario**: ETH/USDC pool, current price $2,000

**Exercise 1**: Calculate ranges for different strategies

**Strategy 1: Full Range (V2 equivalent)**
- Lower price: $_____
- Upper price: $_____
- Width: ±_____%
- Efficiency: _____x (similar to V2)

**Strategy 2: Wide Range**
- Lower price: $_____ (±20%)
- Upper price: $_____ (±20%)
- Width: _____%
- Efficiency: _____x

**Strategy 3: Medium Range**
- Lower price: $_____ (±10%)
- Upper price: $_____ (±10%)
- Width: _____%
- Efficiency: _____x

**Strategy 4: Narrow Range (Advanced)**
- Lower price: $_____ (±2%)
- Upper price: $_____ (±2%)
- Width: _____%
- Efficiency: _____x

### Risk vs. Efficiency Analysis

**For each strategy, assess**:

| Strategy | Efficiency | Risk Level | Rebalancing Frequency | Best For |
|----------|------------|------------|----------------------|----------|
| Full Range | _____ | _____ | _____ | _____ |
| Wide Range | _____ | _____ | _____ | _____ |
| Medium Range | _____ | _____ | _____ | _____ |
| Narrow Range | _____ | _____ | _____ | _____ |

**Your Choice**: Strategy _____
**Reasoning**: _________________________________

## 📊 Phase 2: Tick Calculation Practice (15 minutes)

### Understanding Ticks

**Exercise 2**: Convert prices to ticks (simplified)

**Current Price**: $2,000 ETH/USDC

**Price $1,800** (10% below):
- Price ratio: $1,800 ÷ $2,000 = _____
- Approximate tick: _____ (use Uniswap interface for exact)

**Price $2,200** (10% above):
- Price ratio: $2,200 ÷ $2,000 = _____
- Approximate tick: _____

**Your Range**:
- Lower tick: _____
- Upper tick: _____
- Tick spacing: _____ (based on fee tier)

### Fee Tier Selection

**Exercise 3**: Choose appropriate fee tier

**Pair: ETH/USDC**
- Volatility: High
- Recommended tier: _____%
- Tick spacing: _____

**Pair: USDC/USDT**
- Volatility: Very Low
- Recommended tier: _____%
- Tick spacing: _____

**Pair: wstETH/ETH**
- Volatility: Low (correlated)
- Recommended tier: _____%
- Tick spacing: _____

## 🔄 Phase 3: Position Management (15 minutes)

### Out-of-Range Response Protocol

**Scenario**: Your position goes out of range

**Current Position**:
- Range: $1,800 - $2,200
- Current price: $2,300 (above upper bound)
- Position: 100% USDC
- Fees earned: $0 (out of range)

**Decision Framework**:

**Option 1: Wait**
- Pros: _________________________________
- Cons: _________________________________
- When to use: _________________________________

**Option 2: Rebalance**
- New range: $_____ - $_____
- Gas cost: $_____
- Expected fees: $_____
- Profitable? _____ (Yes/No)

**Option 3: Withdraw**
- When appropriate: _________________________________
- Your decision: Option _____

### Rebalancing Calculation

**Exercise 4**: Calculate rebalancing needs

**Current Position**:
- Range: $1,800 - $2,200
- Current price: $2,100
- Position: 50% ETH, 50% USDC

**New Range** (centered on $2,100):
- Lower: $_____ (±10%)
- Upper: $_____ (±10%)

**Rebalancing Steps**:
1. Withdraw old position: Gas $_____
2. Swap to correct ratio: Gas $_____
3. Create new position: Gas $_____
4. Total gas: $_____

**Is rebalancing worth it?**
- Expected weekly fees: $_____
- Gas cost: $_____
- Break-even time: _____ weeks
- Decision: _____ (Rebalance/Wait)

## 📈 Phase 4: Fee Collection Strategy (10 minutes)

### Fee Collection Timing

**Scenario**: V3 position on Arbitrum

**Position Details**:
- Capital: $10,000
- Weekly fees: $10
- Gas to collect: $0.50

**Collection Frequency Analysis**:

**Daily Collection**:
- Weekly gas: $0.50 × 7 = $_____
- Net fees: $10 - $_____ = $_____
- Efficient? _____ (Yes/No)

**Weekly Collection**:
- Weekly gas: $_____
- Net fees: $10 - $_____ = $_____
- Efficient? _____ (Yes/No)

**Monthly Collection**:
- Monthly gas: $_____
- Monthly fees: $_____
- Net fees: $_____ - $_____ = $_____
- Efficient? _____ (Yes/No)

**Optimal Frequency**: _____ (Daily/Weekly/Monthly)

## 🎯 Phase 5: Complete V3 Position Plan (10 minutes)

### Your V3 Position Design

**Pair**: _____ / _____

**Range Selection**:
- Lower price: $_____
- Upper price: $_____
- Width: ±_____%
- Rationale: _________________________________

**Fee Tier**: _____%
**Tick Spacing**: _____

**Management Plan**:
- Monitoring frequency: _____ (Daily/Weekly)
- Rebalancing trigger: Price moves >_____%
- Fee collection: _____ (Daily/Weekly/Monthly)
- Out-of-range response: _____

**Risk Limits**:
- Maximum IL tolerance: _____%
- Gas cost limit: $_____ per month
- Rebalancing frequency: Max _____ per month

## 📚 Next Steps

- [ ] Set up V3 position on testnet
- [ ] Practice range selection with different scenarios
- [ ] Monitor a test position for 1 week
- [ ] Review Lesson 6 for multi-protocol strategies

---

[← Back to Lesson 5](../lessons/lesson-05-concentrated-liquidity-mastery.md) | [Next: Exercise 6 →](exercise-06-cross-protocol-analysis-and-selection.md)

