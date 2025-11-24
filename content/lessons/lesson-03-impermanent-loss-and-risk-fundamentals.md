# Lesson 3: Impermanent Loss and Risk Fundamentals

## 🎯 Core Concept: The Hidden Cost of Liquidity Provision

Impermanent Loss (IL) is the **single biggest risk** most liquidity providers don't understand. It's called "impermanent" because it only becomes permanent when you withdraw, but the reality is: **most LPs lose money to IL, even when earning fees**.

### The Brutal Truth

Many LPs see "100% APY" and think they're making money. But when they account for impermanent loss, they discover they would have been better off just holding their tokens. Understanding IL is the difference between profitable and unprofitable liquidity provision.

## 💸 What is Impermanent Loss?

### Simple Definition

**Impermanent Loss** = The difference between:
- What your LP position is worth
- What your tokens would be worth if you just held them

**Key Point**: IL occurs when the price ratio of the two tokens changes from when you deposited.

### Why It Happens

AMMs automatically rebalance your position as prices change:
- When Token A goes up → The pool sells your Token A to buy Token B
- When Token A goes down → The pool buys more Token A with your Token B

**The Problem**: You're always selling winners and buying losers. This is the opposite of what profitable traders do.

## 📊 Impermanent Loss: Step-by-Step Example

### Scenario Setup

You deposit liquidity when:
- ETH price: $2,000
- You deposit: 1 ETH + 2,000 USDC
- Total value: $4,000

### What Happens When ETH Rises to $2,500

**Step 1**: External market moves
- ETH price on Binance: $2,500 (25% increase)

**Step 2**: Arbitrageurs act
- They see ETH is "cheap" in your pool ($2,000)
- They buy ETH from your pool, adding USDC
- Pool price adjusts to $2,500

**Step 3**: Your position rebalances
- Pool automatically sold some of your ETH
- You now have: ~0.894 ETH + ~2,236 USDC
- New value: (0.894 × $2,500) + $2,236 = $4,471

**Step 4**: Compare to holding
- If you just held: 1 ETH + 2,000 USDC
- Holding value: (1 × $2,500) + $2,000 = $4,500
- **IL = $4,500 - $4,471 = $29 (0.65%)**

### What Happens When ETH Drops to $1,500

**Step 1**: ETH price falls 25% to $1,500

**Step 2**: Arbitrageurs buy "cheap" USDC
- They add ETH, remove USDC from pool
- Pool price adjusts to $1,500

**Step 3**: Your position rebalances
- Pool automatically bought more ETH with your USDC
- You now have: ~1.155 ETH + ~1,732 USDC
- New value: (1.155 × $1,500) + $1,732 = $4,465

**Step 4**: Compare to holding
- If you just held: 1 ETH + 2,000 USDC
- Holding value: (1 × $1,500) + $2,000 = $3,500
- **IL = $3,500 - $4,465 = -$965 (negative IL = you're better off!)**

Wait, that doesn't make sense! Let me recalculate...

Actually, when price drops, you have:
- LP value: $4,465
- Holding value: $3,500
- **IL = $3,500 - $4,465 = -$965**

But this is misleading. The real comparison:
- You started with: $4,000
- LP position now: $4,465 (up 11.6%)
- Holding would be: $3,500 (down 12.5%)

So you're actually **better off** in the LP when price drops? No—let's think about this correctly.

**Correct Calculation**:
- You started with: 1 ETH ($2,000) + 2,000 USDC = $4,000
- After 25% drop: 1 ETH ($1,500) + 2,000 USDC = $3,500
- LP position: 1.155 ETH ($1,732.50) + 1,732 USDC = $3,464.50
- **IL = $3,500 - $3,464.50 = $35.50 (1.0%)**

You still lost money compared to holding, just less than if you held only ETH.


![IL Mechanism Step-by-Step](images/lessons/lesson_03/lp03_03_il_mechanism_step-by-step.png)


## 📈 The Impermanent Loss Formula

### Mathematical Formula

For a price change of **r** (where r = new_price / old_price):

$$IL\% = 2 \times \frac{\sqrt{r} - 1}{1 + r} - (r - 1) \times \frac{1}{1 + r}$$

**Simplified for equal value deposits**:

$$IL\% = 2 \times \frac{\sqrt{r}}{1 + r} - 1$$

### IL Table: Price Changes vs. Loss

| Price Change | Impermanent Loss |
|--------------|------------------|
| ±5%          | 0.1%             |
| ±10%         | 0.5%             |
| ±25%         | 2.0%             |
| ±50%         | 5.7%             |
| ±100% (2x)   | 20.0%            |
| ±300% (4x)   | 50.0%            |

**Key Insight**: IL grows exponentially with price divergence. A 2x price move causes 20% IL. A 4x move causes 50% IL!

### Visual Representation

![Impermanent Loss Curve](images/lessons/lesson_03/lp03_01_impermanent_loss_curve.png)

The curve shows:
- IL is symmetric (same loss for +50% and -50% moves)
- IL increases faster as price moves further
- IL is always negative (you lose compared to holding)

## ⚠️ When IL Becomes Permanent

**Impermanent Loss** becomes **Permanent Loss** when you:
1. Withdraw your liquidity while prices are divergent
2. Realize the loss by converting back to your original tokens

**Example**:
- You deposit at ETH = $2,000
- ETH rises to $3,000 (50% increase)
- IL = 5.7% ($228 on $4,000 position)
- You withdraw: **Loss is now permanent**
- If you wait and ETH returns to $2,000: IL disappears

**The Catch**: Most LPs withdraw during volatility (when IL is highest), locking in losses.

## 🔄 IL vs. Fees: The Break-Even Analysis

### The Critical Question

**Do fees earned exceed impermanent loss?**

This determines if LPing is profitable.

### Break-Even Calculation

**Example**: ETH/USDC pool
- Your capital: $10,000
- Daily volume: $100,000
- Fee rate: 0.3%
- Your share: 1% of pool

**Daily fees**: $100,000 × 0.003 × 0.01 = **$3/day**
**Annual fees**: $3 × 365 = **$1,095/year**

**IL scenarios**:
- If ETH moves ±25%: IL = 2% = $200
- If ETH moves ±50%: IL = 5.7% = $570
- If ETH moves ±100%: IL = 20% = $2,000

**Analysis**:
- Small moves (±25%): Fees ($1,095) > IL ($200) ✅ Profitable
- Medium moves (±50%): Fees ($1,095) > IL ($570) ✅ Still profitable
- Large moves (±100%): Fees ($1,095) < IL ($2,000) ❌ **Losing money**

**Reality**: In volatile markets, IL often exceeds fees, making LPing unprofitable.


![IL vs Fees Break-Even Analysis](images/lessons/lesson_03/lp03_02_il_vs_fees_break-even_analysis.png)


## 🎯 Risk Factors That Increase IL

### 1. High Volatility

**Volatile pairs** (e.g., meme coins):
- Experience frequent large price swings
- IL accumulates quickly
- Fees rarely compensate

**Stable pairs** (e.g., USDC/USDT):
- Minimal price divergence
- IL is negligible
- Fees can be profitable

### 2. Low Correlation

**Uncorrelated pairs** (e.g., ETH/BTC):
- Prices move independently
- Higher IL risk
- Requires active management

**Correlated pairs** (e.g., wstETH/ETH):
- Prices move together
- Lower IL (ratio stays stable)
- More predictable

### 3. Long Time Horizons

**Long-term positions**:
- More time for prices to diverge
- IL compounds over time
- Requires rebalancing

**Short-term positions**:
- Less time for divergence
- Lower IL risk
- But higher gas costs

## 💡 Strategies to Minimize IL

### 1. Choose Stable Pairs

**Best**: Stablecoin pairs (USDC/USDT, DAI/USDC)
- IL is minimal (<0.1% even with depegs)
- Fees are consistent
- Lower risk overall

**Good**: Correlated pairs (wstETH/ETH, WBTC/ETH)
- Ratio stays relatively stable
- IL is manageable
- Still earn decent fees

**Avoid**: Volatile uncorrelated pairs (unless you're hedging)

### 2. Use Narrow Ranges (V3)

In Uniswap V3, you can concentrate liquidity:
- Narrow range = higher fees per dollar
- But higher IL if price exits range
- Requires active management

**Trade-off**: More fees vs. more IL risk

### 3. Hedge Your Position

**Delta-neutral strategy**:
- Provide liquidity (long both assets)
- Short one asset using perpetuals
- Neutralize price exposure
- Profit from fees only

**Advanced**: Requires understanding derivatives and higher capital

### 4. Active Rebalancing

**Rebalance when**:
- Price moves significantly (±20%+)
- IL exceeds fees earned
- Better opportunities elsewhere

**Cost**: Gas fees for rebalancing (use L2!)

## 🔬 Advanced Deep-Dive: Loss Versus Rebalancing (LVR)

### Beyond Impermanent Loss

**Loss Versus Rebalancing (LVR)** is a more sophisticated metric that measures the cost of providing liquidity against informed traders (arbitrageurs).

### The LVR Concept

LVR quantifies how much value arbitrageurs extract from LPs due to:
- **Stale prices**: AMM prices lag behind market prices
- **Block time delays**: Price updates only happen on-chain
- **Adverse selection**: Arbitrageurs trade when it's profitable for them

### LVR Formula

$$LVR = \frac{1}{2} \times \sigma^2 \times t$$

Where:
- σ = volatility
- t = time

**Key Insight**: LVR is proportional to volatility squared. High volatility = massive LVR.

### LVR vs. IL

| Metric | What It Measures | Reversibility |
|--------|------------------|---------------|
| **IL** | Opportunity cost vs. holding | Reversible if price returns |
| **LVR** | Value extracted by arbitrageurs | **Never reversible** (monotonic) |

**Critical Difference**: LVR is cumulative and never decreases. Every price movement extracts value permanently.

### Real-World Impact

In high-volatility pools:
- LVR can exceed 50% annually
- Fees might be 20% APY
- **Net result: -30% APY** (losing money!)

This is why professional LPs hedge their positions.


![LVR vs IL Comparison](images/lessons/lesson_03/lp03_04_lvr_vs_il_comparison.png)


## 🎓 Beginner's Corner: IL Myths Debunked

**Myth 1**: "IL is only temporary"
- **Reality**: It becomes permanent when you withdraw during divergence

**Myth 2**: "Fees always cover IL"
- **Reality**: In volatile markets, IL often exceeds fees

**Myth 3**: "IL only happens when prices go up"
- **Reality**: IL happens with any price divergence (up or down)

**Myth 4**: "Stablecoin pairs have no IL"
- **Reality**: They have minimal IL, but depegs can cause massive losses

**Myth 5**: "I can avoid IL by choosing the right pair"
- **Reality**: You can minimize IL, but never eliminate it completely

## 📊 Risk Assessment Framework

### Before Providing Liquidity, Ask:

1. **What's the volatility?**
   - High volatility = high IL risk
   - Check historical price movements

2. **What's the correlation?**
   - Correlated pairs = lower IL
   - Uncorrelated = higher IL

3. **What's the fee rate?**
   - Higher fees = more buffer against IL
   - Lower fees = need lower volatility

4. **What's the expected volume?**
   - High volume = more fees
   - Low volume = fees might not cover IL

5. **Can I afford the IL?**
   - Calculate worst-case IL scenarios
   - Ensure you can handle the loss

## 🎯 Key Takeaways

1. **Impermanent Loss is real** and often exceeds fees
2. **IL = opportunity cost** of LPing vs. holding
3. **IL grows exponentially** with price divergence
4. **IL becomes permanent** when you withdraw during divergence
5. **Stable pairs minimize IL** but have lower fees
6. **LVR is cumulative** and never reverses
7. **Always calculate IL** before providing liquidity

## 🚀 Next Steps

Now that you understand the risks, Lesson 4 will show you how to set up your first LP position safely, minimizing IL while maximizing fees.

Complete **Exercise 3** to calculate IL for different scenarios and build your risk assessment skills.

---

**Remember**: IL is the hidden cost that destroys LP profits. Always calculate it before depositing. If IL exceeds expected fees, don't provide liquidity—just hold your tokens.

[← Back to Summary](../SUMMARY.md) | [Next: Exercise 3 →](../exercises/exercise-03-risk-assessment-and-il-analysis.md) | [Previous: Lesson 2 ←](lesson-02-mathematics-of-liquidity-provision.md)

