# Import libraries
import requests
import bs4 as bs
import pandas as pd
import os


# Creating Computer Science QA for Database
def computerscience():
    link = "https://www.indeed.com/career-advice/interviewing/computer-science-interview-questions"
    resp = requests.get(link)
    soup = bs.BeautifulSoup(resp.text, 'html.parser')
    questions = []
    answers = []
    for question in soup.find_all('h3')[:-3]:
        question = question.text
        questions.append(question)
    
    for answer in soup.find_all('p', {'class' : 'styles-module--contentSection--_QWYk'})[4:]:
        try:
            answer = answer.find('em').string
        except:
            answer = ""

        if not answer == '':
           answers.append(answer)
    
    return questions, answers



# Creating Accounting QA for Database
def accounting():
    link = "https://corporatefinanceinstitute.com/resources/careers/interviews/accounting-interview-questions/"
    resp = requests.get(link)
    soup = bs.BeautifulSoup(resp.text, 'html.parser')
    questions = []
    answers = []
    for question in soup.find_all('h4'):
        question = question.text
        question = question[3:]
        questions.append(question)
    for answer in soup.find_all('p')[5:34]:
        answer = answer.text
        answer = answer.replace("\xa0", "")
        if not answer == '':
            answers.append(answer)
    return questions, answers


# Creating Finance QA for Database
def finance():
    link = "https://www.wallstreetprep.com/knowledge/finance-interview-questions-and-answers/"
    resp = requests.get(link)
    soup = bs.BeautifulSoup(resp.text, 'html.parser')
    questions = []
    answers = []
    for question, answer in zip(soup.find_all('h3'), soup.find_all('p')[12:25]):
        question = question.find('span').text
        question = question.replace("Q: ", "")
        questions.append(question)
        answer = answer.text
        answer = answer.replace("A: ", "")
        answers.append(answer)
    return questions, answers

# Creating Mechanical Engineering QA for Database
def mecheng():
    link = "https://www.apollotechnical.com/mechanical-engineering-interview-questions-to-ask-candidates/"
    resp = requests.get(link, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'})
    soup = bs.BeautifulSoup(resp.content, 'html.parser')
    questions = []
    answers = []
    for question in soup.find_all('h3')[16:-9]:
        question = question.find('span').string
        questions.append(question)
    check_doubles = []
    for answer in soup.find_all('p', {'class': 'has-medium-font-size'})[28:47]:

        if answer.find_next().name == 'p':
            next_tag = answer.find_next().text
            check_doubles.append(next_tag)

        elif answer.find_next().name == 'a':
            next_tag = answer.find_next()
            next_tag = next_tag.find_next()
            if next_tag.name == 'p':
                check_doubles.append(next_tag.text)

        else:
            next_tag = ''
        answer = answer.text
        if answer in check_doubles:
            pass
        else:
            answer = answer.replace("\xa0","")
            answers.append(answer)
    return questions, answers


folder = "dataframes"
computerscience = computerscience()
accounting = accounting()
finance = finance()
mecheng = mecheng()
categories = [computerscience, accounting, finance, mecheng]
names = ['computerscience','accounting','finance','mecheng']
if not os.path.exists(folder):
    os.makedirs(folder)

for x in range(len(names)):
    path = names[x] + ".csv"
    df = pd.DataFrame({'Questions' : categories[x][0],
                       'Answers' : categories[x][1]}, columns=['Questions', 'Answers'])
    df.to_csv(os.path.join(folder, path))

