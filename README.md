# En Lih's Ascendion Technical Assessment

## How to access the repository
Run the following code to clone the repository to your local directory, ensure that you have ```Git``` installed on your system
```bash
git clone https://github.com/enlihhhhh/enlih-ascendion-assessment.git
```

Ensure that you navigate to the folder by running the following code
```bash
cd enlih-ascendion-assessment
```

## Repository Structure 
```
enlih-ascendion-assessment/
│
├── main.py 
├── web_scraping.ipynb
├── cityu_tech300_startups.csv   
├── requirements.txt
├── README.md                
``` 

### Files Information
1. ```main.py:``` Python Code to run the entire scraping logic
2. ```web_scraping.ipynb:``` Jupyter Notebook containing the experiments to get to the final scraper (Run this only if you wish to see outputs individually)
3. ```cityu_tech300_startups.csv:```: Contains the final scraped data in a CSV file
4. ```requirements.txt```: Contains all the dependancies required to run the code

## **Local Environment Setup Instructions**

### **Prerequisites**
Ensure you have the following installed on your system:
- Python 3.10 or higher
- Conda or Miniconda for virtual environment management

### **Instructions to install Miniconda with Python on your system**

### For Linux (Preferred)
```bash
# Download Miniconda Installer For Linux (Ubuntu/Debian, Fedora, Arch)
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# Run the installer
bash ~/Miniconda3-latest-Linux-x86_64.sh

# Close and reopen your terminal, then run the following code to activate Miniconda
source ~/.bashrc

# Verify Installation of Miniconda
conda --version
```

For Windows and macOS installation, kindly refer to the following [Official Anconda Website](https://www.anaconda.com/docs/getting-started/miniconda/install#macos-linux-installation) for more information on the installation

---


### **1. Create a Virtual Environment**
Use Conda or Miniconda to create and activate a virtual environment (downgrade or upgrade Python Version when necessary):

### **Using Conda (Preferred)**
```bash
# Creating virtual environment
conda create --name ascendion_env python=3.11

# Activating environment
conda activate ascendion_env

# Deactivate environment
conda deactivate ascendion_env
```

### **Using Python's venv**
```bash
# Creating virtual environment
python -m venv ascendion_env

"""
Steps on Virtual Environment management
""" 
ascendion_env\Scripts\activate # Activate env on Windows
source ascendion_env/bin/activate # Activate env on macOS / Linux

# Deactivate environment
deactivate
```
---

### **2. Install Required Libraries**
Install all required libraries using the provided requirements.txt file
```bash
pip install -r requirements.txt
```

## Running of Code

Ensure that you are currently on the folder directory and run the following code to run the python script

```bash
python3 main.py
```

After the script finishes running, the output will be saved in the same directory as the script, under the filename ```cityu_tech300_startups.csv```.

### Sample Output

| Company Name     | CityU URL                                        | Company Website           | Email   |
|------------------|--------------------------------------------------|----------------------------|------------------------|
| 5th Immersiv | https://www.cityu.edu.hk/hktech300/start-ups/seed-fund-teams/5th-immersiv | https://brideunionhk.com  | martin@bride-union.com |

The scraping process may take up to an hour depending on your internet speed and system performance.

Note: If you wish to analyse the invidual outputs by cells, refer to the ```web_scraping.ipynb``` Jupyter Notebook for more instructions