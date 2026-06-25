AI-Driven Analog IC Design: Automated Dataset Generation & Machine Learning for Op-Amps
This repository showcases an end-to-end framework that bridges analog integrated circuit (IC) design with machine learning. It automates the generation of simulation datasets using ngspice and trains XGBoost regression models to act as fast, highly accurate neural surrogates for predicting the performance metrics of a parameterized two-stage CMOS Operational Amplifier (op-amp).

By replacing slow SPICE simulations with ML models, this approach enables instantaneous performance evaluation (inference in microseconds), paving the way for rapid design space exploration and automated optimization algorithms.

📌 Project Overview
Analog IC sizing is traditionally a manual, iterative, and time-consuming process. Designers rely on SPICE simulations to evaluate circuit performance, which can take seconds to minutes per iteration.

This project demonstrates an AI-assisted design flow:

Automated Simulation Pipeline: A Python script generates randomized design parameter sets (transistor widths, compensation resistor/capacitor values).
Parallel SPICE Execution: Netlists are dynamically built from templates, executed in parallel using ngspice, and the raw text outputs are parsed to extract key performance metrics: DC Gain, Unity Gain Frequency (UGF), and Phase Margin (PM).
Data Quality Filtering: Invalid designs (e.g., those that fail to converge or have too low gain) are discarded.
Machine Learning Surrogate Models: XGBoost regressors are trained on the clean dataset to predict electrical metrics directly from physical sizing parameters with high accuracy (
R
2
>
0.95
R 
2
 >0.95).
⚙️ System Architecture & Workflow
Mermaid diagram
📂 Repository Structure

├── Ai_model/
│   ├── ml_models/
│   │   ├── train_model.py       # Trains XGBoost regressors on simulation data
│   │   ├── evaluate_model.py    # Evaluates trained models & plots R² scatter plots
│   │   └── predict.py           # Runs real-time inference on custom parameters
│   ├── saved_models/            # Serialized XGBoost models (.pkl)
│   └── plots/                   # Saved evaluation plots
├── templates/
│   ├── 180nm_bsim3.txt          # TSMC 180nm BSIM3 transistor model card
│   ├── opamp.sp                 # Parameterized Two-Stage Op-Amp netlist subcircuit
│   └── tb_openloop.sp           # SPICE testbench template for AC/DC measurements
├── dataset_clean.csv            # Clean simulation dataset (features & targets)
├── parameter_sampler.py         # Sizing parameter generator (random search)
├── netlist_builder.py           # Dynamically injects parameters into SPICE templates
├── spice_runner.py              # Subprocess wrapper for ngspice execution
├── extract_metrics.py           # Extracts Gain, UGF, and PM from SPICE logs
├── result_parser.py             # Basic validation and filtering logic
├── dataset_writer.py            # Appends valid simulation results to CSV
├── parallel_runner.py           # Manages multiprocessing Pool for high-speed simulation
├── generate_dataset.py          # Main entrypoint for dataset generation
├── requirements.txt             # Python dependencies
└── .gitignore                   # Git exclusion rules
🚀 Setup & Installation
1. Prerequisites
Python 3.8+
ngspice: The simulator must be installed and added to your system PATH.
Windows: Download from SourceForge and add the bin directory to your environment variables.
macOS: Install via Homebrew: brew install ngspice
Linux: Install via APT: sudo apt-get install ngspice
2. Install Dependencies
Clone this repository and install the required Python packages:

bash

pip install -r requirements.txt
💻 Usage Guide
Step 1: Generate the Dataset
Run the parallel simulation pipeline to sample sizing parameters, execute SPICE simulations, and build dataset.csv:

bash

python generate_dataset.py
Note: You can configure the number of samples and worker threads inside generate_dataset.py.

Step 2: Train the ML Models
Train the XGBoost regressor models for Gain, UGF, and Phase Margin:

bash

python Ai_model/ml_models/train_model.py
This script saves the trained models as .pkl files in Ai_model/saved_models/.

Step 3: Evaluate Model Performance
Verify the accuracy of the trained surrogate models on the test set:

bash

python Ai_model/ml_models/evaluate_model.py
This outputs the 
R
2
R 
2
  scores, Mean Absolute Error (MAE), and generates correlation plots.

Step 4: Run Real-time Inference
Predict the performance of a custom op-amp sizing instantly without running SPICE:

bash

python Ai_model/ml_models/predict.py
📈 Machine Learning Results
The surrogate models achieve high accuracy on a 20% validation split, allowing them to act as reliable surrogates for SPICE simulations.

Metric	Target Performance	XGBoost 
R
2
R 
2
  Score	Mean Absolute Error (MAE)
DC Gain	
20
−
70
 dB
20−70 dB	~ 0.98	~ 0.8 dB
Unity Gain Frequency (UGF)	
10
−
300
 MHz
10−300 MHz	~ 0.96	~ 6.5 MHz
Phase Margin (PM)	
30
∘
−
110
∘
30 
∘
 −110 
∘
 	~ 0.97	~ 1.8°
Evaluation Plot (True vs. Predicted): The evaluation script generates scatter plots showing strong correlation, indicating that the XGBoost models capture the complex, non-linear relationships of the BSIM3 transistor equations.

🔮 Future Enhancements
Multi-Objective Optimization: Integrate genetic algorithms (NSGA-II) or Bayesian Optimization using these trained ML surrogates to find optimal sizes for specific constraints (e.g., target gain 
>
60
 dB
>60 dB, power 
<
1
 mW
<1 mW).
Deep Learning Surrogates: Implement Artificial Neural Networks (ANNs) using PyTorch for comparisons.
Topology Classification: Expand to support multiple op-amp topologies (e.g., Folded Cascode, Telescopic) and classify suitability based on target specs.
Layout-Aware ML: Incorporate parasitic extraction estimates (from layout) into the training loop for post-layout performance prediction.
