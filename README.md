# NeuralFlappyBird


## Reasons for why / Technologies used

The reason for creating this is because there was a need for me to understand the amount of neurons and the more complicated parts of python so i decided to make a flappy bird. For the project technologies i used Numpy pygame and my own brain code that uses Numpy as a dependency these technologies allowed me to run my code efficiently and without much hastle.

## Optimizations

In general, the system doesnt really demonstrate optimization however it does use numpy for the brain and the calculations instead of making my own.

## Description

This project showcases a simple representation of my own interpretation of Flappy Bird in this case the ball is the bird and the bars that are moving towards the screen are the pipes. However, in this simulation there's a brain in each ball and when all of them are no longer alive the simulation creates copies of the best in this case the one who makes it through the most pipes with slight mutation/variations in order to encourage new paths and actions, and as time goes on new generations will learn how to navigate between the pipes and 'learn'.

## Run Locally

Clone the project

```bash
git clone https://github.com/Nocivofrank/NeuralFlappyBird.git
cd NeuralFlappyBird
```

Install dependencies:

```
pip install -r requirements.txt
```

Open terminal in project root directory and run

```bash
python main.py
```

## Authors

- [@Nocivofrank](https://www.github.com/Nocivofrank)

