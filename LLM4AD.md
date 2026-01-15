# 📚 每日 arXiv 论文总结(LLM4AD/VLM4AD/VLA4AD)

**日期**: 2026-01-15
**论文数量**: 2 篇
**LLM**: DeepSeek (deepseek-chat)

---


- [SoC: Semantic Orthogonal Calibration for Test-Time Prompt Tuning](https://arxiv.org/abs/2601.08617)
  - Leo Fillioux, Omprakash Chakraborty, Ismail Ben Ayed, Paul-Henry Cournède, Stergios Christodoulidis, Maria Vakalopoulou, Jose Dolz
  - Publish Date: 2026.01.13
  - Task: Perception
  - Summary：
    - Proposes Semantic Orthogonal Calibration (SoC), a Huber-based regularizer for test-time prompt tuning of vision-language models to improve uncertainty calibration.
    - Theoretically and empirically shows that prior full orthogonality constraints degrade calibration by pushing semantically related classes apart, making models overconfident.
    - Demonstrates that SoC enforces smooth prototype separation while preserving semantic proximity, leading to improved calibration and competitive discriminative performance.

---


- [Semantic Misalignment in Vision-Language Models under Perceptual Degradation](https://arxiv.org/abs/2601.08355)
  - Guo Cheng
  - Publish Date: 2026.01.13
  - Task: Perception
  - Datasets: [Cityscapes](https://www.cityscapes-dataset.com/)
  - Summary：
    - A systematic study of semantic misalignment in Vision-Language Models (VLMs) under controlled degradation of upstream visual perception, using semantic segmentation as a representative module.
    - Introduces perception-realistic corruptions and proposes language-level misalignment metrics to quantify hallucination, critical omission, and safety misinterpretation.
    - Reveals a disconnect between pixel-level robustness and multimodal semantic reliability, highlighting a critical limitation for safety-critical applications like autonomous driving.

---

# 📚 每日 arXiv 论文总结(LLM4AD/VLM4AD/VLA4AD)

**日期**: 2026-01-11
**论文数量**: 4 篇
**LLM**: DeepSeek (deepseek-chat)

---


- [ThinkDrive: Chain-of-Thought Guided Progressive Reinforcement Learning Fine-Tuning for Autonomous Driving](https://arxiv.org/abs/2601.04714)
  - Chang Zhao, Zheming Yang, Yunqing Hu, Qi Guo, Zijian Wang, Pengcheng Li, Wen Ji
  - Publish Date: 2026.01.08
  - Task: Planning
  - Summary：
    - ThinkDrive, a Chain-of-Thought (CoT) guided progressive reinforcement learning fine-tuning framework for autonomous driving that synergizes explicit reasoning with difficulty-aware adaptive policy optimization.
    - Employs a two-stage training strategy: first performing supervised fine-tuning (SFT) using CoT explanations, then applying progressive RL with a difficulty-aware adaptive policy optimizer that dynamically adjusts learning intensity based on sample complexity.
    - Outperforms strong RL baselines on evaluation metrics and shows a 2B-parameter model trained with this method can surpass the performance of the much larger GPT-4o.

---


- [UniDrive-WM: Unified Understanding, Planning and Generation World Model For Autonomous Driving](https://arxiv.org/abs/2601.04453)
  - Zhexiao Xiong, Xin Ye, Burhan Yaman, Sheng Cheng, Yiren Lu, Jingru Luo, Nathan Jacobs, Liu Ren
  - Publish Date: 2026.01.07
  - Project Page: [UniDrive-WM](https://unidrive-wm.github.io/UniDrive-WM)
  - Task: Planning
  - Datasets: [Bench2Drive](https://bench2drive.github.io/)
  - Summary：
    - UniDrive-WM, a unified VLM-based world model that jointly performs driving-scene understanding, trajectory planning, and trajectory-conditioned future image generation within a single architecture.
    - The model's trajectory planner predicts a future trajectory, which conditions a VLM-based image generator to produce plausible future frames, providing supervisory signals that enhance understanding and iteratively refine trajectory generation.
    - Experiments on Bench2Drive show improvements of 5.9% in L2 trajectory error and 9.2% in collision rate over previous methods, demonstrating the advantages of integrating VLM-driven reasoning, planning, and generative world modeling.

---


- [A Vision-Language-Action Model with Visual Prompt for OFF-Road Autonomous Driving](https://arxiv.org/abs/2601.03519)
  - Liangdong Zhang, Yiming Nie, Haoyang Li, Fanjie Kong, Baobao Zhang, Shunxin Huang, Kai Fu, Chen Min, Liang Xiao
  - Publish Date: 2026.01.07
  - Task: Planning
  - Datasets: [RELLIS-3D](https://github.com/unmannedlab/RELLIS-3D)
  - Summary：
    - Proposes OFF-EMMA, an end-to-end multimodal framework for off-road autonomous driving, addressing insufficient spatial perception and unstable reasoning in VLA models.
    - Introduces a visual prompt block using semantic segmentation masks to enhance spatial understanding and a chain-of-thought with self-consistency reasoning strategy to improve planning robustness.

---


- [FROST-Drive: Scalable and Efficient End-to-End Driving with a Frozen Vision Encoder](https://arxiv.org/abs/2601.03460)
  - Zeyu Dong, Yimin Zhu, Yu Wu, Yu Sun
  - Publish Date: 2026.01.06
  - Task: End-to-End
  - Datasets: [Waymo Open E2E Dataset](https://waymo.com/open/)
  - Summary：
    - FROST-Drive, a novel End-to-End (E2E) architecture for autonomous driving that preserves the generalization of a pretrained Vision-Language Model (VLM) by keeping its vision encoder frozen.
    - The model combines the frozen encoder with a transformer-based adapter and a GRU-based decoder for waypoint generation, and introduces a custom loss to optimize for Rater Feedback Score (RFS).
    - Experiments on the Waymo Open E2E Dataset show the frozen-encoder approach outperforms full fine-tuning, offering a new pathway for robust, generalizable driving models.

---

# 📚 每日 arXiv 论文总结(LLM4AD/VLM4AD/VLA4AD)

**日期**: 2026-01-10
**论文数量**: 2 篇
**LLM**: DeepSeek (deepseek-chat)

---


- [ThinkDrive: Chain-of-Thought Guided Progressive Reinforcement Learning Fine-Tuning for Autonomous Driving](https://arxiv.org/abs/2601.04714)
  - Chang Zhao, Zheming Yang, Yunqing Hu, Qi Guo, Zijian Wang, Pengcheng Li, Wen Ji
  - Publish Date: 2026.01.08
  - Task: Planning
  - Summary：
    - ThinkDrive, a Chain-of-Thought (CoT) guided progressive reinforcement learning fine-tuning framework for autonomous driving that synergizes explicit reasoning with difficulty-aware adaptive policy optimization.
    - The method employs a two-stage training strategy, starting with supervised fine-tuning using CoT explanations, followed by progressive RL with a difficulty-aware adaptive policy optimizer that dynamically adjusts learning intensity.

---


- [UniDrive-WM: Unified Understanding, Planning and Generation World Model For Autonomous Driving](https://arxiv.org/abs/2601.04453)
  - Zhexiao Xiong, Xin Ye, Burhan Yaman, Sheng Cheng, Yiren Lu, Jingru Luo, Nathan Jacobs, Liu Ren
  - Publish Date: 2026.01.07
  - Project Page: [UniDrive-WM](https://unidrive-wm.github.io/UniDrive-WM)
  - Task: Planning
  - Datasets: [Bench2Drive](https://bench2drive.github.io/)
  - Summary：
    - UniDrive-WM, a unified VLM-based world model that jointly performs driving-scene understanding, trajectory planning, and trajectory-conditioned future image generation within a single architecture.
    - The model's trajectory planner predicts a future trajectory to condition a VLM-based image generator, providing supervisory signals that enhance scene understanding and iteratively refine trajectory generation.
    - Experiments on Bench2Drive show improvements of 5.9% in L2 trajectory error and 9.2% in collision rate over previous methods, demonstrating advantages of integrating reasoning, planning, and generative modeling.

---
