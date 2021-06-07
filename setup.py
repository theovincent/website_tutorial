from setuptools import setup

setup(
    name="dash_website",
    version="0.1",
    description="Website that shows the results of our paper.",
    packages=["dash_website"],
    requires=["setuptools", "wheel"],
    install_requires=[
        "gunicorn",
        "dash_bootstrap_components",
        "dash_core_components",
        "dash_html_components",
        "dash-gif-component",
        "dash_table",
        "dash",
        "numpy",
        "pandas",
        "plotly",
        "boto3",
        "matplotlib",
        "pyarrow",
    ],
    extras_require={
        "dev": ["tqdm", "openpyxl", "ipykernel", "black", "pyyaml", "nbformat"],
    },
    entry_points={"console_scripts": ["launch_local_website=dash_website.index:launch_local_website"]},
)
