<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>jingfelix</title>
</head>

<body>
    <style>
        * {
            padding: 0%;
            margin: 0%;
            text-decoration: none;
            color: black;
            font-size: 15px;
            font-family: 'Times New Roman', Times, serif;
            background-color: #ffffe5;
        }

        body {
            max-width: 1080px;
            min-height: 70vh;
            margin: 0 auto;
            padding-top: 3rem;
            display: flex;
            flex-direction: column-reverse;
        }

        div.block {
            /*max-width: 80%;*/
            padding-left: 1.5rem;
            padding-right: 1.5rem;
            display: flex;
            flex-direction: column;
            flex-wrap: wrap;
            justify-content: center;
            flex-grow: 1;
        }

        #intro {
            padding-top: 1rem;
        }

        #slogan {
            padding-top: 1rem;
            padding-bottom: 1rem;
            font-size: 5rem;
            font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
            font-weight: 200;
            border-bottom: solid 2px rgb(124, 124, 124);
        }

        p {
            font-size: 1.4rem;
            margin-top: 1rem;
            margin-bottom: 1.2rem;
            line-height: 2rem;
        }

        p.bold {
            font-size: 1.5rem;
            font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
            font-weight: bold;
        }

        a {
            font-size: inherit;
            font-style: italic;
        }

        @media screen and (min-width: 650px) {
            body {
                flex-direction: row;
                align-items: center;
            }

            #slogan {
                width: 90%;
                font-size: 5rem;
                padding-left: 2rem;
                border-left: solid 2px rgb(124, 124, 124);
                border-bottom: none;
            }


            div.bottom {
                width: 100%;
                position: fixed;
                bottom: 1rem;
                left: 0%;
                text-align: center;
                background-color: rgba(0, 0, 0, 0);
                margin-top: 2rem;
            }
        }

        div.bottom {
            width: 100%;
            position: fixed;
            top: 1rem;
            left: 0%;
            text-align: center;
            background-color: rgba(0, 0, 0, 0);
            margin-top: 1rem;
        }
    </style>
    <div class="block two">
        <div id="intro">
            <p class="bold">
                Hello there. My name is Tianyi Jing.
            </p>
            <p class="bold">
                I am an undergraduate in Huazhong University of Science and Technology, major in Cyber Security and
                Engneering.
            </p>
            <p>
                I am interested in how technology made changes in our life, and happy to try new tech-products.
            </p>
            <p>
                I love to make tools that bright my life: including <a href="https://jingfelix.github.io">my blog</a>,
                <a href="https://github.com/jingfelix/Anonymous-Q-and-A">question box</a>, <a href="https://github.com/jingfelix/Anonymous-Q-and-A">BiliFM</a> and <a href="">My Cloud</a>
                (haven't finished yet) . I tried for the Bingyan Club, but dropped out during the internship phase.
            </p>
            <p>
                You can find me at <a href="https://github.com/jingfelix">GitHub</a>,
                <a href="https://www.zhihu.com/people/jing-tian-yi-26">Zhihu</a>
                or <a href="mailto:jingfelix@outlook.com">E-mail</a>.
            </p>
        </div>
    </div>
    <div class="block one">
        <div id="slogan">
            Code, <br>
            Love, <br>
            Design.
        </div>

    </div>

</body>
<script>
    let a_list = document.querySelectorAll('a');
    var i = 0;
    for (len = a_list.length; i < len; i++) {
        a_list[i].onmouseover = function () {
            this.style.textDecoration = 'underline';
        }
        a_list[i].onmouseout = function () {
            this.style.textDecoration = 'none';
        }
    }
</script>

</html>