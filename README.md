# YAM-Yet_Another_Menu
A web application that recommends lunch menus based on user information and location
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



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
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h1 align="center">YAM-Yet_Another_Menu</h1>

  <p align="center">
    A web application that recommends lunch menus based on user information and location
    <br />
    <a href="http://ec2-13-124-251-22.ap-northeast-2.compute.amazonaws.com/">View Demo</a>
    ·
    <a href="https://github.com/ehgmsdk20/YAM-Yet_Another_Menu/issues">Report Bug</a>
    ·
    <a href="https://github.com/ehgmsdk20/YAM-Yet_Another_Menu/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Screen Shot][product-screenshot]](http://ec2-13-124-251-22.ap-northeast-2.compute.amazonaws.com/)

You've probably thought about what to eat for your lunch menu. In this case you can get help from yam.  
I think this project is useful for the following reasons

Here's why:
* Most portal sites such as Naver do not categorize restaurants by menu.
* In the case of Baedal Minjok, the menu is classified by menu, but it is limited to restaurants that can deliver.

A list of commonly used resources that I used in this project are listed in the acknowledgements.

### Built With

* [Django](https://docs.djangoproject.com)
* [PostgreSQL](https://www.postgresql.org)



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites(in Ubuntu)

* Python3  
  - Follow instructions at [this site](https://somjang.tistory.com/entry/PythonUbuntu%EC%97%90-Python-37-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0)
* PostgreSQL  
  - You can see how to install and set PostgreSQL in [this readme file](https://github.com/ehgmsdk20/Django_tutorial_with_PostgreSQL#readme)
* Nginx
  ```
  sudo apt-get install nginx
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/ehgmsdk20/YAM-Yet_Another_Menu.git
   ```
2. Install python packages in virtual environment
   ```sh
   cd path_to_repo/yam
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Get Kakaomap api key at [https://developers.kakao.com](https://developers.kakao.com)  
   and replace 'your_appkey' to this key in yam/kakaomap/templates/kakaomap/searchaddr.html
5. Run Server in Django
   ```sh
   cd yam
   python3 manage.py runserver
   ```


<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.
1. Main page  
   ![Main](https://github.com/ehgmsdk20/images/blob/main/yam_main.png)
   ***
2. Profile
   ![Profile](https://github.com/ehgmsdk20/images/blob/main/yam_profile.png)
   ***
3. Edit Profile
   ![EditProfile](https://github.com/ehgmsdk20/images/blob/main/yam_editprofile.png)
   ***
4. Set up search
   ![Setting](https://github.com/ehgmsdk20/images/blob/main/yam_choose.png)
   ***
6. Result
   ![Result](https://github.com/ehgmsdk20/images/blob/main/yam_result.jpg)
   ***



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/ehgmsdk20/YAM-Yet_Another_Menu/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the GPL-3.0 License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Kim Doheun - ehgmsdk@kaist.ac.kr

Project Link: [https://github.com/ehgmsdk20/YAM-Yet_Another_Menu](https://github.com/ehgmsdk20/YAM-Yet_Another_Menu)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Kakaomap API](https://apis.map.kakao.com)
* [Selenium](https://www.selenium.dev/documentation/en)
* [Tor](https://www.torproject.org)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/ehgmsdk20/YAM-Yet_Another_Menu
[contributors-url]: https://github.com/ehgmsdk20/YAM-Yet_Another_Menu/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ehgmsdk20/YAM-Yet_Another_Menu
[forks-url]: https://github.com/ehgmsdk20/YAM-Yet_Another_Menu/network/members
[stars-shield]: https://img.shields.io/github/stars/ehgmsdk20/YAM-Yet_Another_Menu
[stars-url]: https://github.com/ehgmsdk20/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/ehgmsdk20/YAM-Yet_Another_Menu
[issues-url]: https://github.com/ehgmsdk20/YAM-Yet_Another_Menu/issues
[license-shield]: https://img.shields.io/github/license/ehgmsdk20/YAM-Yet_Another_Menu
[license-url]: https://github.com/ehgmsdk20/YAM-Yet_Another_Menu/blob/master/LICENSE.txt
[product-screenshot]: https://github.com/ehgmsdk20/images/blob/main/yam_result.jpg
