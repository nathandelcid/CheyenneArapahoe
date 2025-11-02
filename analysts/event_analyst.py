import asyncio 

from fast_agent import FastAgent
from datetime import datetime

current_date = datetime.now().strftime("%Y-%m-%d") 

instruction="""
You are an Event Analyst AI Agent. Your primary goal is to identify the most promising and actively discussed **events** on Reddit that could be relevant for **prediction markets** (e.g., Kalshi, Polymarket, Manifold, etc.).
"""

prompt="""
Search the following subreddits for posts and discussions about upcoming events that have potential for prediction market trading: 
- r/PredictionMarkets
    - Look for high-engagement posts about market-moving events, weekly threads, and trade ideas
    - Keywords: prediction, market, resolution, deadline
- r/sportsbook
    - Monitor lines, injury updates, sharp money, and consensus picks
    - Keywords: odds, line movement, injury, prop
- r/SecurityAnalysis
    - Scan for event-driven threads: earnings, M&A rumors, analyst notes
    - Keywords: earnings, guidance, acquisition, valuation
- r/investing
    - Watch macro and sector news, corporate actions, and earnings reactions
    - Keywords: earnings, Fed, guidance, catalyst
- r/rforcasting
    - Identify forecasting posts, community polls, and prediction methods
    - Keywords: forecast, probability, model
- r/Metaculus
    - Track high-interest questions, community consensus shifts, and comment analysis
    - Keywords: question, probability, consensus
- r/gambling
    - Spot sentiment shifts, tip threads, and large-stake discussions that imply event edges
    - Keywords: bet, value, sharps
- r/DailyFantasy
    - Monitor lineup leaks, injury news, and slate-moving information ahead of contests
    - Keywords: lineup, injury, value
- r/ManifoldMarkets
    - Find trending markets, resolution debates, and community consensus dynamics
    - Keywords: market, resolution, trending
- r/PolymarketTrading
    - Watch popular contracts, liquidity changes, and trader commentary
    - Keywords: contract, price, liquidity
- r/Kalshi
    - Identify event listings tied to economic or policy outcomes and settlement details
    - Keywords: contract, outcome, settlement
- r/CryptoCurrency
    - Monitor protocol upgrades, airdrops, regulation news, and large token movements
    - Keywords: upgrade, fork, airdrop, regulation
- r/LessWrong
    - Source probability reasoning, forecasting techniques, and debate threads
    - Keywords: forecasting, probability, rationality
- r/TheMotte
    - Track political strategy discussions, framing battles, and hot takes that drive attention
    - Keywords: politics, framing, narrative
- r/PoliticalBetting
    - Follow polls, betting odds, and pre-election sentiment shifts
    - Keywords: poll, odds, election
- r/dataisbeautiful
    - Use visualizations to detect emerging trends, spikes, or anomalies in public attention
    - Keywords: visualization, trend, spike
- r/BayesianStatistics
    - Look for methodological threads that suggest improved forecasting approaches
    - Keywords: Bayesian, posterior, prior
- r/MLQuants
    - Find model-driven signals, event-driven strategies, and quant discussion
    - Keywords: model, backtest, alpha
- r/TheoreticalStatistics
    - Monitor advanced statistical insights that could inform event probability estimates
    - Keywords: inference, estimation, hypothesis
        
- Focus on **events within a time range of 1 day to 1 month**, ideally those that **resolve within a week or two** — enabling short-term prediction opportunities.
- Prioritize events that have:
  - High engagement (upvotes, comments, active threads)
  - Clear, binary or measurable outcomes (e.g., elections, policy announcements, market data releases, sports results)
  - Recurring or time-bound nature (weekly economic data, sports matchups, etc.)
- Identify *why* each event is potentially valuable — e.g., strong disagreement in predictions, high volatility, or high public attention.

For each promising event you find, provide:
1. **Event Title / Summary**
2. **Estimated Resolution Date or Timeframe**
3. **Why it’s gaining attention**
4. **Community Source (subreddit link if available)**
5. **Potential Prediction Market Type** (e.g., political, economic, sports, crypto)

Keep your focus on short- to medium-term events (daily–monthly) that can yield clear returns or insights within a week or so.

The current date is {{currentDate}}.
"""

fast = FastAgent(
    name="event-analyst",
)

@fast.agent(
        name="event-analyst",
        instruction=instruction,
        servers=["reddit"])

async def main():
    # use the --model command line switch or agent arguments to change model
    async with fast.run() as agent:
        #await agent.interactive(agent="event-analyst")
        await agent.send(prompt.replace("{{currentDate}}", current_date))

if __name__ == "__main__":
    asyncio.run(main())