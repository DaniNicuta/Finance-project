# Finance Project Using Yahoo Finance

This project is a web application for financial analysis and investing, built using the Yahoo Finance API and FastAPI.

The Yahoo Finance API provides real-time stock quotes, historical data, financial news,
and other financial information for publicly-traded companies around the world. Using FastAPI, 
we have developed a user-friendly web application that allows users to search for companies,
view financial data in charts and graphs, and analyze trends in the market.

Some features of this application include:

Real-time stock quotes and historical data for publicly-traded companies
Personalized watchlist and alerts to keep users informed about the performance of their favorite companies
Technical indicators, financial ratios, and other metrics for financial analysis
Stock screening, portfolio analysis, and backtesting to evaluate the performance of investments
To run this application, you will need to set up a virtual environment with the necessary dependencies and API keys.
See the documentation for more information on how to set up and run the application.

We hope this application will provide users with a comprehensive platform for financial analysis and investing,
leveraging the power of the Yahoo Finance API and the speed and efficiency of FastAPI to deliver a seamless user 
experience.
For Windows, steps to deploy:
```
git clone <git_repo_url>
cd itschool3-finance-project
python3 - m env\
.\env\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```
For Linux, steps to deploy:
```
git clone <git_repo_url>
cd finance-project
python3 -m venv env/
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

This project uses FastAPI & uvicorn.

FastAPI docs: https://fastapi.tiangolo.com/

