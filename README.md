# Airlines Data Analysis Project

## Business Problem
Our company operates a diverse fleet of aircraft ranging from small business jets to medium-sized machines. We have been providing high-quality air transportation services to our clients for several years, and our primary focus is to ensure a safe, comfortable, and convenient journey for our passengers. However, we are currently facing challenges due to several factors such as stricter environmental regulations, higher flight taxes, increased interest rates, rising fuel prices, and a tight labor market resulting in increased labor costs. As a result, the company's profitability is under pressure, and they are seeking ways to address this issue. To tackle this challenge, they are looking to conduct an analysis of their database to find ways to increase their occupancy rate, which can help boost the average profit earned per seat.

## Main Challenges
1. Stricter environmental regulations: The demand on the airlines industry to reduce its carbon footprint is growing, resulting in more stringent environmental laws that increase operating costs and restrict expansion potential.
2. Higher flight taxes: To address environmental issues and generate revenue, governments worldwide are imposing heavier taxes on aircraft, raising the cost of flying and decreasing demand.
3. Tight labor market resulting in increased labor costs: The shortage of trained personnel in aviation has driven up labor costs and increased turnover rates.

## Objectives
1. Increase Occupancy Rates: By raising occupancy rates, we can enhance the average profit per seat and alleviate the impact of the challenges we're facing.
2. Improve Price Strategy: We need to formulate a pricing strategy that considers the evolving market conditions and customer preferences, aiming to attract and retain customers.
3. Enhance Customer Experience: Our focus should be on delivering a seamless and convenient experience for our customers, spanning from booking to arrival. This approach will differentiate us in a highly competitive industry and foster customer loyalty.

The end goal of this task would be to identify opportunities to increase the occupancy rate on low-performing flights, which can ultimately lead to increased profitability for the airline.

## Basic Analysis
The basic analysis of data provides insights into the number of planes with more than 100 seats, how the number of tickets booked, and the total amount earned changed over time, as well as the average fare for each aircraft with different conditions. These findings will be helpful in developing strategies to optimize occupancy rates and pricing for each aircraft. **Table 1** shows the aircraft with more than 100 seats and the actual count of seats.

<div align="center">

| aircraft_code | num_seats |
|---------------|-----------|
| 319           | 116       |
| 320           | 140       |
| 321           | 170       |
| 733           | 130       |
| 763           | 222       |
| 773           | 402       |

**Table 1**

</div>

In order to gain a deeper understanding of the trend in ticket bookings and revenue earned through those bookings, we utilized a line chart visualization. Upon analysis of the chart, we observe that the number of tickets booked exhibits a gradual increase from June 22nd to July 7th, followed by a relatively stable pattern from July 8th until August, with a noticeable peak in ticket bookings where the highest number of tickets was booked on a single day. It is important to note that the revenue earned by the company from these bookings is closely tied to the number of tickets booked. Therefore, we can see a similar trend in the total revenue earned by the company throughout the analyzed time period. These findings suggest that further exploration of the factors contributing to the peak in ticket bookings may be beneficial for increasing overall revenue and optimizing operational strategies.

<div align="center">

![Image](https://i.ibb.co/whN1cvF/Image-1.png)

**Figure 1**

</div>

<div align="center">

![Image](https://i.ibb.co/Jxy2rJ7/Image-3.png)

**Figure 2**
</div>

We were able to generate a bar graph to graphically compare the data after completing computations for the average cost associated with different fare conditions for each aircraft. Figure 3 displays data for three types of fares: business, economy, and comfort. It's worth mentioning that the comfort class is available on only one aircraft, the 773. Conversely, the CN1 and CR2 planes provide only the economy class. When comparing different pricing circumstances within each aircraft, the charges for the business class are consistently greater than those for the economy class. This trend may be observed across all planes, irrespective of fare conditions.

<div align="center">

![Image](https://i.ibb.co/Km6qnB3/Image-4.png)

**Figure 3**
</div>

## Analyzing Occupancy Rate
Airlines must thoroughly analyze their revenue streams in order to maximize profitability. The overall income per year and average revenue per ticket for each aircraft are important metrics to consider. Airlines may use this information to determine which aircraft types and itineraries generate the most income and alter their operations appropriately. This research can also assist in identifying potential for pricing optimization and allocating resources to more profitable routes. The below Figure 4 shows the total revenue, total tickets, and average revenue made per ticket for each aircraft. The aircraft with the highest total revenue is SU9, and from Figure 3, it can be seen that the price of the business class and economy class is the lowest on this aircraft. This could be the reason that most people bought tickets for this aircraft as it costs less compared to others. The aircraft with the least total revenue is CN1, and the possible reason behind this is that it only offers economy class with a very low price. It might be because of its poor conditions or fewer facilities.

<div align="center">

| aircraft_code | tickets_count | total_revenue | avg_revenue_per_ticket |
|---------------|---------------|---------------|------------------------|
| 319           | 52853         | 2706163100    | 51201                  |
| 321           | 107129        | 1638164100    | 15291                  |
| 733           | 86102         | 1426552100    | 16568                  |
| 763           | 124774        | 4371277100    | 35033                  |
| 773           | 144376        | 3431205500    | 23765                  |
| CN1           | 14672         | 96373800      | 6568                   |
| CR2           | 150122        | 1982760500    | 13207                  |
| SU9           | 365698        | 5114484700    | 13985                  |

**Figure 4**
</div>















                                                                                        
