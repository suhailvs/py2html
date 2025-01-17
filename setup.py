import setuptools

statuses = [
    "1 - Planning",
    "2 - Pre-Alpha",
    "3 - Alpha",
    "4 - Beta",
    "5 - Production/Stable",
    "6 - Mature",
    "7 - Inactive",
]
py_versions = "3.10 3.11 3.12 3.13".split()

setuptools.setup(
    name="py2html",
    description="Python to HTML, made easy.",
    version="0.1",
    author="Suhail vs",
    author_email="suhailvs@gmail.com",  # SEE NOTE BELOW (*)
    license="BSD",
    classifiers=[
        "Development Status :: " + statuses[1],
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
    ]
    + ["Programming Language :: Python :: " + o for o in py_versions],
    url="https://www.django-rest-framework.org/",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        "fastcore>=1.7.18",
        "python-dateutil",
        "starlette>0.33",
        "oauthlib",
        "itsdangerous",
        "uvicorn[standard]>=0.30",
        "httpx",
        "fastlite>=0.1.1",
        "python-multipart",
        "beautifulsoup4",
    ],
    extras_require={"dev": ["ipython", "lxml", "pysymbol_llm"]},
    python_requires=">=3.8",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
)
