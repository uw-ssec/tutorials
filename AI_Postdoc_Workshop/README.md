# AI in Science Postdoc Workshop

## Generative AI / RAG Copilot for Scientific Software

Don Setiawan, Anant Mittal, Anuj Sinha, Ishika Khandelwal, Cordero Core, Madhav
Kashyap, Niki Burggraf, Anshul Tambay, Vani Mandava, Apoorva Sheera, Madeline Gordon

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
Using a simple example from computer science community, we demonstrate how the tool
performs correctly with and incorrectly without RAG-enabled context. At the end
of the tutorial, attendees will create an AI-powered question and answering
application that they can use to advance their research.

Following is an example of the output of a simple use case from the tutorial:

### Tutorial Outline (1 hour 40 minutes total)

#### [Module 1: Introduction to LLMs and Problem Setup (45 minutes)](./module1/index.md)

- [Python Environment Setup](./module1/setup.md)
- [LLMs: Prompt Engineering, and OLMo](./module1/1-llms-prompt-engineering-with-olmo.ipynb)
- [LangChain: The LLM Application Framework](./module1/2-langchain.ipynb)
- [Domain-Specific Question and Answer Examples](./module1/3-domain-specific-question-answering.ipynb)
- [Algorithms Prompting with OLMo](./module1/4-algorithms-prompting-with-olmo.ipynb)

#### [Break 1 (5 minutes)](./break1.md)

#### [Module 2: Building LLM-powered Domain Specific Question and Answer System (50 minutes)](./module2/index.md)

- [Retrieval-Augmented Text Generation](./module2/1-retrieval-augmented-text-generation.ipynb)
- [Algorithms Chat Application](./module2/2-olmo-chat-rag.ipynb)

### Acknowledgements

We would like to thank
[Professor Andy Connolly](https://escience.washington.edu/member/andy-connolly/)
for providing the questions and the domain expertise for the astronomy use case
of this tutorial.

We also thank the [Allen Institute for AI (AI2)](https://allenai.org/) for
providing the Open Language Model (OLMo) and the Dolma dataset.

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
