# Chapter Summary: Business Metrics

## Revenue, cost of goods sold, and margin

**Revenue** is the amount of money that customers paid to the company.

**The cost of goods sold** is the money that the company paid for the purchase of the product. 

Knowing the revenue and the cost of goods sold, you can calculate the first business indicator — **gross profit**. Gross profit is the first indicator of business health. It's pretty easy to calculate it. 

![Chapter%20Summary%20Business%20Metrics%20425aef8786984fd381fecab877561e76/resschet_metrik.jpg](Chapter%20Summary%20Business%20Metrics%20425aef8786984fd381fecab877561e76/resschet_metrik.jpg)

The ratio of gross profit to revenue is called **gross** **margin.**

![Chapter%20Summary%20Business%20Metrics%20425aef8786984fd381fecab877561e76/resschet_metrik%201.jpg](Chapter%20Summary%20Business%20Metrics%20425aef8786984fd381fecab877561e76/resschet_metrik%201.jpg)

## Operating expenses and operating profit

**Operating expenses** are all expenses related to the company's business operations. 

If we subtract the operating expenses from the gross profit, we'll get the **operating profit.**

![Chapter%20Summary%20Business%20Metrics%20425aef8786984fd381fecab877561e76/resschet_metrik%202.jpg](Chapter%20Summary%20Business%20Metrics%20425aef8786984fd381fecab877561e76/resschet_metrik%202.jpg)

Operating profit helps you to know how much a company earns from its business operations. With very few exceptions, operating profit correlates with net profit: the larger the operating profit, the greater the net profit. Moreover, the operating profit is faster and easier to calculate. 

If the operating profit is negative, it is called an **operating loss**. It shows that business owners can't get money out of their business yet. But like a negative gross profit, an operating loss doesn't necessarily mean that everything is lost. Often the company is **planned loss-making** because it invests all profits in rapid growth.

If you divide the operating profit by the revenue, you get the **operating profit margin**. This is the share of the revenue that remains in the company after deducting the cost of goods sold, salaries, rent, marketing, and other expenses related to the main activities. Investors are often interested in operating margins because it allows you to compare different businesses.

![Chapter%20Summary%20Business%20Metrics%20425aef8786984fd381fecab877561e76/resschet_metrik%203.jpg](Chapter%20Summary%20Business%20Metrics%20425aef8786984fd381fecab877561e76/resschet_metrik%203.jpg)

## Net profit

The cost of goods sold, operating expenses, and obligations to the state and creditors are taken into account by the **net profit** indicator. This is the amount that business owners can take for themselves or reinvest in the development of the company.

![Chapter%20Summary%20Business%20Metrics%20425aef8786984fd381fecab877561e76/resschet_metrik%204.jpg](Chapter%20Summary%20Business%20Metrics%20425aef8786984fd381fecab877561e76/resschet_metrik%204.jpg)

Net profit can only be calculated at the end of the year when all tax and loan liabilities have been determined. Therefore, gross and operating profits are used for the daily management of the company, and the net profit is calculated for the annual shareholders meeting.

A negative net profit is called a **net loss**. It shows that the company failed to make money.

## Return on investment

Investors want to know when their investment will pay off. For them, the main metric is **ROI (Return on Investment)**.

![Chapter%20Summary%20Business%20Metrics%20425aef8786984fd381fecab877561e76/roi.jpg](Chapter%20Summary%20Business%20Metrics%20425aef8786984fd381fecab877561e76/roi.jpg)

## Conversion

The sales process can be described as follows: visitor → sale → buyer.

It all starts with the fact that the company is contacted by a user. Then, there is a sale. The more effective the business is at doing this, the better things are for the company. Therefore, one of the most important metrics is conversion. It shows the percentage of users who completed a targeted action.

## Funnels

**Funnels** are a way to display:

1. the path that the user takes to buy a product;
2. the proportion of people who reach the next stage, that is, those who "don’t drop off".

To build a funnel, you need to measure how many people got to each stage. 

A graph that presents the number of people at each stage resembles a funnel for liquids:

![Chapter%20Summary%20Business%20Metrics%20425aef8786984fd381fecab877561e76/voronka.jpg](Chapter%20Summary%20Business%20Metrics%20425aef8786984fd381fecab877561e76/voronka.jpg)

Knowing the number at each stage, you can calculate the percentage of people who reached a certain step, as well as the percentage of those who took each subsequent step:

![Chapter%20Summary%20Business%20Metrics%20425aef8786984fd381fecab877561e76/konversiya.jpg](Chapter%20Summary%20Business%20Metrics%20425aef8786984fd381fecab877561e76/konversiya.jpg)

Funnel analysis allows you to formulate hypotheses, test them, and track changes.

## Online and offline metrics

To answer this question, we will do **metric decomposition:** break metrics into components. 

The main metric for us is revenue. To calculate it, we need to multiply the number of users per day, their conversion, and the average receipt, which is the sum of goods both originally added by the user and those recommended by the model.

![Chapter%20Summary%20Business%20Metrics%20425aef8786984fd381fecab877561e76/viruchka.jpg](Chapter%20Summary%20Business%20Metrics%20425aef8786984fd381fecab877561e76/viruchka.jpg)

The target evaluation metric is the average price of the products that are added based on recommendations. It is the **online metric** calculated in a working system with real users. You can't calculate it according to historic data for another model. 

To build new models, you will also need **offline metrics**. They are calculated according to historical data. You’re already familiar with two offline metrics — the *accuracy* and *MSE* learning metrics. 

The cost of goods added based on the recommendation is affected by:

1. How many products from the list of recommendations are interesting for the user? This is measured by *precision* metrics.
2. Does the model add all products interesting to the user to the list? It's measured by the *recall* metric.

Remember that the *F1 score* combines the *precision* and *recall* metrics.