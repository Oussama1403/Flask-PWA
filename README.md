# Flask-PWA



### Made with:
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![Python](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white) ![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

a flask app that supports progressive web app technology it is supposed to be a template when I start a new Flask project.

## Installation and usage

```bash
git clone https://github.com/Oussama1403/Flask-PWA
cd Flask-PWA
python3 flask_app.py
```
Then head over to http://127.0.0.1:5000/ you should see a page and install button in the browser(if supports).<br>
<b>a web browser will only allow the app to register if the application is served over https,or on localhost(127.0.0.1:5000) for development purposes.</b>


The project directory will contain:
```

├── flask_app.py
├── README.md
├── static
│   ├── 512x512.png
│   ├── app.js
│   ├── css
│   │   └── style.css
│   ├── logo.png
│   └── manifest.json
├── sw.js
└── templates
    ├── base.html
    └── home.html

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
