![Image Alt Text](https://i.ibb.co/sJVDRvV/wp6767845-indigo-airlines-wallpapers.jpg)

# [Airlines Data Analysis ](https://u43xftqvbcfmptwkp9cayh.streamlit.app/)

## Steps Included 
* Understanding the Business Problem
* Importing Libraries
* Database connection to extract data
* Exploring tables present in the Database to identify key variables
* Analyzing the key variables
* Creating Report with all the results and analysis for the company.

## Skills 
* Python
* SQL

## Dataset
* Download the dataset from [Kaggle](https://www.kaggle.com/datasets/fiazbhk/airline-data-analysis?select=travel.sqlite).

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

| aircraft_code | total_revenue | tickets_count | avg_revenue_per_ticket |
|---------------|---------------|---------------|------------------------|
| 319           | 2706163100    | 52853         | 51201                  |
| 321           | 1638164100    | 107129        | 15291                  |
| 733           | 1426552100    | 86102         | 16568                  |
| 763           | 4371277100    | 124774        | 35033                  |
| 773           | 3431205500    | 144376        | 23765                  |
| CN1           | 96373800      | 14672         | 6568                   |
| CR2           | 1982760500    | 150122        | 13207                  |
| SU9           | 5114484700    | 365698        | 13985                  |

**Figure 4**
</div>

The average occupancy per aircraft is another critical metric to consider. Airlines may measure how successfully they fill their seats and discover opportunities to boost occupancy rates by using this metric. Higher occupancy rates can help airlines increase revenue and profitability while lowering operational expenses associated with vacant seats. Pricing strategy, airline schedules, and customer satisfaction are all factors that might influence occupancy rates. The below Figure 5 shows the average booked seats from the total number of seats for each aircraft. The occupancy rate is calculated by dividing the booked seats by the total number of seats. Higher occupancy rate means the aircraft seats are more booked and only few seats are left unbooked.

<div align="center">

| aircraft_code | booked_seats | num_seats | occupancy_rate |
|---------------|--------------|-----------|----------------|
| 319           | 53.583181    | 116       | 0.461924       |
| 321           | 88.809231    | 170       | 0.522407       |
| 733           | 80.255462    | 130       | 0.617350       |
| 763           | 113.937294   | 222       | 0.513231       |
| 773           | 264.925806   | 402       | 0.659019       |
| CN1           | 6.004431     | 12        | 0.500369       |
| CR2           | 21.482847    | 50        | 0.429657       |
| SU9           | 56.812113    | 97        | 0.585692       |

**Figure 5**
</div>

Airlines can assess how much their total yearly turnover could improve by providing all aircraft with a 10% higher occupancy rate to further examine the possible benefits of raising occupancy rates. This research can assist airlines in determining the financial impact of boosting occupancy rates by 10%, which results in a gradual increase. Therefore, airlines should focus more on pricing strategies.

<div align="center">

| aircraft_code | booked_seats | num_seats | occupancy_rate | Inc_occupancy_rate | Inc_Total_Annual_Turnover |
|---------------|--------------|-----------|----------------|--------------------|---------------------------|
| 319           | 53.58318098720292 | 116   | 0.46192397402761143 | 0.5081163714303726 | 2976779410.0              |
| 321           | 88.80923076923077 | 170   | 0.5224072398190045  | 0.574647963800905  | 1801980510.0              |
| 733           | 80.25546218487395 | 130   | 0.617349709114415   | 0.6790846800258565 | 1569207310.0000002        |
| 763           | 113.93729372937294 | 222  | 0.5132310528350132  | 0.5645541581185146 | 4808404810.0              |
| 773           | 264.9258064516129 | 402   | 0.659019419033863   | 0.7249213609372492 | 3774326050.0              |
| CN1           | 6.004431314623338  | 12    | 0.5003692762186115  | 0.5504062038404727 | 106011180.00000001        |
| CR2           | 21.48284690220174  | 50    | 0.42965693804403476 | 0.4726226318484382 | 2181036550.0              |
| SU9           | 56.81211267605634  | 97    | 0.5856918832583128  | 0.644261071584144  | 5625933169.999999         |

**Figure 6**
</div>

## Conclusion 
In summary, analyzing revenue data such as total revenue per year, average revenue per ticket, and average occupancy per aircraft is crucial for airlines aiming to maximize profitability. By assessing these indicators, airlines can identify areas for improvement and adapt their pricing and route plans accordingly. A higher occupancy rate stands as a crucial factor in enhancing profitability since it enables airlines to optimize revenue while minimizing costs related to empty seats. Additionally, airlines should consider revising the pricing strategy for each aircraft. The disparity between lower and higher prices may deter people from purchasing tickets for those specific aircraft. Establishing a reasonable price aligned with the aircraft's condition and facilities is essential, avoiding extremes of overly cheap or expensive prices.

Moreover, increasing occupancy rates should not compromise consumer satisfaction or safety standards. Airlines must strike a balance between the imperative for profit and the importance of delivering high-quality service while upholding stringent safety regulations. By adopting a data-driven approach to revenue analysis and optimization, airlines can potentially achieve long-term success in a highly competitive industry.


























                                                                                        
