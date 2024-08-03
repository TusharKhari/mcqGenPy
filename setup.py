# for installing local packages in my virtual environment 


from setuptools import find_packages,setup

setup(
    name="mcqgenerator", 
    version="0.0.1", 
    author="khari",
    author_email="tusharkhari57@gmail.com", 
    install_requires=["openai", "langchain", "streamlit","python-dotenv","PyPDF2", "langchain-community", "langchain-core"],
    packages=find_packages()
)