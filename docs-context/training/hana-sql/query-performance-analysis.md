Classification: training-derived-concepts
Source basis: openSAP_hanasql1_Week_3_All_Slides.pdf
Trust usage: conceptual performance-analysis framing
Do not use for: exact local performance metrics or plan claims
Topics covered: query plan analysis, operator cost, runtime reasoning

# Query Performance Analysis

- Performance analysis should focus on how data is processed through the SQL plan.
- Useful reasoning dimensions include:
  - join selectivity
  - cardinality growth
  - grouping cost
  - sorting cost
  - row reduction before expensive operators
- This should improve AMDP performance explanations and review comments.
