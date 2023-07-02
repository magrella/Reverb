import pkg_resources


def check_installed_packages(path=None):
    # List of required packages
    required_packages = [
        'beautifulsoup4',
        'pandas',
        'scrapy',
        'matplotlib',
        'numpy'
    ]

    # Check installed packages and their versions
    installed_packages = pkg_resources.working_set

    if path:
        pkg_resources.working_set.add_entry(path)

    for package in required_packages:
        try:
            dist = installed_packages.by_key[package]
            print(f"{dist.key} ({dist.version}) is installed.")
        except KeyError:
            print(f"{package} is not installed.")

if __name__ == "__main__":
    path = input("Enter the path for the specified environment (leave empty for default): ")
    check_installed_packages(path)
