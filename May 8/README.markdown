# Sales Data Analysis

## Context

I have done it in google colab and downloaded it in both .ipynb and .py format. Both formats I have uploaded here along with the data I have used. Since previous functions need to be used I have used the word count function.

## Main Steps

 1. Import `pandas`, `numpy`, `matplotlib`, `re`, `collections`.
 2. Set file path to `sales_data_sample.csv`.
 3. Load CSV, convert `ORDERDATE`, calculate `TOTAL_SALES`, extract `YEAR`, `MONTH`, drop missing values, print confirmation.
 4. Group by `YEAR`, sum `TOTAL_SALES`, print yearly sales.
 5. Group by `PRODUCTLINE`, sum `TOTAL_SALES`, print product sales.
 6. Group by `CUSTOMERNAME`, get top 5 `TOTAL_SALES`, print results.
 7. Calculate mean, median, std of `TOTAL_SALES` with NumPy, print stats.
 8. Count words in `CUSTOMERNAME` using prior word count logic, print top 5.
 9. Plot yearly sales bar chart, save as `annual_sales.png`, display.
10. Save analysis to `analysis_results.txt`.
