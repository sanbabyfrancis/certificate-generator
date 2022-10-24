# certificate-generator

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- ABOUT THE PROJECT -->
## Introduction

- Many bulk certificate generators use jpeg or other image formats to create certificates which often results in poor quality of the certificates.
- This project aims to produce certificates that are lossless and are of high quality by using PDF format.
- `certificate-generator.py` is a simple python script that can produce multiple certificates from a given template (in PDF).
- The name of the participants are provided by the user in the form of a spreadsheet.
- The font style, size and position of the text to be printed on the certificate is also provided by the user.


<!-- GETTING STARTED -->
## Getting Started

The following instructions would help you run the python script on your local machine.

### Prerequisites

- **Python 3.2 or higher**

Python modules to be installed:
- PyPDF2
- pandas
- reportlab

### Installation

- Install the required python modules: `pip3 install PyPDF2 pandas reportlab`
- Clone this repository: `git clone https://github.com/sanbabyfrancis/certificate-generator.git`

<!-- USAGE EXAMPLES -->
## Usage

- Move into the directory containing the python script: `cd certificate-generator`
- Copy the template of the certificate (in .pdf format) into the directory.
- Copy the spreadsheet that contains the name of the participants into the directory.
- Copy a font file (in .ttf format) into the directory. The name will be printed using this font.
- Run the python script: `python3 certificate-generator.py`
- Provide the necessary inputs to the program. Pixel dimension specifies the position where the name has to be printed on the certificate.
- The certificates will be generated inside the `certificates` directory.

<!-- SCREENSHOTS -->
## Screenshots

<img width="920" alt="sanbabyfrancis@Lenovo___certificate generator" src="https://user-images.githubusercontent.com/73488722/158309806-4b866ad7-1d6e-4770-aeb0-3632889b182d.png">

template.pdf | example.pdf
--- | ---
![template](https://user-images.githubusercontent.com/73488722/158216104-5a3a1650-82a4-466b-8620-d561865413d9.png) | ![DONELL BASSETT](https://user-images.githubusercontent.com/73488722/158215512-1baa208e-003c-4395-a004-61a3cee865c1.png)


<!-- CONTACT -->
## Contact

[![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/sanbabyfrancis.svg?style=social&label=Follow%20%40sanbabyfrancis)](https://twitter.com/sanbabyfrancis)

**San Baby Francis** <br>
san.baby.francis123@gmail.com


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Add text to existing pdf using python](https://stackoverflow.com/questions/1180115/add-text-to-existing-pdf-using-python)
* [mursalfk/Certificate-Generator](https://github.com/mursalfk/Certificate-Generator)
* [bhargav-joshi/Bulk-Certificates-Generator](https://github.com/bhargav-joshi/Bulk-Certificates-Generator)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/sanbabyfrancis/certificate-generator.svg?style=for-the-badge
[contributors-url]: https://github.com/sanbabyfrancis/certificate-generator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/sanbabyfrancis/certificate-generator.svg?style=for-the-badge
[forks-url]: https://github.com/sanbabyfrancis/certificate-generator/network/members
[stars-shield]: https://img.shields.io/github/stars/sanbabyfrancis/certificate-generator.svg?style=for-the-badge
[stars-url]: https://github.com/sanbabyfrancis/certificate-generator/stargazers
[issues-shield]: https://img.shields.io/github/issues/sanbabyfrancis/certificate-generator.svg?style=for-the-badge
[issues-url]: https://github.com/sanbabyfrancis/certificate-generator/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/sanbabyfrancis
