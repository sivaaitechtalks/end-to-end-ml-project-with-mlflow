# with out setup.py
#It tells Python: Here’s my project’s name, where my code lives, and what it needs to run.
# ❌ You can’t install your project with pip install .

# ❌ You can’t import it easily from other folders (import myproject might fail)

# ❌ You can’t share or publish it (e.g., on PyPI or to teammates easily)

# ❌ Tools like pytest, Docker, or CI/CD pipelines might not recognize your project’s structure

# ❌ Dependencies (like numpy, pandas, etc.) won’t auto-install for others 


import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "End-to-end-ML-Project-with-MLflow"
AUTHOR_USER_NAME = "entbappy"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "entbappy73@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)