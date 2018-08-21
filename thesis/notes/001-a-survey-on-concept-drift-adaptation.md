# A Survey on Concept Drift Adaptation

## Adaptive Learning Algorithms

- **Adaptive Learning Algorithms** are algorithms that updates the model (the concept, the predictions) along with new data.
  Responding to possible concept drift.

- **Supervised Learning Algorithms** are trained with some existing - labeled - data.

  - **Prediction Types**:

    - **Categorical**: Class labels;
    - **Regression**: Coninuous value;

  - **Learning Modes**:

    - **Offline**: All training data should be avaiable. Model is trained before can be used;

    - **Online**: The model is elaborated and updated when new **training data** arrives;
    - **Incremental Learning**: Update the model after each _example_ or _batch of examples_.

      - **_Incremental Learning With Partial Memory_**: When the incremental learning model uses some previous (random or not) history;

    - **Streaming Algorithms**: Analyze high-speed continuous flow of data. Have time and memory constraints.

- **Concept Drift**:

  - **Real Concept Drift**: Happens when the relation between data and target prediction changes. _The data distribution dosent necessarily needs to change_. **_Makes the model obsolete_**;

  - **Virtual Concept Drift**: A drift that _does not_ change the prediction target. But change change the classes boundaries.

  > The paper focus on **Real Concept Drift** only.

- **The ways Concept Drift happen**:

  - Sudden;
  - Incremental;
  - Gradual;
  - Reoccurring concepts;
  - _Outlier_ (not a concept drift).

- **What predictive models need in Changing Environments**:

  - Detect concept drift as soon as possible;
  - Differentiate concept drift from noise;
  - Operate before new data arrives and use limited amount of memory;

- **Online Adaptive Learning Algorithm Flow**:

1.  **Predict**: Receive an example `X` and predict an `y` for it;

2.  **Diagnose**: After some time, receive the correct `y` for `X`.
    Calculate the **_loss estimation_** with it;

3.  **Update**: If the **_loss estimation_** indicates, update the model using the correct label.

- **Some ares of application that deal with Concept Drift**:

  - **Monitoring and Control**: Mass flow prediction in industrial boiler;

  - **Management and Strategic Planning**: Smart Grids and Wind or Solar power plant production prediction;

  - **Personal Assistance and Information**: Spam classification, media monitoring, etc;

  - **Ubiquitous Environment Applications**: Autonomous vehicles.

## Taxonomy of methods for concept drift adaptation

- **Adaptive Learning Algorithms**: are usually composed of four principal modules:

  - **Memory**:

    - **Types of Memory**:

      - **Long-Term Memory** - Generalization of data models;

      - **Short-Term Memory** - Data;

        - **Data Management**: Adaptive models consider the most recent data as the most informative;

          - **Single Example**

          - **Multiple Examples**: A set of recent examples. May use a sliding window (of fixed or variable size);

        - **Forgetting Mechanisms**: Approach to discard old data;

          - **Abrupt Forgetting**: Also called _partial memory_, operate on training windows based on FIFO and limited size data (_sequence based_) or _landkmark based_ variable size based (using timestamps);

          - **Gradual Forgetting**: Nothing is discarded. Recent have more weight, older less;

  - **Change Detection**: The module responsible for change detection. Characterizes and quantify concept drift throught change points.

    - **Sequential Analysis**: _SPRT_, _CUSUM_,_Page-Hinkley_ and _Shiryae’s Bayesian_;

    - **Statistical Process Control (Control Charts)**: _EWMA_;

    - **Monitoring Distributions on Two Different Time Windows**: _ADWIN_;

    - **Contextual Approaches**: _Splice_;

  - **Learning**:

    - **Learning Mode**: When new labeled data arrives, it´s time to update the model. Two ways:

      - **Retraining**: Discards previous model. Merge the new data with the older data, then builds another model;

      - **Incremental**: For each example, makes a minor update to the model statistics;

        - **Online**: Updates the model with the most recent example, if its misclassified;

          - **Streaming Algorithms**: Algorithms to process high-speed continuous flows of data. The algorithm has few passes and has memory use restriction.

    - **Adaptation Methods**:

      - **Blind**: Always update the model with most recent data, even if no concept drift has happened. _Slower response to abrupt concept drifts_;

      - **Informed**: React to a trigger;

        - **Global Replacement**: Delete old model, reconstruct a whole new model;

        - **Local Replacement**: If a *granular model* is being used (Decision Tree), only some parts of the model are replaced;

        - **Model Management**: 

            - **Ensemble**: Ensembles mantain some models and predict using all of them, in weighted fashion;
            
            - **Reoccurring Concept Management**: Some techniques keep older models in a sleeping mode, instead of discarding.
            So, when a concept reoccurrs, it just needs to rescue the sleeping model; 

  - **Loss Estimation**: Quantifies misclassification based on environment feedback;

      - **Model Dependent**: SVM provides statistics "for free". These are used to adapt the model;

      - **Model Independent**: Propose the use of two sliding windows, one with more data, and one with less. The smaller window will react faster to changes, signaling a concept drift when the smaller window error estimator is bigger than the larger window;


      > **Supervised Adaptive Learning** algorithms rely on feedback from the environment to update their models. But, not always the feedback is promptly avaiable or easy to get. Sometimes may be costly, unreliable, biased, ....


## Evaluation

**We need two things to make evaluations**: metrics chosen acoording to the model goal and methodology, to calculate those in the streaming 

Página 25...