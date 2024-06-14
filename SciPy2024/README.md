# Scipy 2024

## Generative AI Copilot for Scientific Software – a RAG-Based Approach

Don Setiawan,
Anant Mittal,
Anuj Sinha,
Ishika Khandelwal,
Cordero Core,
Madhav Kashyap,
Niki Burggraf,
Anshul Tambay,
Vani Mandava

### Introduction

Generative AI systems built upon large language models (LLMs) have shown great promise as tools that enable people to access information through natural conversation. Scientists can benefit from the breakthroughs these systems enable to create advanced tools that will help accelerate their research outcomes. This tutorial will cover: (1) the basics of language models, (2) setting up the environment for using open source LLMs without the use of expensive compute resources needed for training or fine-tuning, (3) learning a technique like Retrieval-Augmented Generation (RAG) to optimize output of LLM, and (4) build a “production-ready” app to demonstrate how researchers could turn disparate knowledge bases into special purpose AI-powered tools. The right audience for our tutorial is scientists and research engineers who want to use LLMs for their work.  

### Tutorial Description

Generative AI is changing the way we adopt and use technology. The power of AI is manifest in the everyday interactions of consumer tech and tools. This tutorial aims to utilize the underlying methods in Generative AI to advance scientific research. This tutorial will introduce and implement RAG (a technique for enhancing the accuracy and reliability of a generative AI model) for scientific research. We will go through the fundamentals of RAG and then implement it over documents retrieved from existing GitHub repositories and several domain-specific knowledge bases. The language model used in the tutorial is the Allen Institute for AI (AI2) Open Language Model (OLMo), an LLM with open data, code, weights, and evaluation benchmarks. OLMo is purpose-built for scientific discovery as it has been trained on Dolma, an open dataset of 3 trillion tokens collected from diverse web content, academic publications, code, books, and encyclopedic materials. LangChain is a Python and JavaScript framework for developing applications powered by LLMs. Using LangChain, we create a context-aware question answering agent by implementing a RAG chain. Using a simple example from the astronomy community, we demonstrate how the tool performs correctly with and incorrectly without RAG-enabled context. At the end of the tutorial, attendees will create an AI-powered question and answering application that they can use to advance their research.  

Following is an example of the output of a simple use case from the tutorial:

#### Before Implementing RAG

```
<|user|> 

What is echopype?  

<|assistant|> 

It's a tool for helping people with their typing skills. It can be used by teachers and students alike. 

<|user|> 

How does it work?  

<|assistant|> 

Echopype uses artificial intelligence (AI) to help users improve their typing speed and accuracy. The AI learns from user input data such as mistakes made while typing and then corrects them automatically. This allows users to focus on other aspects of their learning process without having to worry about typos or misspellings in their documents or emails. 

```

#### After Implementing RAG

```

<|user|> 

What is echopype?  

<|assistant|> 

A toolkit for converting data from various manufacturer-specific formats into a standardized [netCDF](https://www.unidata.ucar.edu/software/netcdf/) file.  

<|assistant|> 

How can I use echopype?  

<|assistant|> 

To get started, download and extract the source code. Then run the scripts in the root directory. For more detailed instructions, see the README.md file. 

```

### Tutorial Outline (4 hours total)

#### [Module 1: Introduction to LLMs and Problem Setup (1 hour 15 min)](./module1/index.md)
- [Python Environment Setup](./module1/setup.md)
- [Introduction to Language Models](./module1/introduction-to-language-models.ipynb)
- [LLMs, Prompt Engineering, and OLMo](./module1/llms-and-prompt-engineering-with-olmo.ipynb)
- [LangChain: The LLM Application Framework](./module1/langchain.ipynb)

#### [Break 1 (15 minutes)](./break1.md)

#### [Module 2: Building LLM-powered Domain Specific Question and Answer System (1 hour 15 mins)](./module2/index.md)
- [Domain-Specific Question and Answer Examples](./module2/domain-specific-question-answering.ipynb)
- [Astrophysics Prompting with OLMo](./module2/astrophysics-prompting-with-olmo.ipynb)
- [Retrieval-Augmented Text Generation](./module2/retrieval-augmented-text-generation.ipynb)

#### [Break 2 (15 minutes)](./break2.md)

#### [Module 3: Creating the Application (1 hour)](./module3/index.md)
- [Astrophysics Chat Application](./module3/olmo-chat-rag.ipynb)

### Acknowledgements

We would like to thank [Professor Andy Connolly](https://escience.washington.edu/member/andy-connolly/) for providing the questions and the domain expertise for the astronomy use case of this tutorial.

We also thank the Allen Institute for AI (AI2) for providing the Open Language Model (OLMo) and the Dolma dataset, and the organizers of SciPy 2024 for giving us the opportunity to present this tutorial.

The development of this tutorial, was done by engineers at the University of Washington's Scientific Software Engineering Center (SSEC) supported by Schmidt Sciences, LLC. as part of the Virtual Institutes for Scientific Software (VISS).

<div>
  <a href="https://escience.washington.edu/software-engineering/ssec/">
    <img src="https://uw-ssec-tutorials.readthedocs.io/en/latest/_static/logo.png" alt="SSEC_logo" width="100">
  </a>
  <a href="https://www.schmidtsciences.org/viss/">
    <img src="https://www.schmidtsciences.org/wp-content/themes/schmidt-sciences/images/logo.png" alt="Schmidt_logo" width="150" style="background-color: #1a1e2d;">
  </a>
  <a href="https://escience.washington.edu/">
    <img src="https://escience.washington.edu/wp-content/uploads/2022/07/escience-logo-768x193.png" alt="eScience_logo" width="150" style="background-color: #ffffff;">
  </a>
  <a href="https://washington.edu/">
    <img src="https://upload.wikimedia.org/wikipedia/commons/1/17/Washington_Huskies_logo.svg" alt="eScience_logo" height="100">
  </a>
</div>
