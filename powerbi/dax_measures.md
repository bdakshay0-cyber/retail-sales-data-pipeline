# Power BI DAX Measures

# ============================================================
# Total Sales
# ============================================================

```DAX
Total Sales =
SUM(factsales[gross_sales])

# ============================================================
# Total Orders
# ============================================================

Total Orders =
DISTINCTCOUNT(factsales[sales_id])

# ============================================================
# Units Sold
# ============================================================

Units Sold =
SUM(factsales[quantity])

# ============================================================
# Total Customers
# ============================================================

Total Customers =
DISTINCTCOUNT(factsales[customer_id])

# ============================================================
# Average Order Value
# ============================================================

Average Order Value =
DIVIDE(
    [Total Sales],
    [Total Orders],
    0
)

# ============================================================
# Average Selling Price
# ============================================================

Average Selling Price =
DIVIDE(
    [Total Sales],
    [Units Sold],
    0
)

# ============================================================
# Average Monthly Sales
# ============================================================

Average Monthly Sales =
AVERAGEX(
    VALUES(dimdate[month]),
    [Total Sales]
)

# ============================================================
# Average Monthly Sales is used instead of YoY Growth because
# the sample fact dataset covers only January–June 2026 and
# there is no prior-year fact data for comparison.
# ============================================================


# ============================================================
# MoM measures
# ============================================================

Sales Previous Month =
CALCULATE(
    [Total Sales],
    DATEADD(
        dimdate[date],
        -1,
        MONTH
    )
)

# ============================================================

Sales MoM % =
DIVIDE(
    [Total Sales] - [Sales Previous Month],
    [Sales Previous Month],
    0
)


# ============================================================
# YTD 
# ============================================================

Sales YTD =
TOTALYTD(
    [Total Sales],
    dimdate[date]
)

# ============================================================
# customer measures
# ============================================================

Sales per Customer =
DIVIDE(
    [Total Sales],
    [Total Customers],
    0
)

# ============================================================
Orders per Customer =
DIVIDE(
    [Total Orders],
    [Total Customers],
    0
)

# ============================================================
# Corrected Product Rank
# ============================================================

Product Sales Rank =
IF(
    ISINSCOPE(dimproduct[product_name]),
    RANKX(
        ALLSELECTED(dimproduct[product_name]),
        [Total Sales],
        ,
        DESC,
        DENSE
    )
)
# ============================================================
# Product Sales Rank is calculated at individual product level.
# Category-level rows intentionally do not display Product Rank.
# ============================================================

# ============================================================
# Month display columns
# ============================================================

Year Month =
FORMAT(
    dimdate[date],
    "YYYY-MM"
)

# ============================================================
YearMonthSort =
dimdate[year] * 100 +
dimdate[month]


# Year Month → Sort by → YearMonthSort
# month_name → Sort by → month


