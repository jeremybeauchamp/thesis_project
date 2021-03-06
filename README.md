# My Thesis Project

This is the repo for my thesis project. It contains the code, thesis, and papers related to this research. Below is the abstract of my thesis, which gives a general idea of what my research was all about:

> To avoid serious diabetic complications, people with type 1 diabetes must keep their Blood Glucose Levels (BGLs) as close to normal as possible. Insulin dosages and carbohydrate consumption are important considerations in managing BGLs. Since the 1960s, models have been developed to forecast blood glucose levels based on the history of BGLs, insulin dosages, carbohydrate intake, and other physiological and lifestyle factors. Such predictions can be used to alert people of impending unsafe BGLs or to control insulin flow in an artificial pancreas. In past research, an LSTM-based approach to blood glucose level prediction was developed to process "what if" scenarios, in which people could enter foods they might eat or insulin amounts they might take and then see the affect on future BGLs. In this work, the "what-if" scenario is inverted and a similar architecture is introduced, based on chaining two LSTMs that can be trained to make either insulin or carbohydrate recommendations aimed at reaching a desired BG level in the future. Leveraging a recent state-of-the-art model for time series forecasting, a novel deep residual architecture is proposed for the same recommendation task, in which the two LSTM chain is used as a repeating block. Experimental evaluations using real patient data from the OhioT1DM dataset show that the new integrated architecture compares favorably with the previous LSTM-based approach, substantially outperforming the baselines. The promising results suggest that this novel approach could potentially be of practical use to people with type 1 diabetes for self-management of BGLs.

In addition to my thesis, my research produced three published papers:

* *"LSTMs and Deep Residual Networks for Carbohydrate and Bolus Recommendations in Type 1 Diabetes Management"* by Jeremy Beauchamp, Razvan Bunescu, Cindy Marling, Zhongen Li, and Chang Liu. [[link]](https://www.mdpi.com/1424-8220/21/9/3303)

* *"An LSTM-based Approach for Insulin and Carbohydrate Recommendations in Type 1 Diabetes Self-Management"* by Jeremy Beauchamp, Razvan Bunescu, and Cindy Marling. [[link]](http://oucsace.cs.ohio.edu/~smarthlt/pubs/chapter21.pdf)

* *"A General Neural Architecture for Carbohydrate and Bolus Recommendations in Type 1 Diabetes Management"* by Jeremy Beauchamp, Razvan Bunescu, and Cindy Marling. [[link]](http://ceur-ws.org/Vol-2675/paper6.pdf)

The **docs** directory contains the latex source and PDF versions of my thesis and the 3 papers listed above. Additionally it contains a set of PowerPoint slides that I created and used for my thesis defense, and a set of slides I used for a presentation at the KDH 2020 workshop.

The **code** directory contains the Python code required to go from raw data to trained and tested neural network models. There are two subdirectories corresponding to the two deep learning models that were developed for the project. Since the data is collected from human subjects, I did not include it in this repo. If you are interested in getting access to the data, contact Ohio University.
