import os
from setuptools import find_packages, setup

setup(
    name="chatllama",
    version="0.0.0",
    description="RAG chatbot project using Llama 2",
    author="H.S.",
    url="https://github.com/0reoreore0/rag_llama_chatbot_cpu.git",
    python_requires=">=3.8",
    install_requires=[
        "loguru==0.7.2",
        "langchain==0.1.9",
        "llama-cpp-python==0.2.53",
        "chromadb==0.4.24",
        "langchainhub==0.1.14",
        "sentence-transformers==2.5.0",
        "pypdf==4.0.2",
        "fastapi==0.110.0",
        "uvicorn==0.27.1",
        "gradio==4.20.0"
    ],
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
)
