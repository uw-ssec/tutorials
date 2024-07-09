# Scipy 2024

## Generative AI Copilot for Scientific Software – a RAG-Based Approach

Don Setiawan, Anant Mittal, Anuj Sinha, Ishika Khandelwal, Cordero Core, Madhav
Kashyap, Niki Burggraf, Anshul Tambay, Vani Mandava

### Introduction

Generative AI systems built upon large language models (LLMs) have shown great
promise as tools that enable people to access information through natural
conversation. Scientists can benefit from the breakthroughs these systems enable
to create advanced tools that will help accelerate their research outcomes. This
tutorial will cover: (1) the basics of language models, (2) setting up the
environment for using open source LLMs without the use of expensive compute
resources needed for training or fine-tuning, (3) learning a technique like
Retrieval-Augmented Generation (RAG) to optimize output of LLM, and (4) build a
“production-ready” app to demonstrate how researchers could turn disparate
knowledge bases into special purpose AI-powered tools. The right audience for
our tutorial is scientists and research engineers who want to use LLMs for their
work.

### Tutorial Description

Generative AI is changing the way we adopt and use technology. The power of AI
is manifest in the everyday interactions of consumer tech and tools. This
tutorial aims to utilize the underlying methods in Generative AI to advance
scientific research. This tutorial will introduce and implement RAG (a technique
for enhancing the accuracy and reliability of a generative AI model) for
scientific research. We will go through the fundamentals of RAG and then
implement it over documents retrieved from existing GitHub repositories and
several domain-specific knowledge bases. The language model used in the tutorial
is the Allen Institute for AI (AI2) Open Language Model (OLMo), an LLM with open
data, code, weights, and evaluation benchmarks. OLMo is purpose-built for
scientific discovery as it has been trained on Dolma, an open dataset of 3
trillion tokens collected from diverse web content, academic publications, code,
books, and encyclopedic materials. LangChain is a Python and JavaScript
framework for developing applications powered by LLMs. Using LangChain, we
create a context-aware question answering agent by implementing a RAG chain.
Using a simple example from the astronomy community, we demonstrate how the tool
performs correctly with and incorrectly without RAG-enabled context. At the end
of the tutorial, attendees will create an AI-powered question and answering
application that they can use to advance their research.

Following is an example of the output of a simple use case from the tutorial:

#### Before Implementing RAG

```
<|user|>

What is Astropy?

<|assistant|>

A community-driven effort to build a common platform of astronomical tools and data formats, Astpy (short for "astronomy") is an open-source project that aims to create a unified framework for working with data in astronomy. Built on top of NumPy, SciPy, and other popular scientific libraries, Astropy provides functions, classes, and tools to facilitate and simplify the processing and analysis of astronomical datasets and simulations. This platform offers consistency in data structures, formatting, and interfaces across different packages, making it easier for researchers to work with large-scale observational and theoretical datasets alike. The project serves as a central location for many open-source tools, simplifying access and encouraging collaboration among astronomers and computer scientists.

```

#### After Implementing RAG

```

<|user|>

What is Astropy?

<|assistant|>

Astropy is a community-developed open-source project that provides an integrated package for astronomical data analysis in Python. It includes various functionalities, such as time management, coordinate transformations, and data manipulation. Astropy is designed to be compatible with other popular data science tools like NumPy, SciPy, and IPython.

The context provided describes the `astropy.utils` package, which contains various utility functions and classes that are not astronomy-specific but mainly for use within the Astropy project. This package covers topics such as downloading data from URLs, data structures, compatibility with older versions of Python/Numpy, and version intercompatibility functions.

To summarize, Astropy is an open-source astronomical data analysis toolkit built upon existing packages like NumPy, SciPy, and IPython to provide a cohesive experience for users seeking astronomy-related functionality in Python. The `astropy.utils` package contains various utility functions and classes that are not specific to astronomy but instead cater to the Astropy project's requirements and internal compatibility concerns.

```

### Tutorial Outline (4 hours total)

#### [Module 1: Introduction to LLMs and Problem Setup (1 hour 15 min)](./module1/index.md)

- [Python Environment Setup](./module1/setup.md)
- [Introduction to Language Models](./module1/1-introduction-to-language-models.ipynb)
- [LLMs, Prompt Engineering, and OLMo](./module1/2-llms-and-prompt-engineering-with-olmo.ipynb)
- [LangChain: The LLM Application Framework](./module1/3-langchain.ipynb)

#### [Break 1 (15 minutes)](./break1.md)

#### [Module 2: Building LLM-powered Domain Specific Question and Answer System (1 hour 15 mins)](./module2/index.md)

- [Domain-Specific Question and Answer Examples](./module2/1-domain-specific-question-answering.ipynb)
- [Astrophysics Prompting with OLMo](./module2/2-astrophysics-prompting-with-olmo.ipynb)
- [Retrieval-Augmented Text Generation](./module2/3-retrieval-augmented-text-generation.ipynb)

#### [Break 2 (15 minutes)](./break2.md)

#### [Module 3: Creating the Application (1 hour)](./module3/index.md)

- [Astrophysics Chat Application](./module3/1-olmo-chat-rag.ipynb)
- [Try with your data](./module3/2-try-with-your-data.ipynb)

### Acknowledgements

We would like to thank
[Professor Andy Connolly](https://escience.washington.edu/member/andy-connolly/)
for providing the questions and the domain expertise for the astronomy use case
of this tutorial.

We also thank the [Allen Institute for AI (AI2)](https://allenai.org/) for
providing the Open Language Model (OLMo) and the Dolma dataset, the organizers
of SciPy 2024 for giving us the opportunity to present this tutorial, and
[Quansight](https://quansight.com/) for providing the
[Nebari](https://www.nebari.dev/) platform for this tutorial.

The development of this tutorial, was done by engineers at the
[University of Washington's Scientific Software Engineering Center (SSEC)](https://escience.washington.edu/software-engineering/ssec/)
supported by Schmidt Sciences, LLC. as part of the
[Virtual Institutes for Scientific Software (VISS)](https://www.schmidtsciences.org/viss/).

<div>
  <a href="https://escience.washington.edu/software-engineering/ssec/">
    <img src="https://uw-ssec-tutorials.readthedocs.io/en/latest/_static/logo.png"
    alt="SSEC_logo" width="100">
  </a>
  <a href="https://www.schmidtsciences.org/viss/">
    <img src="https://www.schmidtsciences.org/wp-content/themes/schmidt-sciences/images/logo.png" alt="Schmidt_logo" width="150" style="background-color: #1a1e2d;">
  </a>
  <a href="https://escience.washington.edu/">
    <img src="https://escience.washington.edu/wp-content/uploads/2022/07/escience-logo-768x193.png" alt="eScience_logo" width="150" style="background-color: #ffffff;">
  </a>
  <a href="https://washington.edu/">
    <img src="https://upload.wikimedia.org/wikipedia/commons/1/17/Washington_Huskies_logo.svg" alt="uw_logo" height="100">
  </a>
</div>

### Feedback Survey

Please fill out the [tutorial survey](https://tinyurl.com/ssecfeedback) at the
end to help us improve the tutorial.
