# Electric Guitars Insights from Reverb.com

This repository contains a Jupyter notebook and instrutions for extracting insights from electric guitar postings on Reverb.com. The goal of this project is to analyze the data and gain valuable insights into the electric guitar market.

## Description

The ability to build tools capable of retrieving and parsing information stored across the internet has become increasingly valuable in various fields of data science. This project is inspired by a course focused on web scraping, where we learn how to navigate and parse HTML code, and develop tools to automatically crawl websites.

The main technology used in this project is the Python library called scrapy. However, the techniques learned can be applied to other popular Python libraries as well, including BeautifulSoup and Selenium. 

## Project Objective

The objective of this project is to extract valuable insights from electric guitar postings on Reverb.com. By scraping the website, we can gather data on various aspects of electric guitars, such as brand, model, price, condition, and other relevant attributes. These insights can be used for market analysis, pricing trends, popularity rankings, and other data-driven research.

## Repository Structure

The repository is organized as follows:

- `notebook.ipynb`: This Jupyter notebook demonstrates how to analyze and extract insights from the scraped data. It includes exploratory data analysis (EDA), visualizations, and statistical analysis.
- `check_packages.py`: This standalone Python script allows you to check the installed packages and their versions in your current environment or a specified environment.
- `README.md`: This file you are currently reading provides an overview of the project and instructions on how to use the notebook and the `check_packages.py` script.

## Getting Started

### Running the Jupyter Notebook

To get started with the Jupyter notebook, follow these steps:

1. Clone the repository to your local machine using the following command:

   ```
   git clone https://github.com/your-username/reverb.git
   ```
   #### Checking Installed Packages (Skip to section 2 if creating a new enviroment)

   To check the installed packages and their versions in your current environment or a specified environment, follow these steps:

   1.1. Open your terminal or command prompt and navigate to the directory where the repository is cloned.

   1.2. Run the `check_packages.py` script by executing the following command:

   ```bash
   python check_packages.py
   ```

   The script will prompt you to enter the path for the specified environment. If you leave it empty and press Enter, the check will be performed on the default Python installation directory.



2. Creating a New Environment from requirements.txt

   If you want to create a new environment and install the required packages from the `requirements.txt` file, follow these steps:

   2.1. Create a new Python environment using a tool like conda or virtualenv.

   2.2. Activate the newly created environment.

   2.3. Navigate to the directory where the repository is cloned.

   2.4. Install the required packages by running the following command:

      ```bash
      pip install -r requirements.txt
      ```

      This will install all the necessary packages and their specific versions as listed in the `requirements.txt` file.


3. Open the `notebook.ipynb` file in Jupyter Notebook or Jupyter Lab to explore the code and analysis.


4. Follow the instructions and code within the notebook to perform the data extraction, analysis, and visualization.


## Contributing

If you wish to contribute to this project, follow these steps:

1. Fork the repository on

3. Open the `notebook.ipynb` file in Jupyter Notebook or Jupyter Lab to explore the code and analysis.

4. Follow the instructions and code within the notebook to perform the data extraction, analysis, and visualization.

## Contributing

If you wish to contribute to this project, follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch from the `main` branch to work on your changes.
3. Make your modifications and improvements in your branch.
4. Commit and push your changes to your forked repository.
5. Submit a pull request to the original repository, describing your changes in detail.

Please ensure that your contributions align with the project's goals and follow best practices for code quality and documentation.

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code.
