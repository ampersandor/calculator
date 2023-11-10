## Calculator 1.0.0

<details>
    <summary>Table of content</summary>

- [About](#about)
- [Getting-Started](#getting-started)
    - [Prerequisite](#prerequisite)
    - [Installation](#installation)
- [License](#license)
- [Contact](#contact)
- [Links](#links)    
</details>

## About

A sphinx template tutorial repository
## Getting Started
### Prerequisite
* Python 3.10
* Access to the respotiry (ssh key or Public Access Token)

### Installation

#### Construct Python virtual environment (recommended)
#### Install

When the repository is public
```bash
pip install git+https://github.com/ampersandor/calculator@main#egg=calculator

```

When the repository is private or internal
```bash
export TOKEN="ENTER YOUR GITHUB TOKEN HERE"

pip install git+https://${TOKEN}@github.com/ampersandor/calculator@main#egg=calculator

```

#### How to use
```python
from custom_logger import my_logger, get_logger

@my_logger
def hi(name):
    return f"Hi {name}"

def hello(name):
    logger = get_logger(__file__)  # retrieve the logger object using __file__
    logger.info("this is hello function")
    return f"Hello {name}"

```

## Contact

DongHun Kim - <ddong3525@naver.com>  


