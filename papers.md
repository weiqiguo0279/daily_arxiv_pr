# 🚗 Autonomous Driving VLM/VLA Papers

- [Heterogeneous Low-Bandwidth Pre-Training of LLMs](https://arxiv.org/abs/2601.02360)
  - Yazan Obeidi, Amir Sarfi, Joel Lidin, Paul Janson, Eugene Belilovsky
  - Publish Date: 2026.01.05
  - Task: Reasoning
  - Summary：
    - Introduces a heterogeneous distributed training framework for LLM pre-training, combining low-communication data parallelism (SparseLoCo) with low-bandwidth pipeline model parallelism via activation compression.
    - Proposes adaptations to make subspace pipeline compression compatible with SparseLoCo, enabling resource-limited participants to jointly instantiate a model replica.
    - Finds that selective heterogeneous compression improves the loss-communication tradeoff, especially at aggressive compression ratios, offering a path to incorporate low-bandwidth model parallelism into LLM pre-training.

- [ExposeAnyone: Personalized Audio-to-Expression Diffusion Models Are Robust Zero-Shot Face Forgery Detectors](https://arxiv.org/abs/2601.02359)
  - Kaede Shiohara, Toshihiko Yamasaki, Vladislav Golyanik
  - Publisher: The University of Tokyo, Max Planck Institute for Informatics
  - Publish Date: 2026.01.05
  - Task: Detection
  - Datasets: [DF-TIMIT](https://github.com/), [DFDCP](https://github.com/), [KoDF](https://github.com/), [IDForge](https://github.com/)
  - Summary：
    - ExposeAnyone, a fully self-supervised face forgery detection method using a personalized audio-to-expression diffusion model.
    - The method computes identity distances via diffusion reconstruction errors to enable person-of-interest detection, outperforming previous state-of-the-art by 4.22 percentage points in average AUC.
    - Demonstrates robustness to unseen manipulations, including Sora2-generated videos, and high resilience to corruptions like blur and compression for real-world applicability.

- [VINO: A Unified Visual Generator with Interleaved OmniModal Context](https://arxiv.org/abs/2601.02358)
  - Junyi Chen, Tong He, Zhoujie Fu, Pengfei Wan, Kun Gai, Weicai Ye
  - Publish Date: 2026.01.05
  - Task: Generation
  - Summary：
    - VINO, a unified visual generator that performs image and video generation and editing within a single framework using a shared diffusion backbone.
    - It couples a vision-language model (VLM) with a Multimodal Diffusion Transformer (MMDiT), encoding multimodal inputs as interleaved conditioning tokens to guide the diffusion process.
    - The model supports multi-reference grounding, long-form instruction following, and identity preservation across static and dynamic content via a multi-stage training pipeline.

- [DARC: Drum accompaniment generation with fine-grained rhythm control](https://arxiv.org/abs/2601.02357)
  - Trey Brosnan
  - Publish Date: 2026.01.05
  - Summary：
    - DARC is a generative drum accompaniment model that conditions on both musical context from other stems and explicit rhythm prompts like beatboxing or tapping tracks.
    - It augments the STAGE drum stem generator with fine-grained rhythm control via parameter-efficient fine-tuning while maintaining musical context awareness.

- [Talk2Move: Reinforcement Learning for Text-Instructed Object-Level Geometric Transformation in Scenes](https://arxiv.org/abs/2601.02356)
  - Jing Tan, Zhaoyang Zhang, Yantao Shen, Jiarui Cai, Shuo Yang, Jiajun Wu, Wei Xia, Zhuowen Tu, Stefano Soatto
  - Publish Date: 2026.01.05
  - Task: Reasoning
  - Summary：
    - Talk2Move, a reinforcement learning (RL) based diffusion framework for text-instructed spatial transformation of objects within scenes, addressing the challenge of object-level geometric transformations like translating, rotating, or resizing.
    - The framework employs Group Relative Policy Optimization (GRPO) to explore geometric actions through diverse rollouts from input images and textual variations, eliminating the need for costly paired data.
    - It introduces object-centric spatial rewards for evaluating displacement, rotation, and scaling, and uses off-policy step evaluation with active step sampling to improve learning efficiency and achieve precise, semantically faithful transformations.

- [VINO: A Unified Visual Generator with Interleaved OmniModal Context](https://arxiv.org/abs/2601.02358)
  - Junyi Chen, Tong He, Zhoujie Fu, Pengfei Wan, Kun Gai, Weicai Ye
  - Publish Date: 2026.01.05
  - Task: Generation
  - Summary：
    - VINO, a unified visual generator that performs image and video generation and editing within a single framework using a shared diffusion backbone.
    - It couples a vision-language model (VLM) with a Multimodal Diffusion Transformer (MMDiT), encoding multimodal inputs as interleaved conditioning tokens to guide the diffusion process.
    - The model supports multi-reference grounding, long-form instruction following, and identity preservation across static and dynamic content via a multi-stage training pipeline.

- [DatBench: Discriminative, Faithful, and Efficient VLM Evaluations](https://arxiv.org/abs/2601.02316)
  - Siddharth Joshi, Haoli Yin, Rishabh Adiga, Ricardo Monti, Aldo Carranza, Alex Fang, Alvin Deng, Amro Abbas, Brett Larsen, Cody Blakeney, Darren Teh, David Schwab, Fan Pan, Haakon Mongstad, Jack Urbanek, Jason Lee, Jason Telanoff, Josh Wills, Kaleigh Mentzer, Luke Merrick, Parth Doshi, Paul Burstein, Pratyush Maini, Scott Loftin, Spandan Das, Tony Jiang, Vineeth Dorna, Zhengping Wang, Bogdan Gaza, Ari Morcos, Matthew Leavitt
  - Publish Date: 2026.01.05
  - Task: VQA
  - Datasets: [DatBench-Full](https://github.com/), [DatBench](https://github.com/)
  - Summary：
    - Proposes DatBench, a cleaned evaluation suite for Vision-Language Models (VLMs) designed to satisfy three desiderata: faithfulness, discriminability, and efficiency.
    - Identifies and mitigates critical failure modes in existing VLM evaluations, such as multiple-choice formats, blindly solvable questions, and mislabeled samples.
    - Curates DatBench-Full (33 datasets) and a discriminative subset, DatBench, achieving up to 50x speedup while closely matching the discriminative power of original datasets.

- [CycleVLA: Proactive Self-Correcting Vision-Language-Action Models via Subtask Backtracking and Minimum Bayes Risk Decoding](https://arxiv.org/abs/2601.02295)
  - Chenyang Ma, Guangyu Yang, Kai Lu, Shitong Xu, Bill Byrne, Niki Trigoni, Andrew Markham
  - Publisher: University of Oxford
  - Publish Date: 2026.01.05
  - Project Page: [CycleVLA](https://dannymcy.github.io/cyclevla/)
  - Task: Planning
  - Summary：
    - Introduces CycleVLA, a system that equips Vision-Language-Action models (VLAs) with proactive self-correction to anticipate and recover from incipient failures before they fully manifest.
    - Integrates a progress-aware VLA, a VLM-based failure predictor and planner for subtask backtracking, and a test-time scaling strategy using Minimum Bayes Risk (MBR) decoding to improve retry success.

- [TopoLoRA-SAM: Topology-Aware Parameter-Efficient Adaptation of Foundation Segmenters for Thin-Structure and Cross-Domain Binary Semantic Segmentation](https://arxiv.org/abs/2601.02273)
  - Salim Khazem
  - Publish Date: 2026.01.05
  - Code: [TopoLoRA-SAM](https://github.com/salimkhazem/Seglab.git)
  - Task: Perception
  - Datasets: [DRIVE](https://drive.grand-challenge.org/), [STARE](http://cecas.clemson.edu/~ahoover/stare/), [CHASE_DB1](https://blogs.kingston.ac.uk/retinal/chasedb1/), [Kvasir-SEG](https://datasets.simula.no/kvasir-seg/), [SL-SSDD](https://github.com/gaofenng/SL-SSDD)
  - Summary：
    - TopoLoRA-SAM, a topology-aware and parameter-efficient adaptation framework for binary semantic segmentation, adapting foundation models like SAM to thin structures and noisy modalities.
    - The method injects Low-Rank Adaptation (LoRA) into a frozen ViT encoder, augmented with a lightweight spatial convolutional adapter and optional topology-aware supervision via differentiable clDice.
    - Evaluated on five benchmarks, it achieves the best overall average Dice while training only 5.2% of parameters, matching or exceeding fully fine-tuned specialist models.

- [The JWST EXCELS survey: Outflows in 1.5 < z < 5 quiescent galaxies are likely relics from episodic AGN activity](https://arxiv.org/abs/2601.02269)
  - Elizabeth Taylor, Adam C. Carnall, David Maltby, Omar Almaini, Ho-Hin Leung, Struan D. Stevenson, Andrea Negri, Fergus Cullen, Vivienne Wild, Ross J. McLure, Alice E. Shapley, Karla Z. Arellano-Córdova, Ryan Begley, Cecilia Bondestam, Thomas de Lisle, Callum T. Donnan, James S. Dunlop, Richard Ellis, Guillaume Hewitt, Anton M. Koekemoer, Feng-Yuan Frey Liu, Derek J. McLeod, Kate Rowlands, Ryan L. Sanders, Dirk Scholte, Maya Skarbinski, Thomas M. Stanton
  - Publish Date: 2026.01.05
  - Summary：
    - Investigates neutral gas outflows and inflows in 13 post-starburst and quiescent galaxies at redshifts 1.8 ≤ z ≤ 4.6 using JWST NIRSpec spectroscopy from the EXCELS survey.
    - Finds outflow velocities from ≈300-1200 km/s, with gas flows detected exclusively in objects that quenched <600 Myr ago, and mass outflow rates orders of magnitude higher than current star formation.
    - Proposes observations are consistent with a model of episodic AGN activity driving fossil outflows, suggesting a potential 'outflow cycle' with short periods of AGN activity recurring every ≈40 Myr on average.

- [Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents](https://arxiv.org/abs/2601.02314)
  - Sourena Khanzadeh
  - Publisher: (Inferred from abstract/title)
  - Publish Date: 2026.01.05
  - Task: Reasoning
  - Summary：
    - Introduces Project Ariadne, a novel XAI framework using Structural Causal Models (SCMs) and counterfactual logic to audit the causal integrity and faithfulness of LLM agent reasoning traces.
    - Defines and detects a failure mode termed Causal Decoupling, revealing a persistent Faithfulness Gap where reasoning traces can function as "Reasoning Theater" while decisions are governed by latent parametric priors.
    - Proposes the Ariadne Score as a new benchmark for aligning stated logic with model action, based on measuring Causal Sensitivity via hard interventions on intermediate reasoning nodes.

- [The Polarization and Magnetic Field of the Radio Arc as Observed by ALMA at 100 GHz](https://arxiv.org/abs/2601.02297)
  - Nora Salem, Dylan M. Paré, Paulo Cortes, Mark R. Morris, Valentin J. M. Le Gouellec
  - Publisher: ALMA
  - Publish Date: 2026.01.05
  - Task: Perception
  - Datasets: [ALMA](https://www.almaobservatory.org/)
  - Summary：
    - Presents the first ALMA 100 GHz polarimetric observations of the Radio Arc non-thermal filaments (NTFs) in the Galactic Center, which are not impacted by significant Faraday effects.
    - Finds a uniformly rotated magnetic field with respect to the NTF filament orientation, constant along each filament, but with systematically different orientations across different filaments.
    - Uses the observed magnetic field pattern to update the understanding of line-of-sight structures, suggesting the polarization may result from multiple magnetic field systems or central concentration within the filaments.

- [CycleVLA: Proactive Self-Correcting Vision-Language-Action Models via Subtask Backtracking and Minimum Bayes Risk Decoding](https://arxiv.org/abs/2601.02295)
  - Chenyang Ma, Guangyu Yang, Kai Lu, Shitong Xu, Bill Byrne, Niki Trigoni, Andrew Markham
  - Publisher: University of Oxford
  - Publish Date: 2026.01.05
  - Project Page: [CycleVLA](https://dannymcy.github.io/cyclevla/)
  - Task: Planning
  - Summary：
    - Introduces CycleVLA, a system for proactive self-correction in Vision-Language-Action models (VLAs) that anticipates and recovers from failures before they fully manifest.
    - Integrates a progress-aware VLA, a VLM-based failure predictor/planner for subtask backtracking, and a test-time scaling strategy using Minimum Bayes Risk (MBR) decoding to improve retry success.

- [Quintom Dark Energy: Future Attractor and Phantom Crossing in Light of DESI DR2 Observation](https://arxiv.org/abs/2601.02284)
  - Phusuda Thanankullaphong, Prasanta Sahoo, Prajwal Hassan Puttasiddappa, Nandan Roy
  - Publish Date: 2026.01.05
  - Summary：
    - Studies a two-field dark energy model with a quintessence and a phantom scalar field, identifying stable late-time attractors for phantom-dominated accelerated expansion.
    - Confronts the model with cosmological datasets (Pantheon+, CMB, DESI DR2, DES Y5) via Bayesian analysis, finding observational constraints favor a dynamical dark energy sector.
    - The model's effective dark energy equation of state undergoes a gradual, asymptotic phantom divide crossing, connecting phase-space stability to observational viability.

- [A Comparative Study of Custom CNNs, Pre-trained Models, and Transfer Learning Across Multiple Visual Datasets](https://arxiv.org/abs/2601.02246)
  - Annoor Sharara Akhand
  - Publish Date: 2026.01.05
  - Task: Perception
  - Datasets: [Road-surface defect](https://github.com/), [Agricultural variety](https://github.com/), [Fruit/leaf disease](https://github.com/), [Pedestrian walkway encroachment](https://github.com/), [Unauthorized vehicle](https://github.com/)
  - Summary：
    - Presents a controlled comparison of three CNN paradigms: training custom CNNs from scratch, using pre-trained CNNs as fixed feature extractors, and transfer learning via fine-tuning.
    - Evaluates models across five real-world image classification datasets using accuracy, F1-score, and efficiency metrics like training time and parameter counts.
    - Finds that transfer learning yields the strongest predictive performance, while custom CNNs offer an attractive efficiency-accuracy trade-off under constrained budgets.

- [Heterogeneous Low-Bandwidth Pre-Training of LLMs](https://arxiv.org/abs/2601.02360)
  - Yazan Obeidi, Amir Sarfi, Joel Lidin, Paul Janson, Eugene Belilovsky
  - Publish Date: 2026.01.05
  - Task: Reasoning
  - Summary：
    - Introduces a heterogeneous distributed training framework for LLM pre-training, combining low-communication data parallelism (SparseLoCo) with low-bandwidth pipeline model parallelism via activation compression.
    - Proposes adaptations to make subspace pipeline compression compatible with SparseLoCo, enabling efficient training across participants with varying bandwidth resources.
    - Demonstrates through experiments that selective heterogeneous compression improves the loss-communication tradeoff, especially at aggressive compression ratios, offering a path to incorporate low-bandwidth model parallelism into LLM pre-training.

- [ExposeAnyone: Personalized Audio-to-Expression Diffusion Models Are Robust Zero-Shot Face Forgery Detectors](https://arxiv.org/abs/2601.02359)
  - Kaede Shiohara, Toshihiko Yamasaki, Vladislav Golyanik
  - Publisher: The University of Tokyo, Max Planck Institute for Informatics
  - Publish Date: 2026.01.05
  - Task: Detection
  - Datasets: [DF-TIMIT](https://github.com/ipazc/mtcnn), [DFDCP](https://ai.googleblog.com/2019/09/contributing-data-to-deepfake-detection.html), [KoDF](https://github.com/danmohaha/KoDF), [IDForge](https://github.com/IDForge)
  - Summary：
    - ExposeAnyone, a fully self-supervised face forgery detection method using a personalized audio-to-expression diffusion model.
    - The method computes identity distances via diffusion reconstruction errors between suspected videos and personalized subjects for person-of-interest detection.
    - Demonstrates strong performance on unseen manipulations and Sora2-generated videos, with robustness to corruptions like blur and compression.

- [VINO: A Unified Visual Generator with Interleaved OmniModal Context](https://arxiv.org/abs/2601.02358)
  - Junyi Chen, Tong He, Zhoujie Fu, Pengfei Wan, Kun Gai, Weicai Ye
  - Publish Date: 2026.01.05
  - Task: Generation
  - Summary：
    - VINO, a unified visual generator that performs image and video generation and editing within a single framework using a shared diffusion backbone.
    - It couples a vision-language model (VLM) with a Multimodal Diffusion Transformer (MMDiT), encoding multimodal inputs as interleaved conditioning tokens to guide the diffusion process.
    - The model supports multi-reference grounding, long-form instruction following, and identity preservation across static and dynamic content via a multi-stage training pipeline.

- [Talk2Move: Reinforcement Learning for Text-Instructed Object-Level Geometric Transformation in Scenes](https://arxiv.org/abs/2601.02356)
  - Jing Tan, Zhaoyang Zhang, Yantao Shen, Jiarui Cai, Shuo Yang, Jiajun Wu, Wei Xia, Zhuowen Tu, Stefano Soatto
  - Publish Date: 2026.01.05
  - Task: Reasoning
  - Summary：
    - Talk2Move, a reinforcement learning (RL) based diffusion framework for text-instructed spatial transformation of objects within scenes, using Group Relative Policy Optimization (GRPO) to explore geometric actions without paired data.
    - The framework employs spatial reward guidance, off-policy step evaluation, and active step sampling to improve learning efficiency and achieve precise, consistent, and semantically faithful object transformations.

- [Meta-Learning Guided Pruning for Few-Shot Plant Pathology on Edge Devices](https://arxiv.org/abs/2601.02353)
  - Shahnawaz Alam, Mohammed Mudassir Uddin, Mohammed Kaif Pasha
  - Publisher: (Inferred from context: Agricultural/Edge Computing Research)
  - Publish Date: 2026.01.05
  - Task: Perception
  - Datasets: [PlantVillage](https://plantvillage.psu.edu/), [PlantDoc](https://github.com/pratikkayal/PlantDoc-Dataset)
  - Summary：
    - Proposes a method combining neural network pruning with few-shot learning to enable plant disease detection on low-cost edge devices like Raspberry Pi.
    - Introduces Disease-Aware Channel Importance Scoring (DACIS) within a Prune-then-Meta-Learn-then-Prune (PMP) pipeline to identify and retain important network parts for disease classification.
    - Achieves a 78% model size reduction while maintaining 92.3% accuracy, enabling real-time inference at 7 FPS on a Raspberry Pi 4 for practical field diagnosis.

- [Heterogeneous Low-Bandwidth Pre-Training of LLMs](https://arxiv.org/abs/2601.02360)
  - Yazan Obeidi, Amir Sarfi, Joel Lidin, Paul Janson, Eugene Belilovsky
  - Publish Date: 2026.01.05
  - Summary：
    - Introduces a heterogeneous distributed training framework for LLM pre-training, combining low-communication data parallelism (SparseLoCo) with low-bandwidth pipeline model parallelism via activation compression.
    - Proposes adaptations to make subspace pipeline compression compatible with SparseLoCo, enabling resource-limited participants to jointly instantiate a model replica.
    - Finds that selective heterogeneous compression improves the loss-communication tradeoff, especially at aggressive compression ratios, offering a path to incorporate low-bandwidth model parallelism into LLM pre-training.

- [Falcon-H1R: Pushing the Reasoning Frontiers with a Hybrid Model for Efficient Test-Time Scaling](https://arxiv.org/abs/2601.02346)
  - Falcon LLM Team, Iheb Chaabane, Puneesh Khanna, Suhail Mohmad, Slim Frikha, Shi Hu, Abdalgader Abubaker, Reda Alami, Mikhail Lubinets, Mohamed El Amine Seddik, Hakim Hacid
  - Publisher: Falcon LLM Team
  - Publish Date: 2026.01.05
  - Task: Reasoning
  - Summary：
    - Falcon-H1R, a 7B-parameter reasoning-optimized model, demonstrates that small language models (SLMs) can achieve competitive reasoning performance, matching or outperforming models 2x to 7x larger across reasoning benchmarks.
    - The model combines a hybrid-parallel architecture for faster inference with targeted training strategies (efficient SFT and RL scaling) and data curation to deliver high token efficiency and accuracy without increasing model size.
    - It leverages the DeepConf approach to achieve state-of-the-art test-time scaling efficiency, making it a practical backbone for scaling reasoning systems requiring extensive chain-of-thought generation and parallel test-time scaling.

- [Robust Persona-Aware Toxicity Detection with Prompt Optimization and Learned Ensembling](https://arxiv.org/abs/2601.02337)
  - Berk Atil, Rebecca J. Passonneau, Ninareh Mehrabi
  - Publish Date: 2026.01.05
  - Task: Detection
  - Summary：
    - A systematic evaluation of persona-aware toxicity detection, showing no single prompting method uniformly dominates across all model-persona pairs.
    - Proposes a lightweight meta-ensemble (an SVM over a 4-bit vector of prompt predictions) that consistently outperforms individual prompting methods and traditional majority-voting techniques.
    - Provides one of the first systematic comparisons of persona-conditioned prompting for toxicity detection and offers a robust method for pluralistic evaluation in subjective NLP tasks.

- [Estimating Text Temperature](https://arxiv.org/abs/2601.02320)
  - Nikolay Mikhaylovskiy
  - Publish Date: 2026.01.05
  - Task: Reasoning
  - Summary：
    - Proposes a procedure to estimate the temperature of any text, including human-written text, with respect to a given autoregressive language model.
    - Evaluates temperature estimation capability across a selection of small-to-medium LLMs and uses the best-performing model (Qwen3 14B) to estimate temperatures of popular corpora.

- [Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents](https://arxiv.org/abs/2601.02314)
  - Sourena Khanzadeh
  - Publisher: (Inferred from context: Research Paper)
  - Publish Date: 2026.01.05
  - Task: Reasoning
  - Summary：
    - Introduces Project Ariadne, a novel XAI framework using Structural Causal Models (SCMs) and counterfactual logic to audit the causal integrity and faithfulness of LLM agent reasoning.
    - Defines and detects a failure mode termed Causal Decoupling, revealing a persistent Faithfulness Gap where reasoning traces can be unfaithful "Reasoning Theater" while decisions are governed by latent parametric priors.
    - Proposes the Ariadne Score as a new benchmark for aligning stated logic with model action, based on measuring Causal Sensitivity via hard interventions on intermediate reasoning nodes.

- [Heterogeneous Low-Bandwidth Pre-Training of LLMs](https://arxiv.org/abs/2601.02360)
  - Yazan Obeidi, Amir Sarfi, Joel Lidin, Paul Janson, Eugene Belilovsky
  - Publish Date: 2026.01.05
  - Summary：
    - Introduces a heterogeneous distributed training framework for LLM pre-training, combining low-communication data parallelism (SparseLoCo) with low-bandwidth pipeline model parallelism via activation compression.
    - Proposes adaptations to make subspace pipeline compression compatible with SparseLoCo, enabling resource-limited participants to jointly instantiate a model replica.
    - Finds that selective heterogeneous compression improves the loss-communication tradeoff, especially at aggressive compression ratios, offering a path to incorporate low-bandwidth model parallelism into LLM pre-training.

- [ExposeAnyone: Personalized Audio-to-Expression Diffusion Models Are Robust Zero-Shot Face Forgery Detectors](https://arxiv.org/abs/2601.02359)
  - Kaede Shiohara, Toshihiko Yamasaki, Vladislav Golyanik
  - Publish Date: 2026.01.05
  - Task: Detection
  - Datasets: [DF-TIMIT](https://arxiv.org/abs/2601.02359), [DFDCP](https://arxiv.org/abs/2601.02359), [KoDF](https://arxiv.org/abs/2601.02359), [IDForge](https://arxiv.org/abs/2601.02359)
  - Summary：
    - ExposeAnyone, a fully self-supervised face forgery detection method using a personalized audio-to-expression diffusion model.
    - The method computes identity distances via diffusion reconstruction errors to enable person-of-interest forgery detection, outperforming previous state-of-the-art by 4.22 percentage points in average AUC.
    - Demonstrates robustness to unseen manipulations, including Sora2-generated videos, and to real-world corruptions like blur and compression.

- [VINO: A Unified Visual Generator with Interleaved OmniModal Context](https://arxiv.org/abs/2601.02358)
  - Junyi Chen, Tong He, Zhoujie Fu, Pengfei Wan, Kun Gai, Weicai Ye
  - Publish Date: 2026.01.05
  - Task: Generation
  - Summary：
    - VINO is a unified visual generator that performs image and video generation and editing within a single framework using a shared diffusion backbone.
    - It couples a vision-language model (VLM) with a Multimodal Diffusion Transformer (MMDiT), encoding multimodal inputs as interleaved tokens to guide the diffusion process.
    - The model supports multi-reference grounding, long-form instruction following, and identity preservation across static and dynamic content via a multi-stage training pipeline.

- [DARC: Drum accompaniment generation with fine-grained rhythm control](https://arxiv.org/abs/2601.02357)
  - Trey Brosnan
  - Publish Date: 2026.01.05
  - Summary：
    - DARC is a generative drum accompaniment model that conditions on musical context from other stems and explicit rhythm prompts like beatboxing or tapping tracks.
    - It augments the STAGE drum stem generator with fine-grained rhythm control via parameter-efficient fine-tuning while maintaining musical context awareness.

- [Talk2Move: Reinforcement Learning for Text-Instructed Object-Level Geometric Transformation in Scenes](https://arxiv.org/abs/2601.02356)
  - Jing Tan, Zhaoyang Zhang, Yantao Shen, Jiarui Cai, Shuo Yang, Jiajun Wu, Wei Xia, Zhuowen Tu, Stefano Soatto
  - Publish Date: 2026.01.05
  - Task: Reasoning
  - Summary：
    - Talk2Move, a reinforcement learning (RL) based diffusion framework for text-instructed spatial transformation of objects within scenes, addressing the challenge of object-level geometric transformations like translating, rotating, or resizing.
    - Employs Group Relative Policy Optimization (GRPO) to explore geometric actions through diverse rollouts from input images and textual variations, eliminating the need for costly paired data.
    - Introduces object-centric spatial rewards for evaluating displacement, rotation, and scaling, enabling interpretable and coherent transformations that outperform existing text-guided editing approaches in spatial accuracy and scene coherence.


---

*Last updated: 2026-01-07 00:36:29 UTC*
*Auto-generated by ArxivVLMCrawler*