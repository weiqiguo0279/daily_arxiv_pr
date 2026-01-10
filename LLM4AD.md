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
