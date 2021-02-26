# Datathon21_T077

Team: Aparna Ayyah, Matt Ho, Bryan Ko

Please attach your youtube link down below:
{link:"https://youtu.be/c2tk3m--SE8"}

Slides (Link to PDF): [link](https://drive.google.com/file/d/1Jt-BZMCok0iO3jMHH0ATmcvP8hNmoTAs/view?usp=sharing)

Slides (PDF): In repository, titled "Datathon_Team77.pdf"


**Problem Set (#1):**

*Synchrony:*
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
- Trained Model(RNN + TimeDistributed Layer)
- Demographics of TIMIT Dataset Analysis (TIMIT_Demographic.py)
- Demographics of CommonVoice Dataset Analysis (TIMIT_Demographic.py)
- DeepSpeech Model Code (DeepSpeech_Training.ipynb)

**Instructions to Build:**
1. Clone repository
2. Downloaded needed datasets (some are very large so we could not include them)
3. Run neccesary pre-processing code to format datasets (data_generator.py)
4. Run model building code (DeepSpeech_Training.ipynb)
5. Check out the results! (Also in Datathon_Team77.pdf)

**Sourced Cited:**
- Koenecke, Allison, et al. “Racial Disparities in Automated Speech Recognition.” 
- Scanlon, Dr. Patricia. “Voice Assistants Don't Work for Kids: The Problem with Speech Recognition in the Classroom.” 
- Masina, Fabio, et al. “Investigating the Accessibility of Voice Assistants With Impaired Users: Mixed Methods Study.” 
- Anusha Prakash, Anju Leela Thomas, S. Umesh and Hema A. Murthy, "Building Multilingual End-to-End Speech Synthesisers for Indian Languages".
- V, Anand P. “Indian Accent Speech Recognition.”
- Raju,Anirudh. “How to Make Neural Language Models Practical for Speech Recognition.”
- L. Lugosch, M. Ravanelli, P. Ignoto, V. Tomar, and Y. Bengio, "Speech Model Pre-training for End-to-End Spoken Language Understanding"




