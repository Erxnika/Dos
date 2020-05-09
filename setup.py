from distutils.core import setup

setup(
    name="Slowloris",
    py_modules=["slowloris"],
    entry_points={"console_scripts": ["slowloris=slowloris:main"]},
    version="0.2.1",
    description="Low bandwidth DoS tool. Slowloris rewrite in Python.",
    author="Hyxr",
    author_email="webdosusb@gmail.com",
    url="",
    keywords=["dos", "http", "Hyxr Dos Attack"],
    license="MIT",
)
