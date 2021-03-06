# Datathon21_T077

Team 77: Aparna Ayyah (Sophomore) & Matt Ho (Sophomore)

Please attach your youtube link down below:
{link:"https://youtu.be/c2tk3m--SE8"}

Slides (Link to PDF): [link](https://drive.google.com/file/d/1Jt-BZMCok0iO3jMHH0ATmcvP8hNmoTAs/view?usp=sharing)

Slides (PDF): In repository, titled "Datathon_Team77.pdf"


**Problem Set (#1): Synchrony**

As virtual assistants become more widely used by consumers to simplify tasks and corporations to increase customer service efficiency, some individuals are getting left behind. Many voice assistants are designed to understand non-accented, dictionary language, which leaves out a significant portion of people. Leveraging publicly available data sets, deliver a model that can create equity in this technology for underserved populations.

**Our Model + Approach:**
- Mirror population composition with training data to improve model performance
- Users should be able to select preferred model (“select dialect”) to improve voice assistant performance
- Use N-gram + Noise Contrastive Estimation to understand long range context 
- Allow User to set “context” in which the command takes place

**Key Components:**
- TIMIT corpus subset (Dataset: Race Column)
- Indic TTS (Dataset)
- CommonVoice (Dataset)
- Confidence Level of DeepSpeech (confidenceLevels.py)
- Trained Model with RNN + TimeDistributed Layer (sample_models.py)
- Demographics of TIMIT Dataset Analysis (TIMIT_Demographic.py)
- Demographics of CommonVoice Dataset Analysis (TIMIT_Demographic.py)
- DeepSpeech Model Code (DeepSpeech_Training.ipynb)
- Sample Models using RNN (sample_models.py)

**Links to Datasets**
- Indic TTS: https://www.iitm.ac.in/donlab/tts/
- CommonVoice: https://commonvoice.mozilla.org/en
- TIMIT: https://catalog.ldc.upenn.edu/LDC93S1

**Instructions to Build:**
1. Clone repository
2. Make sure DeepSpeech is installed **This is very important** (*Starter.ipynb*)
3. Downloaded needed datasets (some are very large so we could not upload them) **This must be done before the rest of the code can be run**
4. Run confidenceLevels.py on DeepSpeech to find confidence levels (*confidenceLevels.py*)
5. Run TIMIT_Demographic.py on demographics_DARPA_TIMIT.csv for demgraphic information (*TIMIT_Demographic.py + demographics_DARPA_TIMIT.csv*)
6. Run CommonVoice_Demographics.py for demographic information (*as seen in presentation*)
7. Run neccesary pre-processing code to format datasets (*data_generator.py*)
8. Run model building code (*DeepSpeech_Training.ipynb + sample_models.py*)
9. Check out the results! (Also in *Datathon_Team77.pdf*)

**Sourced Cited:**
- Koenecke, Allison, et al. “Racial Disparities in Automated Speech Recognition.” 
- Scanlon, Dr. Patricia. “Voice Assistants Don't Work for Kids: The Problem with Speech Recognition in the Classroom.” 
- Masina, Fabio, et al. “Investigating the Accessibility of Voice Assistants With Impaired Users: Mixed Methods Study.” 
- Anusha Prakash, Anju Leela Thomas, S. Umesh and Hema A. Murthy, "Building Multilingual End-to-End Speech Synthesisers for Indian Languages".
- V, Anand P. “Indian Accent Speech Recognition.”
- Raju, Anirudh. “How to Make Neural Language Models Practical for Speech Recognition.”
- L. Lugosch, M. Ravanelli, P. Ignoto, V. Tomar, and Y. Bengio, "Speech Model Pre-training for End-to-End Spoken Language Understanding"

**Indian Accent Model Base:**
- V, Anand P. “Indian Accent Speech Recognition.”

**N-Gram Improvements Base:**
- Raju,Anirudh. “How to Make Neural Language Models Practical for Speech Recognition.”


