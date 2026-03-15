## Dissertation

This page contains the code used in the article "AI Diagnostic Assistance Reduces Interobserver Variability in MRI Grading of Chondromalacia Patellae: A Randomized Controlled Trial with a Simulated System". It consists of two parts:

1. The code used for the **form**
2. The code used for **data processing**, generating images, and their statistical analysis

---

## Form Code (in the folder named "formular")

**Files:**

* **app.py:** The backend component.
* **data.db:** The database where participants' responses are saved.
* **static:** The folder containing the images.
* **templates:** The folder containing the code for the web pages seen by the user.
* **environment.yml:** A file containing the modules required for the form to function. It is used to recreate the environment in which the form was developed.

---

## Data Processing Code (in the folder named "procesare")

**Files:**

* **procesare.ipynb:** Cleans the data received from the form.
* **data.csv:** The output of the `procesare.ipynb` file and the input for the `stat.Rmd` file (the database).
* **stat.Rmd:** This is where the statistical analysis of the data is performed.

This folder can be used to recreate the study.

---
