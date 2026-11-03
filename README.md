#  Smart Energy Analyser

A Python-based electricity consumption analyser designed to help users monitor household energy usage, estimate monthly electricity costs, and identify opportunities to improve energy efficiency.

## Features
- **Appliance Management:** Add, remove, and search for household appliances.
- **Energy Consumption Calculation:** Calculate individual and total daily energy consumption based on appliance power ratings and operating hours.
- **Monthly Cost Estimation:** Estimate electricity bills using configurable tiered electricity pricing.
- **Budget Monitoring:** Compare estimated monthly electricity costs against a predefined budget and receive warnings when exceeded.
- **Energy Usage Reports:** Generate detailed reports showing each appliance's percentage contribution to total energy consumption.
- **Energy-Saving Recommendations:** Identify the highest energy-consuming appliance and estimate potential savings from reducing its operating time.
- **Multiple Appliance Search:** Search for several appliances simultaneously using Python dictionaries and sets.

## Technologies and Skills
**Programming Language:** Python 3
**Programming Concepts:**
- Functions and modular programming
- Lists, dictionaries, and sets
- Loops and conditional statements
- User input validation
- String manipulation
- Data processing and mathematical calculations

## How It Works
1. Enter the electricity price per kWh.
2. Add appliances by specifying their names, power consumption (W), and daily operating hours.
3. The program calculates daily electricity consumption:

   **Daily Energy (kWh) = Power (W) × Hours / 1000**

4. Monthly consumption is estimated over 30 days.
5. Tiered electricity pricing is applied to calculate the estimated monthly cost.
6. Users can view detailed reports, identify energy-intensive appliances, and explore potential energy savings.

## Electricity Pricing Model

The program uses a configurable two-tier pricing structure:

| Monthly Consumption | Electricity Rate |
|---|---|
| First 300 kWh | Standard rate |
| Above 300 kWh | 1.5 × standard rate |

The default monthly budget is 50 currency units.

*Note: Pricing tiers and budget values are illustrative and can be adjusted in the source code.*

## Project Purpose

This project was developed to strengthen Python programming, data handling, and problem-solving skills while exploring the application of software in energy monitoring, electricity cost estimation, and sustainable energy management.
